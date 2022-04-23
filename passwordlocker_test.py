import unittest #importing the unittest module
from passwordlocker import User
from passwordlocker import Credentials

class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User('CalebKabaya', 'Mbuguack')

    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.name,'CalebKabaya')
        self.assertEqual(self.new_user.password,'Mbuguack')

if __name__ == '__main__':
    unittest.main()        