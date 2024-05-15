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
        # Add more geometry assertions for other widgets as needed

    def test_login(self):
        # Simulate login process and assert expected behavior
        self.page.username_entry.insert(0, "test@example.com")
        self.page.password_entry.insert(0, "password")
        self.page.log_in()  # Assuming the login function logs the user in
        # Add assertions for expected behavior after login

    def test_signup(self):
        # Simulate signup process and assert expected behavior
        self.page.sign_up()  # Assuming the signup function redirects to signup page
        # Add assertions for expected behavior after signup

if __name__ == "__main__":
    unittest.main()
