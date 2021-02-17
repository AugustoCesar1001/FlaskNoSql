from app import mongo

def mongo_created_user(username, hashed_password, name, email, cellphone):
    id = mongo.db.users.insert(
                {'username': username, 'password': hashed_password, 'name': name, 'email' : email, 'cellphone': cellphone}
    )
    return id