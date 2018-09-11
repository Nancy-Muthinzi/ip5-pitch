import unittest
from app.models import Pitch
from app import db

class UserModelTest(unittest.TestCase):

    def tearDown(self):
        '''
        This method does clean up after each test has run.
        '''
        User.user_list = []

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_pitch = User("Nancy", "Muthinzi", "nanciekathini@gmail.com", "ab12")

    def test_init(self):
        '''
        Test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name, "Nancy")
        self.assertEqual(self.new_user.last_name, "Muthinzi")
        self.assertEqual(self.new_user.email_address, "nanciekathini@gmail.com")
        self.assertEqual(self.new_user.password, "ab12")

    def test_save_user(self):
        '''
        Test_save_user test case to test if the user object is saved into the user list.
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_user(self):
        '''
        This is to check if we can sve multiple user objects to our user_list.
        '''
        self.new_user.save_user()
        test_user = User("Nancy", "Muthinzi", "nanciekathini@gmail.com", "ab12")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        '''
        This is to test if we can remove a user from our user list.
        '''
        self.new_user.save_user()
        test_user = User("Nancy", "Muthinzi", "nanciekathini@gmail.com", "ab12")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)
