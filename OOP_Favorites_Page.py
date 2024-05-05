from tkinter import Toplevel, Label, Frame, Button

class FavoritesWindow:
    def __init__(self):
        self.root = Toplevel()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.title("Favorites Window")
        self.root.configure(bg="lightblue")
        self.root.withdraw()  # Hide the window initially
        self.favorites_list = []
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.screen_width}x{self.screen_height}")
        self.create_widgets()

    
