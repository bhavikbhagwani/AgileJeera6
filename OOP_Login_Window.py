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

    def create_widgets(self):
        self.title_label = Label(self.root, text='Aumeter', font=("Algerian", 60),
                            padx=20, pady=20, bg='#D8A9B3')
        self.title_label.pack()

        self.login_body = Frame(self.root, width=400, height=500, bg="#D8A9B3", highlightthickness=2, highlightbackground="white")
        self.login_body.place(x=50, y=100)

        self.username_label = Label(self.login_body, text="Email: ", font=("Forte", 25), bg='#D8A9B3', fg='Black')
        self.username_label.place(x=5, y=100)

        self.username_entry = Entry(self.login_body, bd=2, relief='ridge')
        self.username_entry.place(x=100, y=160, width=280, height=25)

        self.password_label = Label(self.login_body, text='Password: ', font=("Forte", 25), bg='#D8A9B3')
        self.password_label.place(x=5, y=220, anchor='w')
        
        self.password_entry = Entry(self.login_body, show='*', bd=2, relief='ridge')
        self.password_entry.place(x=100, y=260, width=280, height=25)

        self.login_button = Button(self.root, text="Login", font=("Forte", 20), bg='white', fg='black', command=self.log_in)
        self.login_button.place(x=110, y=460, width=120)

        self.signup_button = Button(self.root, text="Sign Up", font=("Forte", 20), bg='white', fg='black', command=self.sign_up)
        self.signup_button.place(x=250, y=460, width=120)
   
