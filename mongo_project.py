import pymongo
import os

MONGODB_URI ="mongodb://root:r00tUser@myfirstcluster-shard-00-00.w52aw.mongodb.net:27017,myfirstcluster-shard-00-01.w52aw.mongodb.net:27017,myfirstcluster-shard-00-02.w52aw.mongodb.net:27017/myTestDB?ssl=true&replicaSet=atlas-n79620-shard-0&authSource=admin&retryWrites=true&w=majority"
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e