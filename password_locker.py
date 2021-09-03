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

                elif short_code == 'ca':
                         print("-"*60)
                         print(' ')
                         print('To create a new account:')
                         first_name = input('Enter your first name - ').strip()
                         last_name = input('Enter your last name - ').strip()
                         password = input('Enter your password - ').strip()
                         save_user(create_user(first_name,last_name,password))
                         print(" ")
                         print(f'New Account Created for: {first_name} {last_name} using password: {password}')
                elif short_code == 'li':
                         print("-"*60)
                         print(' ')
                         print('To login, enter your account details:')
                         user_name = input('Enter your first name - ').strip()
                         password = str(input('Enter your password - '))
                         user_exists = verify_user(user_name,password)
                         if user_exists == user_name:
                                print(" ")
                                print(f'Welcome {user_name}. Please choose an option to continue.')
                                print(' ')
                                while True:
                                        print('Navigation codes: \n cc-Create a Credential \n dc-Display Credentials \n copy-Copy Password \n ex-Exit')
                                        short_code = input('Enter a  choice').lower().strip()
                                        print("-"*60)
                                        if short_code == 'ex':
                                               print(" ")
                                               print(f'Goodbye {user_name}')
                                               break
                                        elif short_code == 'cc':
                                                print(' ')
                                                print('Enter your credential details:')
                                                site_name = input('Enter the site\'s name- ').strip()
                                                account_name = input('Enter your account\'s name - ').strip()
                                                while True:
                                                        print(' ')
                                                        print("-"*60)
                                                        print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
                                                        psw_choice = input('Enter an option: ').lower().strip()
                                                        print("-"*60)
                                                        if psw_choice == 'ep':
                                                                print(" ")
                                                                password = input('Enter your password: ').strip()
                                                                break
                                                        elif psw_choice == 'gp':
                                                                password = generate_password()
                                                                break
                                                        elif psw_choice == 'ex':
                                                            break
                                                        else:
                                                                print("Sorry! Wrong entry.Try again.")
                                                save_credential(create_credential(user_name,site_name,account_name,password))
                                                print(' ')
                                                print(f'Credential Created: Site Name: {site_name} - Account Name: {account_name} - Password: {password}')
                                                print(' ')
                                        elif short_code == 'dc':
                                            print(' ')
                                            if display_credential(user_name):
                                                print('Here is a list of all your credentials')
                                                print(' ')
                                                for credential in display_credential(user_name):
                                                        print(f'Site Name: {credential.site_name} - Account Name: {credential.account_name} - Password: {credential.password}')
                                                        print(' ')
                                            else:
                                                        print(' ')
                                                        print("Your Credentials are not saved.")
                                                        print(' ')
                                        elif short_code == 'copy':
                                                print(' ')
                                                chosen_site = input('Enter the site name for the credential password to copy: ')
                                                copy_credentials(chosen_site)
                                                print(' ')
                                        else:
                                               print("Sorry! Invalid Entry. Try again.")
                                                





					                