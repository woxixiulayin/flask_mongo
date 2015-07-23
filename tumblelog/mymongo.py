from mongoengine import *
import sys

class Comment(EmbeddedDocument):
    name = StringField(max_length = 100)
    content = StringField()


class User(Document):
    email = StringField(required=True)
    name = StringField(max_length=50, required=True)


class Post(Document):
    title = StringField(max_length=100, required=True)
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length = 30))
    comments  = ListField(EmbeddedDocumentField(Comment))
    meta  = {'allow_inheritance': True}

class TextPost(Post):
    content = StringField()

class ImagePost(Post):
    image_path = StringField()

class LinkPost(Post):
    link_url = StringField()

class Tieba_post_doc(Document):
    url_link = StringField(max_length=300, required=True)
    rep_num = IntField(required=True)
    title = StringField(max_length=100, required=True)
    # first_time = StringField(max_length=20, required=True)
    last_time = StringField(max_length=20, required=True)
    author = StringField(max_length=30, required=True)
    # tags = Field()
    body = StringField(required=True)
    meta  = {'allow_inheritance': True}

for post in Tieba_post_doc.objects():
    print post.title
