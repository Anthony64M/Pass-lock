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

    class Credential:
        """
        The class creates account credentials, generate password and save them.
        """

        #  Class Variables
        credentials_list = []
        user_credentials_list = []
        @classmethod
        def check_user(cls,first_name,password):
            """
            A method that checks if a username and password inserted matches the entry in the user_list.
            """

            current_user = ''
            for user in User.users_list:
                    if (user.first_name == first_name and user.password == password):
                        current_user = user.first_name
            return current_user 
        def __init__(self,user_name,site_name,account_name,password):
            """
            Defines the properties for each user will have.
            """
            # Instance variables
            self.user_name = user_name
            self.site_name = site_name
            self.account_name = account_name
            self.password = password
        
        def save_credentials(self):
            """
            Saves a newly created user instance.
            """
            # global user_list
            Credential.credentials_list.append(self)

        def generate_password(size=16, char=string.ascii.uppercase+string.ascii_lowercase+string.digits):
            """
            Generatea 16 character password for credentials.
            """
            gen_pass=''.join(random.choice(char) for _ in range(size))
            return gen_pass
            