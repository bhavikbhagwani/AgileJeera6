from tkinter import Tk, Label, Entry, Frame, Button

class LoginWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("Aumeter")
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.screen_width}x{self.screen_height}+0+0")
        self.root.config(background='#D8A9B3')
        self.create_widgets()

    
