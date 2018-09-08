import unittest
from models import pitch

Pitch=pitch.Pitch

class PitchTest(unittest.TestCase):
    '''
    test class to test pitch class behaviour
    '''

def setUp(self):
    '''
    this method will run before each test
    '''
    self.new_pitch = Pitch(1234, 'Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time.-Thomas Edison')

def test_instance(self):
    self.assertTrue(isinstance(self.new_pitch, Pitch)) 

if __name__ == '__main__':
    unittest.main()       