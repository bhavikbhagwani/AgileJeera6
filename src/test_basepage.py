import unittest
import tkinter as tk
from whole_app_in_classes_2 import BasePage


class TestBasePage(unittest.TestCase):
    def test_init(self):
        root = tk.Tk()
        base_page = BasePage(root)

  
        self.assertEqual(base_page.master, root)

if __name__ == '__main__':
    unittest.main()
