from pymongo import MongoClient
from info import MONGODB_URI

client = MongoClient(MONGODB_URI)
db = client['uservsit']
collection = db['vists']

def record_visit(user: int, count: int):
    existing_visit = collection.find_one({
        "user": user
    })   
    if not existing_visit:
        collection.insert_one({
            "user": user,
            "count": count
        })
    else:
        user_data = {
            "count": count
        }
        collection.update_one({"user": user}, {"$set": user_data})

def record_withdraw(user, withdraw):
    existing_visit = collection.find_one({
        "user": user
    })
    if existing_visit:
        user_data = {
            "withdraw": withdraw
        }
        collection.update_one({"user": user}, {"$set": user_data})

def get_count(user):
    existing_visit = collection.find_one({
        "user": user
    })
    if existing_visit:
        return existing_visit["count"]  
    else: 
        return None

def get_withdraw(user):
    existing_visit = collection.find_one({
        "user": user
    })
    if existing_visit:
        return existing_visit["withdraw"]  
    else: 
        return False

def get_visits():
    visits = collection.find()
    return [(visit["user"], visit["count"]) for visit in visits]
