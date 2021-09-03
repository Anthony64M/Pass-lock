import pyperclip
import random
import string

# Global Variables
global users_list
class User:
    '''
    Class to create user accounts and save their data
    '''
    # Global user_list
    users_list = []
    def __init__(self,first_name,last_name,password):
        '''
        This method defines properties for each user.
        '''
        # instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):
        '''
        This functiond saves a newly created user instance.
        '''
        User.users_list.append(self)

        