from app import mongo
from bson.objectid import ObjectId

def mongo_created_user(username, hashed_password, name, email, cellphone):
    id = mongo.db.users.insert(
                {'username': username, 'password': hashed_password, 'name': name, 'email' : email, 'cellphone': cellphone})
    return id


def mongo_get_user(id):
    user = mongo.db.users.find_one({'_id' : ObjectId(id)})
    return user


def mongo_get_all_users():
    user = mongo.db.users.find()
    return user


def mongo_update_user(id, username, hashed_password, name, email, cellphone):
    user = mongo.db.users.update_one({'_id' : ObjectId(id)}, {'$set' :
                {'username': username, 'password': hashed_password, 'name': name, 'email' : email, 'cellphone': cellphone}})
    return user

def mongo_delete_user(id):
    user = mongo.db.users.delete_one({'_id': ObjectId(id)})
    return user