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
def generate_password():
    """
    Function to generate password.
    """    
    gen_pass = Credentials.generate_password()
    return gen_pass

def create_credential(user_name,site_name,password):
     """
     Function to create new credential.
     """
     new_credential=Credentials(user_name,site_name,account_name,password)
     return new_credential

def save_credential(credential):
    """
    Function to save new credential information after creation.
    """
    Credentials.save_credential(credential)

def display_credential(user_name):
    """
    Function to display credential information saved by user.
    """
    return Credentials.display_credential(user_name)

def copy_credentials(site_name):
    """
    Function to copy credential information  to clipboard.
    """
    return Credentials.copy_credentials(site_name)

def main():
        print(' ')
        print("Hello from Anthony, Welcome to Pass-Lock.")
        while True:
                print(' ')
                print("-"*60)
                print("Codes for navigation: \n ca-Create an Account \n li-Login \n ex-Exit")
                short_code = input("Enter Choice: ").lower().strip()
                if short_code == 'ex':
                        break 

