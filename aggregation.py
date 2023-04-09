import pymongo
from bson import ObjectId
client = pymongo.MongoClient("mongodb://admin:Idk6fa@localhost:27017/whayn?authSource=admin")
mydb = client['whayn']

users = mydb['user']

# print(dir(users))
# print(dir(users.find({})))
pipeline = [
    {
        "$group":{
            "_id":"$user_type",
            "count":{"$sum":1}
        }
    },{
        "$sort":{
            "count":1
        }
    }
]
# for i in users.aggregate(pipeline=pipeline):
#     print(i)
    
# print(users.count_documents({}))