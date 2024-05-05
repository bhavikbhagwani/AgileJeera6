from tkinter import Toplevel, Label, PhotoImage

class ProfileWindow:
    def __init__(self):
        self.root = Toplevel()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.title("Profile Window")
        self.root.configure(bg="#808080")
        self.root.withdraw()  # Hide the window initially
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.screen_width}x{self.screen_height}")
        self.create_widgets()

    