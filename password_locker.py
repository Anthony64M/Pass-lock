import pyperclip
from user_credentials import User, Credentials

def create_User(fname,lname,password):
    '''
    This Function creates a new user account
    '''
    new_user = User(fname,lname,password)
    return new_user

