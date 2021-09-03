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
               