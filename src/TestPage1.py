import unittest
import tkinter as tk
from WAIC_3 import Page1

class TestPage1(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.page = Page1(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_widgets_existence(self):
        self.assertIsInstance(self.page.title_label, tk.Label)
        self.assertIsInstance(self.page.login_body, tk.Frame)
        self.assertIsInstance(self.page.username_label, tk.Label)
        self.assertIsInstance(self.page.username_entry, tk.Entry)
        self.assertIsInstance(self.page.password_label, tk.Label)
        self.assertIsInstance(self.page.password_entry, tk.Entry)
        self.assertIsInstance(self.page.additional_label, tk.Label)
        self.assertIsInstance(self.page.meditation_text_label, tk.Label)
        self.assertIsInstance(self.page.login_button, tk.Button)
        self.assertIsInstance(self.page.signup_button, tk.Button)

    def test_widgets_geometry(self):
        self.assertEqual(self.page.title_label.winfo_geometry(), "+0+0")
        self.assertEqual(self.page.login_body.winfo_width(), 400)
        self.assertEqual(self.page.login_body.winfo_height(), 500)

    def test_login(self):
        self.page.username_entry.insert(0, "test@example.com")
        self.page.password_entry.insert(0, "password")
        self.page.log_in()  

    def test_signup(self):
        self.page.sign_up() 
if __name__ == "__main__":
    unittest.main()
