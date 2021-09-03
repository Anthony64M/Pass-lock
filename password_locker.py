import pyperclip
from user_credentials import User, Credentials

def create_user(fname,lname,password):
    '''
    This Function creates a new user account
    '''
    new_user = User(fname,lname,password)
    return new_user

def save_user(user):
    '''
    This Function saves new user information
    '''
    User.save_user(user)