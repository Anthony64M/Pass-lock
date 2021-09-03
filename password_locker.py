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

def verify_user(first_name,password):
    '''
    This Function verifies existing user information before credentials are created
    '''
    checking_user = Credentials.check_user(first_name,password)
    return checking_user
    