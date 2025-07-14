from pymongo import MongoClient

def save_to_mongo(data_list):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["structured_data"]
    collection = db["extracted_info"]

    if isinstance(data_list, list) and all(isinstance(item, dict) for item in data_list):
        collection.insert_many(data_list)  # ✅ insert_many for list of dicts
    else:
        raise ValueError("Data must be a list of dictionaries")
