from mongoengine import *

connect(db="book",host="mongodb+srv://maksym_learner:ssXumE4galkz66sP@maksympractise.jz4oll5.mongodb.net/")

class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User)
    meta = {'allow_inheritance': True}

class TextPost(Post):
    content = StringField()

class ImagePost(Post):
    image_path = StringField()

class LinkPost(Post):
    link_url = StringField()

if __name__ == '__main__':
    ross = User(email='ross@example.com', first_name='Ross', last_name='Lawley').save()

    john = User(email='john@example.com')
    john.first_name = 'John'
    john.last_name = 'Lawley'
    john.save()
    post1 = TextPost(title='Fun with MongoEngine', author=ross)
post1.content = 'Took a look at MongoEngine today, looks pretty cool.'
post1.tags = ['mongodb', 'mongoengine']
post1.save()

post2 = LinkPost(title='MongoEngine Documentation', author=john)
post2.link_url = 'http://docs.mongoengine.org/'
post2.tags = ['mongoengine']
post2.save()
    