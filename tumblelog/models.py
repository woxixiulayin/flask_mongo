import datetime
from flask import url_for
from tumblelog import db

class Comment(db.EmbeddedDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    body = db.StringField(verbose_name="Comment", required=True)
    author = db.StringField(verbose_name="Name", max_length=255, required=True)

class Post(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=True)
    body = db.StringField(required=True)
    comments = db.ListField(db.EmbeddedDocumentField('Comment'))

    def get_absolute_url(self):
        return url_for('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'slug'],
        'ordering': ['-created_at']
    }

class Tieba_post_doc(db.Document):
    url_link = db.StringField(max_length=300, required=True)
    rep_num = db.IntField(required=True)
    title = db.StringField(max_length=100, required=True)
    # first_time = StringField(max_length=20, required=True)
    last_time = db.StringField(max_length=20, required=True)
    author = db.StringField(max_length=30, required=True)
    # tags = Field()
    body = db.StringField(required=True)
