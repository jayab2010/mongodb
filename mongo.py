import pymongo
import os

MONGODB_URI ="mongodb://root:<password>@myfirstcluster-shard-00-00.w52aw.mongodb.net:27017,myfirstcluster-shard-00-01.w52aw.mongodb.net:27017,myfirstcluster-shard-00-02.w52aw.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-n79620-shard-0&authSource=admin&retryWrites=true&w=majority"
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

documents = coll.find()

for doc in documents:
    print(doc)


