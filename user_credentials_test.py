import unittest
import pyperclip
from user_credentials import User, Credentials

class TestUser(unittest.TestCase):
    	'''
	        Test class that defines test cases for the user class behaviours.

	        Args:
	         unittest.TestCase: helps in creating test cases
	    '''
	def setUp(self):
            """
            Function to create a user account before each test.
            """
            self.new_user = User("Anthony","Mu\tu\ku","K8ddj6m2l")

        def test_init_(self):
            """
            Test to if check the initialization/creation of user instances is properly done.
            """
            self.assertEqual(self.new_user.first_name, "Anthony")
            self.assertEqual(self.new_user.last_name, "Mu\tu\ku")
            self.assertEqual(self.new_user.password, "K8ddj6m2l")

        def test_save_user(self):
            """
            Test to check if the new users info is saved into the users list.
            """
            self.new_user.save_user()
            self.assertEqual(len(User.users_list),1)
            
class TestCredentials(unittest.TestCase):
    """
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: helps in creating test cases
    """
    def test_check_user(self):
        """
        Function to test whether the login in function check_user works as expected.
        """
        self.new_user = User("Anthony", "Mu\tu\ku","K8ddj6m2l")
        self.new_user.save_user()
        user2 = User("Jymal", "An\tho\ny", "K8ddj6m2l")
        user2.save_user()

        for user in User.users_list:
                if user.first_name == user2.first_name and user.password == user2.password:
                        current_user = user.first_name
        return current_user

        self.assertEqual(current_user,Credential.check_user(user2.password,user2.first_name))

def setUp(self):
    """
    Function to create an account's credentials before each test.
    """
    self.new_credential = Credentials("Anthony", "Instagram", "jymal_anthony", "K8ddj6m2l")
def test__init__(self):
        """
        Test to if check the initialization/creation of credential instances is properly done.
        """
        self.assertEqual(self.new_credential.user_name,"Anthony")
        self.assertEqual(self.new_credential.site_name,"Instagram")
        self.assertEqual(self.new_credential.account_name,"jymal_anthony")
        self.assertEqual(self.new_credential.password,"K8ddj6m2l")

def test_save_credentials(self):
        """
        Test to check if the new credential info is saved into the credentials list.
        """
        self.new_credential.save_credentials()
        pinterest = Credentials('Jymal','Pinterest','Jymal64','K8ddj6m2l')
        pinterest.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

def tearDown(self):
        """
        Function to clear the credentials list after every test
        """
        Credentials.credentials_list = [] 
        User.users_list = []

def test_display_credentials(self):
    """
    Test to check if the display_credentials method, displays the correct credentials.
    """
    self.new_credential.save_credentials()
    pinterest = Credentials('Jymal','Pinterest','Jymal64','K8ddj6m2l')
    pinterest.save_credentials()
    gmail = Credentials("Jymal","Gmail","Jymal","K8ddj6m2l")
    gmail.save_credentials()
    self.assertEqual(len(Credentials.display_credentials(pinterest.user_name)),2)

def test_find_by_site_name(self):
    """
    Test to check if the find_by_site_name method returns the correct credential.
    """
    self.new_credential.save_credentials()
    pinterest = Credentials('Jymal','Pinterest','Jymal64','K8ddj6m2l')
    pinterest.save_credentials()
    credentials_exists = Credentials.find_by_site_name("Pinterest")
    self.assertEqual(credentials_exists.pinterest)

def test_copy_credential(self):
    """
    Test to check if the copy a credential method copies the correct credential.
    """
    self.new_credential.save_credentials()
    pinterest = Credentials('Jymal','Pinterest','Jymal64','K8ddj6m2l')
    pinterest.save_credentials()
    find_credential = None
    for credential in Credentials.user_credential_list:
                    find_credential = credential.find_by_site_name(credential.site_name)
                    return pyperclip.copy(find_credential.site_name)
    Credentials.copy_credentials(self.new_credential.site_name)
    self.assertEqual("K8ddj6m2l", pyperclip.paste())
    print(pyperclip.paste())

if __name__ == '__main__':
        unittest.main(verbosity=2)            
