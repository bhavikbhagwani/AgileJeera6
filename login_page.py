import pyrebase
from tkinter import *
from write_to_data_base import save_to_data_base
from home_page2 import HomePage

class Login_page:
    def __init__(self):
        
        self.saver = save_to_data_base()
        self.master = Tk()
        self.master.title("Aumeter")
        self.homepage = HomePage(self)

        # Get the screen width and height
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Set the geometry of the window to fill the entire screen
        self.master.geometry(f"{screen_width}x{screen_height}+0+0")

        # Background for the window
        self.master.config(background='#D8A9B3')

        self.title_label = Label(self.master, text='Aumeter', font=("Algerian", 60),
                                 padx=20, pady=20,
                                 bg='#D8A9B3')
        self.title_label.pack()


        # StringVar objects to store the username and password
        self.username_var = StringVar()
        self.password_var = StringVar()

        # Username label

        body4 = Frame(self.master, width=400, height=500, bg="#D8A9B3")
        body4.place(x=50, y=100)
        body4.destroy()
        body4 = Frame(self.master, width=400, height=500, bg="#D8A9B3")
        body4.place(x=50, y=100)


        self.username_label = Label(body4, text="Username: ", font=("Forte", 25), bg='#D8A9B3', fg='Black')
        self.username_label.place(x=5, y=100)

        # Username entry field
        self.username_entry = Entry(body4, textvariable=self.username_var, bd=2, relief='ridge')
        self.username_entry.place(x=100, y=160, width=280, height=25)
        self.username_entry.destroy()
        self.username_entry = Entry(body4, textvariable=self.username_var, bd=2, relief='ridge')
        self.username_entry.place(x=100, y=160, width=280, height=25)

        # Password label
        self.password_label = Label(body4, text='Password: ', font=("Forte", 25), bg='#D8A9B3')
        self.password_label.place(x=5, y=220, anchor='w')

        # Password entry field
        self.password_entry = Entry(body4, textvariable=self.password_var, show='*', bd=2, relief='ridge')
        self.password_entry.place(x=100, y=260, width=280, height=25)
        self.password_entry.destroy()
        self.password_entry = Entry(body4, textvariable=self.password_var, show='*', bd=2, relief='ridge')
        self.password_entry.place(x=100, y=260, width=280, height=25)

        # Another label
        additional_image = PhotoImage(file='image1.png')

        # Reduce image size
        new_width, new_height = 400, 400  # Adjust the size as needed
        additional_image = additional_image.subsample(int(additional_image.width() / new_width),
                                                      int(additional_image.height() / new_height))

        # Additional label with resized image
        self.additional_label = Label(self.master, image=additional_image, bg='#D8A9B3', relief='raised')
        self.additional_label.place(x=screen_width - new_width + 360, y=150, anchor='ne')

        # Meditation word
        self.meditation_text_label = Label(self.master, text="Inhale the future, exhale the past.",
                                           font=("Forte", 18), wraplength=300, justify=LEFT, bg='#D8A9B3')
        self.meditation_text_label.place(x=900, y=580)

        self.login_button = Button(self.master, text="Login", font=("Forte", 20), bg='white', fg='black', command=self.log_in)
        self.login_button.place(x=110, y=460, width=120)

        self.signup_button = Button(self.master, text="Sign Up", font=("Forte", 20), bg='white', fg='black', command=self.sign_up)
        self.signup_button.place(x=250, y=460, width=120)
    
    
        self.master.mainloop()
    
    def log_in(self):
        if self.saver.log_in(str(self.username_entry.get()),str(self.password_entry.get())):
            self.username_entry.delete(0, "end")
            self.password_entry.delete(0, "end")
            self.master.withdraw
            self.homepage.show_home_screen()

            
            
        
    
    def sign_up(self):
        if self.saver.sign_up(str(self.username_entry.get()),str(self.password_entry.get())):
            self.username_entry.delete(0, "end")
            self.password_entry.delete(0, "end")
            self.master.withdraw
            self.homepage.show_home_screen()


    def show_log_in_screen_from_home_page(self):
        self.homepage.master.withdraw()
        self.master.deiconify()

