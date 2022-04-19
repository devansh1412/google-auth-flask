from enum import unique
from utils import keygenerator

from model.model import User
from model.model import db

key_object = keygenerator.KeyGenerator()

from flask_login import UserMixin

class google_user(UserMixin):
    def __init__(self, id_, name, email):
        self.id = id_
        self.name = name
        self.email = email

def create_user(username, email):
    #check if already exists
    try:
        users = User.query.filter_by(username=username).all()
    except Exception as e:
        return(str(e))
    if len(users) != 0:
        return None
    # get the api_key for this user
    key_object.generateKey(10)
    dev_key = key_object.getKey()
    # get the quota from config.py
    # quota = config.ALLOWED_API_CALL
    # insert item into user table
    print("insert item into user table step called")
    # try:
    #     new_user = User(
    #             username = username,
    #             email = email,
    #             key = dev_key,
    #     )
    #     db.session.add(new_user)
    #     db.session.commit()
    #     return dev_key
    # except Exception as e:
    #     return(str(e))

def get_user(username):
    # check username and password
    return google_user( "tester", "tester", "tester")
    # try:
    #     users = User.query.filter_by(username=username).first()
    #     return users
    # except Exception as e:
	#     return None

def update_key(username):
    # check username and password
    try:
        users = User.query.filter_by(username=username).first()
        if users != None:
            # get a new key
            key_object.generateKey(10)
            dev_key = key_object.getKey()   
            # update the key to user table
            updated_user = User.query.filter_by(username = username).first()
            updated_user.key = dev_key
            db.session.commit()
            return dev_key
        else:
            return None
    except Exception as e:
	    return(str(e))
    