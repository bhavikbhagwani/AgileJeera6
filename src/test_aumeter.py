"""
UNIT TESTING
"""
from tkinter import *
import unittest

import database, app


class TestDatabase(unittest.TestCase):
    """Test the Database Class."""



    def test_init_database(self):
        """Test Init of Dice."""
        database_test = database.Database()
        self.assertIsInstance(database_test, database.Database)

    def test_user_signs_up_successfully(self):
        """Test User Signing Up Successfully."""
        test_database = database.Database()
    
        example_email = "name2@email.com"
        example_password = "password1234"

        success, user_ID = test_database.sign_up(example_email, example_password)

        user_ID_retrieved = test_database.get_user_ID()
        self.assertTrue(success)
        self.assertEqual(user_ID, user_ID_retrieved)
    

    def test_user_signs_up_unsuccessfully(self):
        """Test User Signing Up UnSuccessfully."""
        test_database = database.Database()

        #already existing email and password
        example_email = "name2@email.com"
        example_password = "password1234"

        success, user_ID = test_database.sign_up(example_email, example_password)

        user_ID_retrieved = test_database.get_user_ID()
        self.assertFalse(success)
        self.assertIsNone(user_ID, user_ID_retrieved)

    def test_user_logs_in_unsuccessfully(self):
        """Test User Logging In UnSuccessfully."""
        test_database = database.Database()

        example_email = "namenotexist@email.com"
        example_password = "password1234"

        success, user_ID = test_database.log_in(example_email, example_password)

        user_ID_retrieved = test_database.get_user_ID()
        self.assertFalse(success)
        self.assertIsNone(user_ID, user_ID_retrieved)

    

    def test_adding_new_user_and_file_type(self):
        """Test Adding User And Correct File Type of Database Info."""
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

    def test_user_logs_in_successfully(self):
        """Test User Logging In Successfully."""
        test_database = database.Database()

        example_email = "name3@email.com"
        example_password = "password12345"

        success, user_ID = test_database.log_in(example_email, example_password)

        user_ID_retrieved = test_database.get_user_ID()
        self.assertTrue(success)
        self.assertEqual(user_ID, user_ID_retrieved)

    
"""
The testing of the Database will only work once after run. To test it again contact aumeterteam@gmail.com
"""
print("\nThe testing of the Database will only work once after run. To test it again contact aumeterteam@gmail.com\n")

class TestBasePage(unittest.TestCase):
    def test_init(self):
        root = Tk()
        base_page = app.BasePage(root)

  
        self.assertEqual(base_page.master, root)

class TestSounds(unittest.TestCase):
    def setUp(self):
        self.sounds = app.Sounds()

    def test_get_sound_url(self):
        # Test a valid sound number
        self.assertEqual(self.sounds.get_sound_url(1), "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/meditation_1.mp3?alt=media&token=b22aaf93-2c27-4477-b96e-c351afdef7bc")
        # Test an invalid sound number
        self.assertIsNone(self.sounds.get_sound_url(100))

    def test_get_sound_name(self):
        # Test a valid sound number
        self.assertEqual(self.sounds.get_sound_name(1), "Breathing")
        # Test an invalid sound number
        self.assertIsNone(self.sounds.get_sound_name(100))


if __name__ == "__main__":
    unittest.main()
    