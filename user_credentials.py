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

        def generate_password(size=16, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
            """
            Generatea 16 character password for credentials.
            """
            gen_pass=''.join(random.choice(char) for _ in range(size))
            return gen_pass


    
        @classmethod
        def display_credentials(cls,user_name):
            """
            Method display list of saved credentials.
            """
            user_credentials_list = []
            for credentials in cls.credentials_list:
                    if credentials.user_name == user_name:
                            user_credentials_list.append(credentials)
            return user_credentials_list

        @classmethod
        def find_by_site_name(cls,site_name):
            """
            TaKES IN A SITE_name and returns a credential that matches the site_name.
            """
            for credential in cls.credentials_list:
                    if credential.site_name == site_name:
                            user_credentials_list.append(credential)
            return user_credentials_list

        @classmethod
        def copy_credentials(cls,site_name):
            """
            Copies a credential info after the credentials site_name has been entered.
            """
            find_credentials = Credentials.find_by_site_name(site_name)
            return pyperclip.copy(find_credential.password)


