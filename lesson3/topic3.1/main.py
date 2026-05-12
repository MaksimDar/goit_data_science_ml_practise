# from bson.objectid import ObjectId

# from pymongo import MongoClient
# from pymongo.server_api import ServerApi

# terminal_command = 'poetry run python3 main.py'
# client = MongoClient(
#     "mongodb+srv://maksym_learner:ssXumE4galkz66sP@maksympractise.jz4oll5.mongodb.net/",
#     server_api=ServerApi('1')
# )

# db = client.book

# result_one = db.cats.insert_one(
#     {
#         "name": "barsik",
#         "age": 3,
#         "features": ["ходить в капці", "дає себе гладити", "рудий"],
#     }
# )

# # print(result_one.inserted_id)

# # result_many = db.cats.insert_many(
# #     [
# #         {
# #             "name": "Lama",
# #             "age": 2,
# #             "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
# #         },
# #         {
# #             "name": "Liza",
# #             "age": 4,
# #             "features": ["ходить в лоток", "дає себе гладити", "білий"],
# #         },
# #     ]
# # )
# # print(result_many.inserted_ids)
# # for cat in db.cats.find():
# #     print(cat)
# # result = db.cats.find_one({"_id": ObjectId('69fe69fc4639cc5dea867479')})
# # print(result)



# # db.cats.update_one({"name": 'Lama'}, {'$set': {'age': 8}})
# # result = db.cats.find_one({"name": "Lama"})
# # print(result)

# db.cats.delete_one({"name": 'Lama'})
# result = db.cats.find_one({"name": 'Lama'})
# print(result)



