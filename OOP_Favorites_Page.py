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

    def create_widgets(self):
        self.header = Label(self.root, text="My Favorites", fg="black", bg="lightgrey", width=100, height=5, font=("Arial", 16))
        self.header.pack(side="top", padx=10, pady=50)

        self.favorites_body = Frame(self.root, width=700, height=500, bg="white", highlightthickness=2, highlightcolor="black")
        self.favorites_body.place(x=250, y=200)

        self.back_home_button = Button(self.root, text="Back to Home", width=20, height=3, bg="lightgrey", font=("Arial", 13, "bold"), command=self.show_home_page_from_favorites_page)
        self.back_home_button.place(x=((self.screen_width - self.back_home_button.winfo_reqwidth()) // 2), y=625)
