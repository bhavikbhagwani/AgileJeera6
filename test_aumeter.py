import unittest
from unittest.mock import patch, MagicMock
import database
from tkinter import messagebox
from firebase_admin import auth




class TestDatabase(unittest.TestCase):
    
    def test_init_database(self):
        database_test = database.Database()
        self.assertIsInstance(database_test, database.Database)


    def test_user_signs_up_successfully(self):
        
        test_database = database.Database()
    
        example_email = "name2@email.com"
        example_password = "password1234"

        success, user_ID = test_database.sign_up(example_email, example_password)

        user_ID_retrieved = test_database.get_user_ID()
        self.assertTrue(success)
        self.assertEqual(user_ID, user_ID_retrieved)


    def test_user_logs_in_successfully(self):

        
        
        test_database = database.Database()
    
        example_email = "name2@email.com"
        example_password = "password1234"

        success, user_ID = test_database.log_in(example_email, example_password)

        user_ID_retrieved = test_database.get_user_ID()
        self.assertTrue(success)
        self.assertEqual(user_ID, user_ID_retrieved)

    def test_user_signs_up_unsuccessfully(self):
        
        test_database = database.Database()
    
        example_email = "name2@email.com"
        example_password = "password1234"

        success, user_ID = test_database.sign_up(example_email, example_password)

        user_ID_retrieved = test_database.get_user_ID()
        self.assertFalse(success)
        self.assertIsNone(user_ID, user_ID_retrieved)


    def test_user_logs_in_successfully(self):

        
        test_database = database.Database()
    
        example_email = "namenotexist@email.com"
        example_password = "password1234"

        success, user_ID = test_database.log_in(example_email, example_password)

        user_ID_retrieved = test_database.get_user_ID()
        self.assertFalse(success)
        self.assertIsNone(user_ID, user_ID_retrieved)


    def test_adding_new_user_and_file_type(self):
        
        test_database = database.Database()

        example_email = "name3@email.com"
        example_password = "password12345"

        success, user_ID = test_database.sign_up(example_email, example_password)
        user_ID_retrieved = test_database.get_user_ID()
        self.assertTrue(success)
        self.assertEqual(user_ID, user_ID_retrieved)
        
        test_database.add_user(user_ID)
        email_retrieved = test_database.get_user_email()
        meditation_list_retrieved = test_database.get_meditation_list_for_this_user(user_ID)
        study_music_list_retrieved = test_database.get_study_music_list_for_this_user(user_ID)
        progress_retrieved = test_database.get_progress(user_ID)

        self.assertEqual(example_email, email_retrieved)
        self.assertIsInstance(example_email, str)

        self.assertEqual(meditation_list_retrieved, [1,2,3,4,5,6,7,8])
        self.assertIsInstance(meditation_list_retrieved, list)

        self.assertEqual(study_music_list_retrieved, [9,10,11,12,13,14,15,16])
        self.assertIsInstance(study_music_list_retrieved, list)

        self.assertEqual(progress_retrieved, 0)
        self.assertIsInstance(progress_retrieved, int)

        test_database.database.child("Users").child(user_ID).remove()




if __name__ == "__main__":
    unittest.main()