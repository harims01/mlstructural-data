# db_ops.py
from pymongo import MongoClient

def save_to_mongo(data_dict):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["structured_data"]
    collection = db["entries"]
    collection.insert_one(data_dict)
