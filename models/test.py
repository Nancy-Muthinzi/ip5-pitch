import unittest
from models import pitch

Pitch=pitch.Pitch

class PitchTest(unittest.TestCase):
    '''
    test class to test pitch class behaviour
    '''

def setUp(self):
    '''
    this will run before each test
    '''

def test_instance(self):
    self.assertTrue(isinstance(self.new_pitch, Pitch)) 

if __name__ == '__main__':
    unittest.main()       