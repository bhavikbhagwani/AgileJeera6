from tkinter import *
from database import Database



class HomePage:
    def __init__(self, login_page):
        self.master = Tk()
        self.master.title("Home Screen Window")
        self.master.configure(bg="lightblue")
        self.master.withdraw()  # Hide the second window initially
        self.login_page = login_page 
    
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        
        self.master.geometry(f"{screen_width}x{screen_height}")

        header = Label(self.master, text="Aumeter", fg="black", bg = "lightgrey", width=100, height=5, font=("Arial", 16))
        header.pack(side="top", padx=10, pady=50)

        profile_icon = Canvas(self.master, width=100, height=100, bg="lightblue", highlightthickness=0)
        profile_icon.place(x=40, y=70)

        # Draw a circle on the canvas
        profile_icon.create_oval(10, 10, 90, 90, fill="white", outline="black", width=2)
        profile_icon.create_text(50, 50, text="My Profile", font=("Arial", 12, "bold"))

        profile_icon.bind("<Button-1>", self.display_drop_down_menu)

        fav_button = Button(self.master,text="View My Favorites", width=20, height=3, bg="lightgrey", font=("Arial", 13, "bold"))
        fav_button.place(x=((screen_width - fav_button.winfo_reqwidth() )// 2),y=300)

        frame_1 = Frame(self.master, width=500, height=200, bg="white", highlightthickness=2, highlightcolor="black", background="lightgrey")

        frame_2 = Frame(self.master, width=500, height=200, bg="white", highlightthickness=2, highlightcolor="black", background="lightgrey")

        frame_1.place(x=110, y=400)
        frame_1.pack_propagate(False)
        frame_2.place(x=700, y=400)
        frame_2.pack_propagate(False)


        text_1 = Label(frame_1, text="ALL Study Music down here", fg="black", bg="lightgrey", font=("Arial", 16, "bold"))
        text_1.pack(pady=10)

        button_1 = Button(frame_1, text="Study Music", width=15, height=2, command=self.open_music_player)
        button_1.pack(pady=10)

        # Text and button for frame 2
        text_2 = Label(frame_2, text="ALL Meditation Sessions down here", fg="black", bg="lightgrey", font=("Arial", 16, "bold"))
        text_2.pack(pady=10)

        button_2 = Button(frame_2, text="Meditation Sessions", width=15, height=2)
        button_2.pack(pady=10)

    
    def show_home_screen(self):
        self.master.deiconify()

    def show_log_in_screen(self):
        self.master.withdraw()
        self.login_page.master.deiconify()
        

    def display_drop_down_menu(self,event):
        menu = Menu(self.master, tearoff=0)
        menu.add_command(label="View Profile")
        menu.add_separator()
        menu.add_command(label="View Home Page", command="")
        menu.add_separator()
        menu.add_command(label="View Progress")
        menu.add_separator()
        menu.add_command(label="View Favorites", command="")
        menu.add_separator()
        menu.add_command(label="Logout", command=self.show_log_in_screen)
        menu.post(event.x_root, event.y_root)
        
    def open_music_player(self):
        self.master.withdraw()
        self.music_player.show_study_music()