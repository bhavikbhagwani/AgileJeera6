from database import Database
import requests, io, time, os
from tkinter import *
import pygame
from tkinter import messagebox

database = Database()

pygame.init()

def get_info_for_profile_page():
    user_ID = database.get_user_ID()
    if user_ID:
        user_data = database.database.child("Users").child(user_ID).get().val()
        if user_data:
            favorite_list = user_data.get('favorites')
            email = user_data.get('email')
            progress = user_data.get('progress')
        return favorite_list, email, progress
    return None, None, None

sound_urls_dictionary = {
            #meditation sessions
            1:"https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/meditation_1.mp3?alt=media&token=b22aaf93-2c27-4477-b96e-c351afdef7bc",
            2:"https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/meditation_2.mp3?alt=media&token=d081118b-413b-4b47-8dd7-d3fa418b764f",
            3:"https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/meditation_3.mp3?alt=media&token=333dc583-5381-41ce-91ff-28ba7b861b1a",
            4:"",
            5:"",
            6:"",
            7:"",
            8:"",
            #study music
            9: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/Weekend.mp3?alt=media&token=ea4bafbb-edc3-460f-84b2-c69ae08da533",
            10: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/Pomodoro.mp3?alt=media&token=88242fdb-2079-474d-8926-47ca23a0d021",
            11: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/Ondas%20Binaurais%20Aumentar.mp3?alt=media&token=55209620-5dde-4293-bddc-cdfd0237bf2d",
            12: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/brown%20noise.mp3?alt=media&token=dd051385-4f9a-43ac-bd29-f018f4665dfe",
            13: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/Calming%20handpan.mp3?alt=media&token=e7062ea9-6a47-4b44-939a-7d8f10f81016",
            14: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/romanticizing%20studying%20playlist.mp3?alt=media&token=1dd924bb-b3d9-4b0f-895f-4f20e53d2d9f",
            15: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/%5BCOPYRIGHT%20FREE%5D%201H%20Study%20Music%20%26%20Ambience%20(Oppenheimer%20Style)%20-%20Jeremy%20Brauns%20Music%20%23oppenheimer.mp3?alt=media&token=d70180ed-4beb-45ba-af49-7a587f7990ab",
            16: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/This%20Playlist%20Will%20Make%20Studying%20Physics%20Seem%20Cool.mp3?alt=media&token=a41eb92c-5319-480b-ae0a-d18ea8139181"
        }


def save_everything_for_user():
    global start_time
    global progress
    end_time = time.time()
    elapsed_time = end_time - start_time
    progress = progress + elapsed_time

    user_info = {"email": database.get_user_email(), "medi_sessions":[1,2,3,4,5,6,7,8], "music_sessions" : [9,10,11,12,13,14,15,16], "favorites":favorites_list, "progress":progress}
    user_ID = database.get_user_ID()

    database.database.child("Users").child(user_ID).set(user_info)

def on_closing():
    # Add any cleanup or confirmation code here
    # For example, you can ask the user for confirmation before closing
    if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
        ### functionality for saving everything
        save_everything_for_user()
        ### functionality to stop music if playing
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        home_page_root.destroy()
        os.system("taskkill /F /T /PID {}".format(os.getpid()))

def play_sound(number):
    sound_url = sound_urls_dictionary.get(number)
    response = requests.get(sound_url)
    sound_file = io.BytesIO(response.content)
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()


def stop_sound():
     pygame.mixer.music.stop()


def log_in():
    global start_time
    global meditation_sessions_list
    global music_list 
    global favorites_list
    global progress
    success, user_ID = database.log_in(str(username_entry.get()),str(password_entry.get()))
    if success:
       
        username_entry.delete(0, "end")
        password_entry.delete(0, "end")
        login_page_root.withdraw()
        meditation_sessions_list = database.get_meditation_list_for_this_user(user_ID)
        music_list = database.get_study_music_list_for_this_user(user_ID)
        favorites_list = database.get_favorites_list_for_this_user(user_ID)
        progress = database.get_progress(user_ID)
        home_page_root.deiconify()
        update_meditation_display()
        update_music_display()

        start_time = time.time()

def sign_up():
    global start_time
    global meditation_sessions_list
    global music_list 
    global favorites_list
    global progress
    success, user_ID = database.sign_up(str(username_entry.get()), str(password_entry.get()))
    if success:
        username_entry.delete(0, "end")
        password_entry.delete(0, "end")

        database.add_user(user_ID)

        login_page_root.withdraw()
        meditation_sessions_list = database.get_meditation_list_for_this_user(user_ID)
        music_list = database.get_study_music_list_for_this_user(user_ID)
        favorites_list = database.get_favorites_list_for_this_user(user_ID)
        progress = database.get_progress(user_ID)
        home_page_root.deiconify()
        update_meditation_display()
        update_music_display()

        start_time = time.time()
            
def show_log_in_screen_from_home_page():
     if messagebox.askokcancel("Log Out", "Are you sure you want to log out?"):
        save_everything_for_user()
        ### functionality for saving everything
        home_page_root.withdraw()
        login_page_root.deiconify()

def display_drop_down_menu(event):
        menu = Menu(home_page_root, tearoff=0)
        menu.add_command(label="View Profile", command=show_profile_page_from_home_page)
        menu.add_separator()
        menu.add_command(label="View Home Page", command="")
        menu.add_separator()
        menu.add_command(label="View Favorites", command=show_favorites_page_from_home_page)
        menu.add_separator()
        menu.add_command(label="Logout", command=show_log_in_screen_from_home_page)
        menu.post(event.x_root, event.y_root)
    
def update_meditation_display():
        for widget in meditation_body.winfo_children():
            widget.destroy()
            

        # Set the number of rows and columns for the grid layout
        num_rows = 4
        num_columns = 2

        # Initialize row and column counters
        row = 0
        column = 0
        for session_num in meditation_sessions_list:
            session_frame = Frame(meditation_body, width=120, height=80, bg="lightgrey", padx=10, pady=10)
            session_frame.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")  # Add sticky option to stretch the frame

            # Label for the session
            session_label = Label(session_frame, text=f"Meditation Session {session_num}", font=("Arial", 12), bg="lightgrey")
            session_label.pack(fill="both", expand=True)  # Fill the entire space of the frame

            # Buttons for Play and Pause
            button_frame = Frame(session_frame, bg="lightgrey")
            button_frame.pack(fill="both", expand=True)

            # Buttons for Play and Pause
            play_button = Button(button_frame, text="  ▶️", width=8, command=lambda num = session_num: play_sound(num))
            play_button.pack(side="left", padx=(0, 5))

            pause_button = Button(button_frame, text="⏹️", width=8, command=lambda num = session_num: stop_sound())
            pause_button.pack(side="right", padx=(0, 5))

            
            add_to_favorites_button = Button(session_frame, text="Add to Favorites", height=1, width=15, command=lambda num = session_num: add_to_favorites(num))
            add_to_favorites_button.pack(fill="both", expand=True, pady=(5,0))

            # Increment row and column
            row += 1
            if row == num_rows:
                row = 0
                column += 1

def update_music_display():
        for widget in music_body.winfo_children():
            widget.destroy()
            

        # Set the number of rows and columns for the grid layout
        num_rows = 4
        num_columns = 2

        # Initialize row and column counters
        row = 0
        column = 0
        for session_num in music_list:
            session_frame = Frame(music_body, width=120, height=80, bg="lightgrey", padx=10, pady=10)
            session_frame.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")  # Add sticky option to stretch the frame

            # Label for the session
            session_label = Label(session_frame, text=f"Study Music {session_num}", font=("Arial", 12), bg="lightgrey")
            session_label.pack(fill="both", expand=True)  # Fill the entire space of the frame

            # Buttons for Play and Pause
            button_frame = Frame(session_frame, bg="lightgrey")
            button_frame.pack(fill="both", expand=True)

            # Buttons for Play and Pause
            play_button = Button(button_frame, text="  ▶️", width=8, command=lambda num = session_num: play_sound(num))
            play_button.pack(side="left", padx=(0, 5))

            pause_button = Button(button_frame, text="⏹️", width=8, command=lambda num = session_num: stop_sound())
            pause_button.pack(side="right", padx=(0, 5))

            
            add_to_favorites_button = Button(session_frame, text="Add to Favorites", height=1, width=15, command=lambda num = session_num: add_to_favorites(num))
            add_to_favorites_button.pack(fill="both", expand=True, pady=(5,0))

            # Increment row and column
            row += 1
            if row == num_rows: 
                row = 0
                column += 1



def update_favorites_display():
    
    if len(favorites_list) == 0:
        text = Label(favorites_body, text="No Favorites Yet", font=("Arial", 16, "bold"))
        text.pack(expand=True)
    else:
        for widget in favorites_body.winfo_children():
            widget.destroy()
        

        # Set the number of rows and columns for the grid layout
        num_rows = 3
        num_columns = 5

        # Initialize row and column counters
        row = 0
        column = 0
        for session_num in favorites_list:
            session_frame = Frame(favorites_body, width=120, height=80, bg="lightgrey", padx=10, pady=10)
            session_frame.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")  # Add sticky option to stretch the frame

            if session_num in meditation_sessions_list:
                # Label for the session
                session_label = Label(session_frame, text=f"Meditation Session {session_num}", font=("Arial", 12), bg="lightgrey")
                session_label.pack(fill="both", expand=True)  # Fill the entire space of the frame
            else:
                 # Label for the session
                session_label = Label(session_frame, text=f"Study Music {session_num}", font=("Arial", 12), bg="lightgrey")
                session_label.pack(fill="both", expand=True)  # Fill the entire space of the frame

            # Buttons for Play and Pause
            button_frame = Frame(session_frame, bg="lightgrey")
            button_frame.pack(fill="both", expand=True)

            # Buttons for Play and Pause
            play_button = Button(button_frame, text="  ▶️", width=8, command=lambda num = session_num: play_sound(num))
            play_button.pack(side="left", padx=(0, 5))

            pause_button = Button(button_frame, text="⏹️", width=8, command=lambda num = session_num: stop_sound())
            pause_button.pack(side="right", padx=(0, 5))

            add_to_favorites_button = Button(session_frame, text="Remove from Favorites", height=1, width=15, command=lambda num = session_num: remove_from_favorites(num))
            add_to_favorites_button.pack(fill="both", expand=True, pady=(5,0))

            # Increment row and column
            column += 1
            if column == num_columns:
                column = 0
                row += 1


def show_favorites_page_from_home_page():
     home_page_root.withdraw()
     favorites_page_root.deiconify()
     update_favorites_display()

def show_home_page_from_favorites_page():
     favorites_page_root.withdraw()
     home_page_root.deiconify()

def show_home_page_from_profile_page():
    profile_page_root.withdraw()
    home_page_root.deiconify()


def add_to_favorites(number):
        if number not in favorites_list:
            favorites_list.append(number)  
            update_favorites_display()

            if number in meditation_sessions_list:
                message_to_display = f"Added Meditation Session {number} to Favorites"
            else:
                message_to_display = f"Added Study Music {number} to Favorites"

            messagebox.showinfo("Success",message_to_display)


def remove_from_favorites(number):
    favorites_list.remove(number)
    update_favorites_display()

    if number in meditation_sessions_list:
        message_to_display = f"Removed Meditation Session {number} from Favorites"
    else:
        message_to_display = f"Removed Study Music {number} from Favorites"

    messagebox.showinfo("Success",message_to_display)

def update_profile_page():

    favorite_list, email, progress = get_info_for_profile_page()
    if favorite_list is None:
        bullet_points = '* no favorites yet'
    else:
        bullet_points = '\n'.join([f'* {item}' for item in favorite_list])
    formatted_time = "{:.2f}".format(float(progress))
    

    #Frame 
    Frame_Text = Frame(profile_page_root, width=500, height=560, bg='#C0C0C0', highlightthickness=2, highlightbackground="white")
    Frame_Text.place(x=50, y=105)

    #Email inside the frame 
    Text_label = Label( Frame_Text ,text="Email: ", font=("Georgia", 20, 'bold'), bg='#C0C0C0', fg='Black')
    Text_label.place(x= 5, y = 20)
    Text_label_1 = Label( Frame_Text ,text=f"* {email}", font=("Georgia", 18, 'bold'), bg='#C0C0C0', fg='Black')
    Text_label_1.place(x= 5, y = 75)

    #Favorite inside the text frame
    Text_label_2 = Label( Frame_Text ,text="Favorites: ", font=("Georgia", 20, 'bold'), bg='#C0C0C0', fg='Black')
    Text_label_2.place(x= 5, y = 140)
    Text_label_3 = Label( Frame_Text ,text=bullet_points, font=("Georgia", 20, 'bold'), bg='#C0C0C0', fg='Black')
    Text_label_3.place(x= 5, y = 200)

    #Progress inside the text frame 

    Text_label_4 = Label( Frame_Text ,text="Time in App: ", 
                        font=("Georgia", 20, 'bold'), 
                        bg='#C0C0C0', fg='Black')
    Text_label_4.place(x= 5, y = 410)
    Text_label_5 = Label( Frame_Text ,text=f"   {formatted_time}", font=("Georgia", 20, 'bold'), bg='#C0C0C0', fg='Black')
    Text_label_5.place(x= 5, y = 450)

    

    back_home_button = Button(profile_page_root,text="Back to Home", width=20, height=3, bg="lightgrey", font=("Arial", 13, "bold"), command=show_home_page_from_profile_page)
    back_home_button.place(x=((screen_width - back_home_button.winfo_reqwidth() )// 2),y=625)



def show_profile_page_from_home_page():
    home_page_root.withdraw()
    update_profile_page()
    profile_page_root.deiconify()
    

#LOG IN PAGE

login_page_root = Tk()
login_page_root.title("Aumeter")


screen_width = login_page_root.winfo_screenwidth()
screen_height = login_page_root.winfo_screenheight()

login_page_root.geometry(f"{screen_width}x{screen_height}+0+0")

login_page_root.config(background='#D8A9B3')

title_label = Label(login_page_root, text='Aumeter', font=("Algerian", 60),
                            padx=20, pady=20,
                            bg='#D8A9B3')

title_label.pack()



login_body = Frame(login_page_root, width=400, height=500, bg="#D8A9B3", highlightthickness=2, highlightbackground="white")
login_body.place(x=50, y=100)
login_body.destroy()
login_body = Frame(login_page_root, width=400, height=500, bg="#D8A9B3", highlightthickness=2, highlightbackground="white")
login_body.place(x=50, y=100)


username_label = Label(login_body, text="Email: ", font=("Forte", 25), bg='#D8A9B3', fg='Black')
username_label.place(x=5, y=100)

username_entry = Entry(login_body, bd=2, relief='ridge')
username_entry.place(x=100, y=160, width=280, height=25)
username_entry.destroy()
username_entry = Entry(login_body, bd=2, relief='ridge')
username_entry.place(x=100, y=160, width=280, height=25)

password_label = Label(login_body, text='Password: ', font=("Forte", 25), bg='#D8A9B3')
password_label.place(x=5, y=220, anchor='w')

password_entry = Entry(login_body, show='*', bd=2, relief='ridge')
password_entry.place(x=100, y=260, width=280, height=25)
password_entry.destroy()
password_entry = Entry(login_body, show='*', bd=2, relief='ridge')
password_entry.place(x=100, y=260, width=280, height=25)

login_photo = PhotoImage(file='image1.png')

new_width, new_height = 400, 400
additional_image_log_in = login_photo.subsample(int(login_photo.width() / new_width),
                                                int(login_photo.height() / new_height))

additional_label = Label(login_page_root, image=additional_image_log_in, bg='#D8A9B3', relief='raised')
additional_label.place(x=screen_width - new_width + 360, y=150, anchor='ne')

meditation_text_label = Label(login_page_root, text="What you think, you become. \n - Buddha",
                                    font=("Forte", 18), wraplength=300, justify=LEFT, bg='#D8A9B3')
meditation_text_label.place(x=900, y=580)

login_button = Button(login_page_root, text="Login", font=("Forte", 20), bg='white', fg='black', command = log_in)
login_button.place(x=110, y=460, width=120)

signup_button = Button(login_page_root, text="Sign Up", font=("Forte", 20), bg='white', fg='black', command = sign_up)
signup_button.place(x=250, y=460, width=120)



# HOME PAGE

global meditation_sessions_list
global music_list 
global favorites_list

meditation_sessions_list = []
music_list = []


home_page_root = Toplevel()

home_page_root.protocol("WM_DELETE_WINDOW", on_closing)

home_page_root.title("Home Screen Window")
home_page_root.configure(bg="lightblue")
home_page_root.withdraw()  # Hide the second window initially


heart_image = PhotoImage(file="heart3.png")





screen_width = home_page_root.winfo_screenwidth()
screen_height = home_page_root.winfo_screenheight()

home_page_root.geometry(f"{screen_width}x{screen_height}")

home_page_header = Label(home_page_root, text="Aumeter", fg="black", bg = "lightblue", width=25, height=2, font=("Algerian", 50))
home_page_header.place(x=((screen_width - home_page_header.winfo_reqwidth() )// 2),y=10)

profile_icon = Canvas(home_page_root, width=100, height=100, bg="lightblue", highlightthickness=0)
profile_icon.place(x=40, y=70)

# Draw a circle on the canvas
profile_icon.create_oval(10, 10, 90, 90, fill="white", outline="black", width=2)
profile_icon.create_text(50, 50, text="My Profile", font=("Arial", 12, "bold"))

profile_icon.bind("<Button-1>", display_drop_down_menu)


meditation_body = Frame(home_page_root, width=400, height=300, bg="white", highlightthickness=2, highlightcolor="black")
meditation_body.place(x=100, y=200)


fav_button = Button(home_page_root,text="View My Favorites", width=20, height=3, bg="lightgrey", font=("Arial", 13, "bold"), command=show_favorites_page_from_home_page)
fav_button.place(x=((screen_width - fav_button.winfo_reqwidth() )// 2),y=300)

music_body = Frame(home_page_root, width=400, height=300, bg="white", highlightthickness=2, highlightcolor="black")
music_body.place(x=1000, y=200)


# FAVORITES PAGE
favorites_page_root = Toplevel()

favorites_page_root.protocol("WM_DELETE_WINDOW", on_closing)


favorites_page_root.title("Favorites Window")
favorites_page_root.configure(bg="lightblue")
favorites_page_root.withdraw()  # Hide the second window initially
favorites_list = []


screen_width = favorites_page_root.winfo_screenwidth()
screen_height = favorites_page_root.winfo_screenheight()

favorites_page_root.geometry(f"{screen_width}x{screen_height}")

header = Label(favorites_page_root, text="My Favorites", fg="black", bg = "lightgrey", width=100, height=5, font=("Arial", 16))
header.pack(side="top", padx=10, pady=50)

favorites_body = Frame(favorites_page_root, width=700, height=500, bg="white", highlightthickness=2, highlightcolor="black")
favorites_body.place(x=250, y=200)




back_home_button = Button(favorites_page_root,text="Back to Home", width=20, height=3, bg="lightgrey", font=("Arial", 13, "bold"), command=show_home_page_from_favorites_page)
back_home_button.place(x=((screen_width - back_home_button.winfo_reqwidth() )// 2),y=625)


## PROFILE PAGE

profile_page_root = Toplevel()
profile_page_root.protocol("WM_DELETE_WINDOW", on_closing)
profile_page_root.title("Profile Window")
profile_page_root.configure(bg="#808080")
profile_page_root.withdraw()  # Hide the second window initially



screen_width = profile_page_root.winfo_screenwidth()
screen_height = profile_page_root.winfo_screenheight()

profile_page_root.geometry(f"{screen_width}x{screen_height}")

# Set window title
title_label = Label(profile_page_root, text='My Profile', font=("Georgia", 25, 'bold'),
                    bg='#808080',
                    padx=20, pady=20)
title_label.place(x = 150 , y = 20)

# Load image
image_2 = PhotoImage(file='image2.png')

# Define new width and height for the image
new_width, new_height = 60,60  # Adjust the size as needed

# Resize the image
image_2_resized = image_2.subsample(int(image_2.width() / new_width),
                                                    int(image_2.height() / new_height))

# Create label with resized image
additional_label = Label(profile_page_root, image=image_2_resized, bg='#D8A9B3', relief='raised')
additional_label.place(x=140, y=25, anchor='ne')


#image 3
image_3 = PhotoImage(file='image3.png')

new_width2, new_height2 = 800 , 800 
image3_resized = image_3.subsample(int(image_3.width() / new_width),
                                                    int(image_3.height() / new_height))
Label_image_3 = Label(profile_page_root, image=image_3, border= 2 ,bg='#C0C0C0', relief='raised')
Label_image_3.place(x=1200, y=180, anchor='ne')

login_page_root.mainloop()