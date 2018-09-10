import unittest
from app.models import User
from app import db

class UserModelTest(unittest.TestCase):

    def setUp(self):
        '''
        method to run before every test
        '''

        self.user_Nancy = User(username = 'Nancy', password = 'banana', email = 'kathinimuthinzi@gmail.com')

    def tearDown(self):
        Review.query.delete()
        User.query.delete()

    def test_save_review(self):
        self.new_review.save_review()
        self.assertTrue(len(Review.query.all())>0)
            
    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('banana'))    