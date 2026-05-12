
import argparse
from bson.objectid import ObjectId

from pymongo import MongoClient
from pymongo.server_api import ServerApi

terminal_command = 'poetry run python3 main.py'
client = MongoClient(
    "mongodb+srv://maksym_learner:ssXumE4galkz66sP@maksympractise.jz4oll5.mongodb.net/",
    server_api=ServerApi('1')
)

db = client.book

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



def create(name,age,features):
    r = db.cats.insert_one({"name": name, "age": age, "features": features})
    return r


def read():
    return db.cats.find()

def update(pk, name,age,features):
    r = db.cats.update_one({"_id:": ObjectId(pk)},{
        "$set": {
            "name": name, 
            "age": age, 
            "features": features
        }
    })
    return r

def delete(pk):
    return db.cats.delete_one({'_id': ObjectId(pk)})


def main():
    match action:
        case 'create':
            r = create(name,age,features)
            print(r)
        case 'read':
            r = read()
            print([e for e in r])
        case 'update':
            r = update(pk,name,age,features)
            print(r)
        case 'delete':
            r = delete(pk)
            print(r)
        case _:
            print("Unknown command")

if __name__ == '__main__':
    main()





