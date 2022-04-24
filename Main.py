#!/usr/bin/env python3.8
from passwordlocker import User,Credentials
def create_new_user(name,password):
     """
     create new user function
     """
     new_user=User(name,password)
     return new_user

def save_user(user):
    """
    save new user function
    """
    user.save_user()

def dispay_user():
    """
    display an existing user
    """ 
    return User.show_user()

def login_user(name,password):
    """
    user login function
    """   
    check_user = Credentials.verfiy_user(name,password)
    return check_user

def create_new_credential(account,name,password):
    """
    create new credentials 
    """
    new_credentials= Credentials(account,name,password)
    return new_credentials
    
