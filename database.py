from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['whois']

def insert_to_db(data):
    if isinstance(data, dict):
        collection.insert_one(data)
    else:
        print("Data is not a dictionary")
