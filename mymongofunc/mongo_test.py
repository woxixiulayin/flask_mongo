from mongoengine import *

connect('test')

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

ross = User(email = 'zhigang@163.com', name = 'zhigang').save()

# post1 = TextPost(title = 'fun with it', author = 'jack' )
# post1.content = "this is a good test for mongoengine"
# post1.tags = ['mongoengine', 'test']
# post1.save()

# post2 = LinkPost(title='MongoEngine Documentation', author=ross)
# post2.link_url = 'http://docs.mongoengine.com/'
# post2.tags = ['mongoengine']
# post2.save()

for post in Post.objects(tags='mongoengine'):
    print post.title

