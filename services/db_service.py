from pymongo import MongoClient
from datetime import datetime
from config import MONGO_URI, DATABASE_NAME, COLLECTION_NAME

class DBService:
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[DATABASE_NAME]
        self.collection = self.db[COLLECTION_NAME]

    def insert_data(self, data):
        data_entry = {
            "data": data,
            "STATUS": "new",
            "insert_date": datetime.utcnow(),
            "update_date": datetime.utcnow(),
            "comments": "",
            "updatedBy": "Automation"
        }
        self.collection.insert_one(data_entry)

    def find_new_data(self, latest_data):
        existing_data = self.collection.find_one({"data": latest_data})
        return existing_data is None
