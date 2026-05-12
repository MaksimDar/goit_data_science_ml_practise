from mongoengine import connect, Document,StringField, IntField,ListField

import argparse
from bson.objectid import ObjectId

connect(db="book",host="mongodb+srv://maksym_learner:ssXumE4galkz66sP@maksympractise.jz4oll5.mongodb.net/")



terminal_command = 'poetry run python3 main.py'


parser = argparse.ArgumentParser(description="Servers Cats")
parser.add_argument( '--action', help='create, read, update,delete') # CRUD action

parser.add_argument('--id')
parser.add_argument('--name')
parser.add_argument('--age')
parser.add_argument('--features',nargs='+')

arg = vars(parser.parse_args())

action = arg.get('action')
pk = arg.get('id')
name = arg.get('name')
age = arg.get('age')
features = arg.get('features')

class Cat(Document):
    name = StringField(max_length=150, required=True)
    age = IntField(min_value=1, max_value=30)
    features = ListField(max_length=150)
    meta = {"collection": 'cats'}

def create(name,age,features):
    r = Cat(name=name, age=age, features=features)
    r.save()
    return r


def read():
    return Cat.objects.all()

def update(pk, name,age,features):
    cat = Cat.objects(id=pk).first()
    if cat:
        cat.update(name=name,age=age,features=features)
        cat.reload()
    return cat

def delete(pk):
    try: 
        cat = Cat.objects.get(id=pk) ### if rerror does not exist
        cat.delete()
    except cat.DoesNotExist:
        return None

    return cat


def main():
    match action:
        case 'create':
            r = create(name,age,features)
            print(r.to_mongo().to_dict())
        case 'read':
            r = read()
            print([e.to_json() for e in r])
        case 'update':
            r = update(pk,name,age,features)
            if r:
                print(r.to_mongo().to_dict())
        case 'delete':
            r = delete(pk)
            if r:
                print(r.to_mongo().to_dict())
        case _:
            print("Unknown command")

if __name__ == '__main__':
    main()