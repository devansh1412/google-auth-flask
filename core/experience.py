from enum import unique
from sqlite3 import Timestamp

from sqlalchemy import false
from utils import keygenerator

import time
from model.model import Blog, Company, User_Company_Blog, User
from model.model import db

ts = time.time()

def addExp(formData):
    _id = ""
    user_id = ""
    company_id = ""
    blog_id = ""
    _key = ""
    _article = formData["roundData"]
    _level = formData["level"]
    _firstName = formData["firstName"]
    _lastName= formData["lastName"]
    _email = formData["email"]
    _batch = formData["batch"]
    _company = formData["company"]
    _feedback = formData["feedback"]
    _status = formData["status"]
    _tags = formData["tags"]
    _cgpa = formData["cgpa"]

    if(userExists(_email)==False):
        #adds to user table
        try:
            new_user = User(
                id = user_id,
                email = _email,
                key = _key,
                admin = False,
                first_name = _firstName,
                last_name = _lastName,
                batch = _batch,
                cgpa = _cgpa,
                timestamp = time.time(),
                status = _status
            )
            db.session.add(new_user)
            db.session.commit()
            print("new user added")
        except Exception as e:
            return(str(e))
    else:
        user_id = User.query.filter_by(email=_email).first()["id"]
    if(companyExists(_company)==False):
        #add to company table
        try:
            new_company = Company(
                id = company_id,
                name = _company,
                timestamp = time.time(),
                status = _status
            )
            db.session.add(new_company)
            db.session.commit()
            print("new company added")
        except Exception as e:
            return(str(e))
    else:
        company_id = Company.query.filter_by(name=_company).first()["id"]
        
    try:
        new_blog = Blog(
                id = blog_id,
                level = _level,
                article = _article,
                timestamp = time.time(),
                status = _status,
                approved = False
        )
        db.session.add(new_blog)
        db.session.commit()
        print("new blog added")
    except Exception as e:
        return(str(e))
    try:
        new_blog = User_Company_Blog(
                id = _id,
                user_id = user_id,
                company_id = company_id,
                blog_id = blog_id,
                timestamp = time.time(),
                status = _status,
                selected= False
        )
        db.session.add(new_blog)
        db.session.commit()
        print("new blog added")
        return "Success"
    except Exception as e:
        return(str(e))
    

def userExists(_email):
    try:
        tuple = User.query.filter_by(email=_email).first()
        if tuple is not None:
            return True
        return False
    except Exception as e:
        return(str(e))

def companyExists(_name):
    try:
        tuple = Company.query.filter_by(name=_name).first()
        if tuple is not None:
            return True
        return False
    except Exception as e:
        return(str(e))

def viewExp(_id):
    #extract details from db
    try:
        tuple = User_Company_Blog.query.order_by(User_Company_Blog.timestamp.desc()).limit(15).all()
        if tuple is not None:
            print(tuple)
        return "Success"
    except Exception as e:
        return(str(e))
    #return tuple to frontend
    return

def search():
    #extract details as per search filters
    #return to frontend
    return

def approve():
    #to be done by himanshu
    return