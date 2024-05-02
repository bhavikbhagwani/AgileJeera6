import unittest
from unittest.mock import MagicMock
from database import Database

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = Database()
    
    def test_instance(self):
        self.assertIsInstance(self.db ,Database)




if __name__ == '__main__':
    unittest.main()