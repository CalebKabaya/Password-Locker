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
    
def save_credentials(credentials):
    """
    save credentials to the credentials list
    """
    credentials.save_datails()

def display_accounts_details():
    """
    show all the saved credential.
    """
    return Credentials.display_credentials()

def delete_credential(credentials):
    """
    delete a credentials from credentials list
    """
    credentials.delete_credentials()

def find_credential(account):
    """
    find a credential from the credential list using account
    """
    return Credentials.find_credential(account)

def check_credendtials(account):
    """
    check if the credentials entere exist in the list
    """
    return Credentials.credential_exist(account)

def generate_Password():
    '''
    generates a random password for the user.
    '''
    generated_new_password=Credentials.generatePassword()
    return generated_new_password

def copy_credentials(account):
    """
    A function that copies the credentials using the pyperclip
    """
    return Credentials.copy_credentials(account)

def main():
    print("Hello Welcome to PassWord Locker...\n Use these short codes: CA-- To Create New Account.\n LOG---to log in to your account if you already have an account\n ")
