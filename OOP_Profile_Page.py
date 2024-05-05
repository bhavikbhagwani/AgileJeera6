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

    def create_widgets(self):
        # Set window title
        self.title_label = Label(self.root, text='Profile', font=("Georgia", 25, 'bold'),
                            bg='#808080', padx=20, pady=20)
        self.title_label.place(x=150, y=20)

        # Load and display profile image
        self.additional_image = PhotoImage(file=r'C:\Users\ghaza\OneDrive\Desktop\mainagile\AgileJeera6\image2.png')
        self.new_width, self.new_height = 60, 60  # Adjust the size as needed
        self.additional_image_resized = self.additional_image.subsample(int(self.additional_image.width() / self.new_width),
                                                    int(self.additional_image.height() / self.new_height))
        self.additional_label = Label(self.root, image=self.additional_image_resized, bg='#D8A9B3', relief='raised')
        self.additional_label.place(x=140, y=25, anchor='ne')

        # Load and display additional image 3
        self.image_3 = PhotoImage(file=r'C:\Users\ghaza\OneDrive\Desktop\mainagile\AgileJeera6\image3.png')
        self.new_width2, self.new_height2 = 800, 800 
        self.image3_resized = self.image_3.subsample(int(self.image_3.width() / self.new_width2),
                                                    int(self.image_3.height() / self.new_height2))
        self.Label_image_3 = Label(self.root, image=self.image3_resized, border=2, bg='#C0C0C0', relief='raised')
        self.Label_image_3.place(x=1200, y=180, anchor='ne')

    def on_closing(self):
        # Implement the functionality to handle closing of the window
        pass

    def run(self):
        self.root.mainloop()

# Usage:
profile_window = ProfileWindow()
profile_window.run()
