from pymongo import MongoClient

def save_to_mongo(data_list):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["structured_data_db"]
    collection = db["structured_entries"]
    collection.insert_many(data_list)
