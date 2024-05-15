import tkinter as tk
from tkinter import *
import time
from tkinter import messagebox
from database import Database
import pygame, requests, io, os

pygame.init()


class Sounds:
    def __init__(self):
        #dictionary to store meditation and music mp3 files in FireBase Storage
        self.sound_urls_dictionary = {
            #meditation sessions
            1: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/meditation_1.mp3?alt=media&token=b22aaf93-2c27-4477-b96e-c351afdef7bc",
            2: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/meditation_2.mp3?alt=media&token=d081118b-413b-4b47-8dd7-d3fa418b764f",
            3: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/meditation_3.mp3?alt=media&token=333dc583-5381-41ce-91ff-28ba7b861b1a",
            4: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/meditation_4.mp3?alt=media&token=fb176afb-a3f8-4330-9221-ba30d7da78ca",
            5: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/meditation_5.mp3?alt=media&token=bf410850-bb0b-4a7c-9b78-c6959872cdb4",
            6: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/meditation_6.mp3?alt=media&token=abe1079b-8243-4cb1-ab8b-d11a2f3751cd",
            7: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/meditation_7.mp3?alt=media&token=786153cf-a5e2-4e38-8a65-afd166e69acc",
            8: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/meditation_8.mp3?alt=media&token=7485918d-8594-4c79-adae-51a9de3a6d8b",
            #study music
            9: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/weekend.mp3?alt=media&token=9adf4712-b512-4d1c-ad89-5bde52ce6fbb",
            10: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/pomodoro.mp3?alt=media&token=cb53c613-beca-4f18-9a16-87f3fdcdef81",
            11: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/binary%20waves.mp3?alt=media&token=ddd36ecd-e28a-4770-b711-6fec19e369b7",
            12: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/brown-noise.mp3?alt=media&token=459d74e9-fbf7-4e4a-ad20-8907c6229008",
            13: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/slow%20jazz.mp3?alt=media&token=b93d625c-dfa3-4974-8d10-a09cc6a6c238",
            14: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/romanticizing.mp3?alt=media&token=154e46db-5edf-4a27-9ced-f97eb521ed2c",
            15: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/oppenheimer.mp3?alt=media&token=1793f3c4-deef-4cb9-bb74-71de8ef30ecb",
            16: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/physics%20music.mp3?alt=media&token=bbcf1a23-b509-4a8e-a3b0-e28f4ae76a55"
        }

        self.sound_to_name_dictionary = {
            1: "Breathing",
            2: "Mindfulness",
            3: "Focus",
            4: "Walking",
            5: "Mantra - AUM",
            6: "Body Scan",
            7: "Fire",
            8: "Mirror Glazing",
            9: "TheWeeknd",
            10: "Pomodoro",
            11: "Binary Waves",
            12: "Brown Noise",
            13: "Slow Jazz",
            14: "Romantic",
            15: "Oppenheimer",
            16: "Physics"
        }
    
    def get_sound_url(self, number):
        return self.sound_urls_dictionary.get(number)
    
    def get_sound_name(self, number):
        name_of_sound = self.sound_to_name_dictionary.get(number)
        return name_of_sound

    def play_sound(self, number):
        try:
            sound_url = self.get_sound_url(number)
            response = requests.get(sound_url)
            sound_file = io.BytesIO(response.content)
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
        except Exception as e:
            print("An error occured while loading or playing the sound: ", e)


    def stop_sound(self):
        try:
            pygame.mixer.music.stop()
        except Exception as e:
            print("An error occured while stopping / pausing the sound: ", e)

class BasePage(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

class Page1(BasePage):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(bg="#D8A9B3")
        screen_width = self.winfo_screenwidth()
        self.database = Database()
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)


        self.title_label = tk.Label(self, text='Aumeter', font=("Algerian", 60),
                            padx=20, pady=20,
                            bg='#D8A9B3')
        self.title_label.pack()

        self.login_body = tk.Frame(self, width=400, height=500, bg="#D8A9B3", highlightthickness=2, highlightbackground="white")
        self.login_body.place(x=50, y=100)
        self.login_body.destroy()
        self.login_body = tk.Frame(self, width=400, height=500, bg="#D8A9B3", highlightthickness=2, highlightbackground="white")
        self.login_body.place(x=50, y=100)

        self.username_label = tk.Label(self.login_body, text="Email: ", font=("Forte", 25), bg='#D8A9B3', fg='Black')
        self.username_label.place(x=5, y=100)

        self.username_entry = tk.Entry(self.login_body, bd=2, relief='ridge')
        self.username_entry.place(x=100, y=160, width=280, height=25)
        self.username_entry.destroy()
        self.username_entry = tk.Entry(self.login_body, bd=2, relief='ridge')
        self.username_entry.place(x=100, y=160, width=280, height=25)

        self.password_label = tk.Label(self.login_body, text='Password: ', font=("Forte", 25), bg='#D8A9B3')
        self.password_label.place(x=5, y=220, anchor='w')

        self.password_entry = tk.Entry(self.login_body, show='*', bd=2, relief='ridge')
        self.password_entry.place(x=100, y=260, width=280, height=25)
        self.password_entry.destroy()
        self.password_entry = tk.Entry(self.login_body, show='*', bd=2, relief='ridge')
        self.password_entry.place(x=100, y=260, width=280, height=25)

        self.login_photo = tk.PhotoImage(file='image1.png')

        self.new_width, self.new_height = 400, 400
        self.additional_image_log_in = self.login_photo.subsample(int(self.login_photo.width() / self.new_width),
                                                        int(self.login_photo.height() / self.new_height))

        self.additional_label = tk.Label(self, image=self.additional_image_log_in, bg='#D8A9B3', relief='raised')
        self.additional_label.place(x=screen_width - self.new_width + 360, y=150, anchor='ne')

        self.meditation_text_label = tk.Label(self, text="What you think, you become. \n - Buddha",
                                            font=("Forte", 18), wraplength=300, justify=LEFT, bg='#D8A9B3')
        self.meditation_text_label.place(x=900, y=580)

        self.login_button = tk.Button(self, text="Login", font=("Forte", 20), bg='white', fg='black', command = self.log_in)
        self.login_button.place(x=110, y=460, width=120)

        self.signup_button = tk.Button(self, text="Sign Up", font=("Forte", 20), bg='white', fg='black', command = self.sign_up)
        self.signup_button.place(x=250, y=460, width=120)



    def log_in(self):
        """Method For User Loggin in the App."""
        global user_ID
        global email
        global start_time
        global meditation_sessions_list
        global music_list 
        global favorites_list
        global progress
        success, user_ID = self.database.log_in(str(self.username_entry.get()),str(self.password_entry.get()))
        if success:
            self.username_entry.delete(0, "end")
            self.password_entry.delete(0, "end")
            messagebox.showinfo("Success", "Log In Successful, you will be directed to the home page")
            email = self.database.get_user_email()
            meditation_sessions_list = self.database.get_meditation_list_for_this_user(user_ID)
            music_list = self.database.get_study_music_list_for_this_user(user_ID)
            favorites_list = self.database.get_favorites_list_for_this_user(user_ID)
            print("favorites retrieved when logged in: ", favorites_list)
            progress = self.database.get_progress(user_ID)
            print("progress retrieved when logged in: ", progress)
            print("user_ID retrieved when logged in after success: ", user_ID)
            self.go_to_page2()

            start_time = time.time()
        else:
            messagebox.showerror("Error", "Log in not successful, wrong email or password")


    def sign_up(self):
        """Method for User Signing up (creating new account) in the App."""
        global user_ID
        global email
        global start_time
        global meditation_sessions_list
        global music_list 
        global favorites_list
        global progress
        success, user_ID = self.database.sign_up(str(self.username_entry.get()), str(self.password_entry.get()))
        if success:
            self.username_entry.delete(0, "end")
            self.password_entry.delete(0, "end")
            
            self.database.add_user(user_ID)
            messagebox.showinfo("Success","Sign Up Successful, you will be directed to the home page")
            email = self.database.get_user_email()
            meditation_sessions_list = self.database.get_meditation_list_for_this_user(user_ID)
            music_list = self.database.get_study_music_list_for_this_user(user_ID)
            favorites_list = self.database.get_favorites_list_for_this_user(user_ID)
            progress = self.database.get_progress(user_ID)
            self.go_to_page2()

            start_time = time.time()
        else:
            messagebox.showerror("Error", "Sign up not successful, wrong email or password")

    def go_to_page2(self):
        self.master.show_page(Page2)

    def on_closing(self):
        """Method when user wants to exit."""
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()

            self.destroy()
            os.system("taskkill /F /T /PID {}".format(os.getpid()))


class Page2(BasePage):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
    
        self.configure(bg="lightgrey")
        self.screen_width = self.winfo_screenwidth()

        self.button = tk.Button(self, text="Go to Page 1", command=self.go_to_page1)
        self.button.pack(pady=10)

        global meditation_sessions_list
        global music_list
        global favorites_list

        self.sounds = Sounds()
        self.database = Database()

        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.configure(bg="#BED7DC")

        heart_image = PhotoImage(file="heart3.png")

        self.home_page_header = Label(self, text="Aumeter", fg="black", bg = "#BED7DC", width=25, height=2, font=("Algerian", 50))
        self.home_page_header.place(x=((self.screen_width - self.home_page_header.winfo_reqwidth() )// 2),y=10)

        # Load image
        self.image_4 = PhotoImage(file='image2.png')

        # Define new width and height for the image
        self.new_width, self.new_height = 90,90  # Adjust the size as needed

        # Resize the image
        self.image_4_resized = self.image_4.subsample(int(self.image_4.width() / self.new_width),
                                                            int(self.image_4.height() / self.new_height))

        # Create label with resized image
        self.additional_label_4 = Label(self, image=self.image_4_resized, bg='#D8A9B3', relief='raised')
        self.additional_label_4.place(x=140, y=50, anchor='ne')

        self.additional_label_4.bind("<Button-1>", self.display_drop_down_menu)

        self.meditation_body = Frame(self, width=400, height=300, bg="#B3C8CF", highlightthickness=2, highlightcolor="black")
        self.meditation_body.place(x=100, y=200)

        self.fav_button = Button(self,text="View My Favorites", width=20, height=3, bg="lightgrey", font=("Arial", 13, "bold"), command=self.go_to_page3)
        self.fav_button.place(x=((self.screen_width - self.fav_button.winfo_reqwidth() )// 2),y=300)

        self.profile_button = Button(self,text="View My Profile", width=20, height=3, bg="lightgrey", font=("Arial", 13, "bold"), command=self.go_to_page4)
        self.profile_button.place(x=((self.screen_width - self.fav_button.winfo_reqwidth() )// 2),y=400)

        self.about_button = Button(self,text="View About Us", width=20, height=3, bg="lightgrey", font=("Arial", 13, "bold"), command=self.go_to_page5)
        self.about_button.place(x=((self.screen_width - self.fav_button.winfo_reqwidth() )// 2),y=500)

        self.music_body = Frame(self, width=400, height=300, bg="#B3C8CF", highlightthickness=2, highlightcolor="black")
        self.music_body.place(x=1000, y=200)

        self.update_meditation_display()
        self.update_music_display()

    def display_drop_down_menu(self, event):
        """Method to display Drop Down Menu for User."""
        menu = Menu(self, tearoff=0)
        menu.add_command(label="View Profile", command=self.go_to_page4)
        menu.add_separator()
        menu.add_command(label="View Favorites", command=self.go_to_page3)
        menu.add_separator()
        menu.add_command(label="About us", command=self.go_to_page5)
        menu.add_separator()
        menu.add_command(label="Logout", command=self.go_to_page1)
        menu.post(event.x_root, event.y_root)

    def update_meditation_display(self):
        """Method to Update Meditation Frame."""
        for widget in self.meditation_body.winfo_children():
            widget.destroy()

        # Setting the number of rows and columns for the grid layout
        num_rows = 4
        num_columns = 2

        # Initializing row and column counters
        row = 0
        column = 0
        for session_num in meditation_sessions_list:
            session_frame = Frame(self.meditation_body, width=120, height=80, bg="#B3C8CF", padx=10, pady=10, highlightbackground="black", highlightthickness=1, highlightcolor="black")
            session_frame.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")  # Add sticky option to stretch the frame

            name = self.sounds.get_sound_name(session_num)

            # Label for the session
            session_label = Label(session_frame, text=name, font=("Arial", 12), bg="#B3C8CF")
            session_label.pack(fill="both", expand=True)  # Fill the entire space of the frame

            # Buttons for Play and Pause
            button_frame = Frame(session_frame, bg="#B3C8CF")
            button_frame.pack(fill="both", expand=True)

            # Buttons for Play and Pause
            play_button = Button(button_frame, text="  ▶️", width=8, command=lambda num = session_num: self.sounds.play_sound(num))
            play_button.pack(side="left", padx=(0, 5))

            pause_button = Button(button_frame, text="⏹️", width=8, command=lambda num = session_num: self.sounds.stop_sound())
            pause_button.pack(side="right", padx=(0, 5))


            add_to_favorites_button = Button(session_frame, text="Add to Favorites", height=1, width=15, command=lambda num = session_num: self.add_to_favorites(num))
            add_to_favorites_button.pack(fill="both", expand=True, pady=(5,0))

            # Increment row and column
            row += 1
            if row == num_rows:
                row = 0
                column += 1


    def update_music_display(self):
            """Method to Update Music Frame Display."""
            for widget in self.music_body.winfo_children():
                widget.destroy()

            # Setting the number of rows and columns for the grid layout
            num_rows = 4
            num_columns = 2

            # Initializing row and column counters
            row = 0
            column = 0
            for session_num in music_list:
                session_frame = Frame(self.music_body, width=120, height=80, bg="#B3C8CF", padx=10, pady=10, highlightbackground="black", highlightthickness=1, highlightcolor="black")
                session_frame.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")  # Add sticky option to stretch the frame

                name = self.sounds.get_sound_name(session_num)

                # Label for the session
                session_label = Label(session_frame, text=name, font=("Arial", 12), bg="#B3C8CF")
                session_label.pack(fill="both", expand=True)  # Fill the entire space of the frame

                # Buttons for Play and Pause
                button_frame = Frame(session_frame, bg="#B3C8CF")
                button_frame.pack(fill="both", expand=True)

                # Buttons for Play and Pause
                play_button = Button(button_frame, text="  ▶️", width=8, command=lambda num = session_num: self.sounds.play_sound(num))
                play_button.pack(side="left", padx=(0, 5))

                pause_button = Button(button_frame, text="⏹️", width=8, command=lambda num = session_num: self.sounds.stop_sound())
                pause_button.pack(side="right", padx=(0, 5))

                add_to_favorites_button = Button(session_frame, text="Add to Favorites", height=1, width=15, command=lambda num = session_num: self.add_to_favorites(num))
                add_to_favorites_button.pack(fill="both", expand=True, pady=(5, 0))

                # Increment row and column
                row += 1
                if row == num_rows: 
                    row = 0
                    column += 1

    def add_to_favorites(self, number):
        if number not in favorites_list:
            favorites_list.append(number)

            name = self.sounds.get_sound_name(number)

            message_to_display = f"Added {name} to Favorites"

            messagebox.showinfo("Success",message_to_display)
    
    def save_everything_for_user(self):
        """Method to Save User's Contents/Progress into Database"""
        global user_ID
        global email
        global start_time
        global progress

        # Stop time progress and calculate elapsed time
        end_time = time.time()
        elapsed_time = end_time - start_time
        progress = progress + elapsed_time

        self.database.save_user_info(user_ID, email, favorites_list, progress)

    def go_to_page1(self):
        if messagebox.askokcancel("Log Out", "Are you sure you want to log out?"):
            self.save_everything_for_user()
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()
            self.master.show_page(Page1)
    
    def go_to_page3(self):
        self.master.show_page(Page3)
    
    def go_to_page4(self):
        self.master.show_page(Page4)
    
    def go_to_page5(self):
        self.master.show_page(Page5)

    def on_closing(self):
        """Method when user wants to exit."""
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()

            try:
                self.save_everything_for_user()
            except NameError:
                print("")
            #stop music if still playing
            

            self.destroy()
            os.system("taskkill /F /T /PID {}".format(os.getpid()))

class Page3(BasePage):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
    
        self.configure(bg="lightblue")
        global favorites_list
        self.screen_width = self.winfo_screenwidth()
        self.database = Database()
        self.sounds = Sounds()

        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.favorites_page_header = Label(self, text="My Favorites", fg="black", bg = "lightblue", width=25, height=2, font=("Algerian", 50))
        self.favorites_page_header.place(x=((self.screen_width - self.favorites_page_header.winfo_reqwidth() )// 2),y=10)

        self.favorites_body = Frame(self, width=700, height=500, bg="white", highlightthickness=2, highlightcolor="black")
        self.favorites_body.place(x=250, y=200)

        self.back_home_button = Button(self,text="Back to Home", width=20, height=3, bg="lightgrey", font=("Arial", 13, "bold"), command=self.go_to_page2)
        self.back_home_button.place(x=((self.screen_width - self.back_home_button.winfo_reqwidth() )// 2),y=625)

        self.update_favorites_display()

    def update_favorites_display(self):
        """Method to Update Favorites Frame Display."""

        for widget in self.favorites_body.winfo_children():
                widget.destroy()

        if len(favorites_list) == 0:
            text = Label(self.favorites_body, text="No Favorites Yet", font=("Arial", 16, "bold"))
            text.grid(row=0, column=0, padx=10, pady=10)
        else:
            

            # Setting the number of rows and columns for the grid layout
            num_rows = 3
            num_columns = 5

            # Initializing row and column counters
            row = 0
            column = 0
            for session_num in favorites_list:
                session_frame = Frame(self.favorites_body, width=120, height=80, bg="lightgrey", padx=10, pady=10)
                session_frame.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")  # Add sticky option to stretch the frame

                name = self.sounds.get_sound_name(session_num)

                # Label for the session
                session_label = Label(session_frame, text=name, font=("Arial", 12), bg="lightgrey")
                session_label.pack(fill="both", expand=True)

                # Buttons for Play and Pause
                button_frame = Frame(session_frame, bg="lightgrey")
                button_frame.pack(fill="both", expand=True)

                # Buttons for Play and Pause
                play_button = Button(button_frame, text="  ▶️", width=8, command=lambda num = session_num: self.sounds.play_sound(num))
                play_button.pack(side="left", padx=(0, 5))

                pause_button = Button(button_frame, text="⏹️", width=8, command=lambda num = session_num: self.sounds.stop_sound())
                pause_button.pack(side="right", padx=(0, 5))

                add_to_favorites_button = Button(session_frame, text="Remove from Favorites", height=1, width=15, command=lambda num = session_num: self.remove_from_favorites(num))
                add_to_favorites_button.pack(fill="both", expand=True, pady=(5, 0))

                # Increment row and column
                column += 1
                if column == num_columns:
                    column = 0
                    row += 1

    def remove_from_favorites(self, number):
        favorites_list.remove(number)
        self.update_favorites_display()

        name = self.sounds.get_sound_name(number)

        message_to_display = f"Removed {name} from Favorites"

        messagebox.showinfo("Success",message_to_display)

    def go_to_page2(self):
        self.master.show_page(Page2)

    def save_everything_for_user(self):
        """Method to Save User's Contents/Progress into Database"""
        global user_ID
        global email
        global start_time
        global progress

        # Stop time progress and calculate elapsed time
        end_time = time.time()
        elapsed_time = end_time - start_time
        progress = progress + elapsed_time

        self.database.save_user_info(user_ID, email, favorites_list, progress)

    def on_closing(self):
        """Method when user wants to exit."""
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()

            try:
                self.save_everything_for_user()
            except NameError:
                print("")
            #stop music if still playing
            

            self.destroy()
            os.system("taskkill /F /T /PID {}".format(os.getpid()))

class Page4(BasePage):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.database = Database()
        self.configure(bg="#808080")
        self.sounds = Sounds()

        global favorites_list
        global progress

        self.screen_width = self.winfo_screenwidth()
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Set window title
        self.title_label = Label(self, text='My Profile', font=("Georgia", 25, 'bold'),
                            bg='#808080',
                            padx=20, pady=20)
        self.title_label.place(x = 150 , y = 20)

        # Load image
        self.image_2 = PhotoImage(file='image2.png')

        # Define new width and height for the image
        self.new_width, self.new_height = 60,60  # Adjust the size as needed

        # Resize the image
        self.image_2_resized = self.image_2.subsample(int(self.image_2.width() / self.new_width),
                                                            int(self.image_2.height() / self.new_height))

        # Create label with resized image
        self.additional_label = Label(self, image=self.image_2_resized, bg='#D8A9B3', relief='raised')
        self.additional_label.place(x=140, y=25, anchor='ne')


        #image 3
        self.image_3 = PhotoImage(file='image3.png')

        self.new_width2, self.new_height2 = 800 , 800 
        self.image3_resized = self.image_3.subsample(int(self.image_3.width() / self.new_width),
                                                            int(self.image_3.height() / self.new_height))
        self.Label_image_3 = Label(self, image=self.image_3, border= 2 ,bg='#C0C0C0', relief='raised')
        self.Label_image_3.place(x=1200, y=180, anchor='ne')

        self.update_profile_page()


    def update_profile_page(self):
        """Method to Update Profile Page Display."""
        global start_time
        global favorites_list
        global progress
        global email
        favorite_list_to_show =  favorites_list
        new_favorites_list_to_show = []
        print("favorite list before: ", favorite_list_to_show)

        for number in favorite_list_to_show:
            name = self.sounds.get_sound_name(number)
            new_favorites_list_to_show.append(name)
        print("new list: ",new_favorites_list_to_show)
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        progress = progress + elapsed_time

        print("elapsed time: ", elapsed_time)
        print("progress: ", progress)

        if len(favorite_list_to_show) == 0:
            bullet_points = '* no favorites yet'

        else:


            bullet_points = '\n'.join([f'* {item}' for item in new_favorites_list_to_show])

            if len(favorite_list_to_show) > 5:
                new_favorites_list_to_show = new_favorites_list_to_show[:5]
                bullet_points = '\n'.join([f'* {item}' for item in new_favorites_list_to_show])
                bullet_points += '\n      ... and more'

        progress = int(progress)
        hours = progress // 3600
        minutes = (progress % 3600) // 60
        seconds = progress % 60
        formatted_time = f"{hours} HOURS {minutes} MINUTES {seconds} SECONDS"

        #Frame 
        Frame_Text = Frame(self, width=550, height=560, bg='#C0C0C0', highlightthickness=2, highlightbackground="white")
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
        Text_label_5 = Label( Frame_Text ,text=f"{formatted_time}", font=("Georgia", 20, 'bold'), bg='#C0C0C0', fg='Black')
        Text_label_5.place(x= 5, y = 450)

        back_home_button = Button(self, text="Back to Home", width=20, height=3, bg="lightgrey", font=("Arial", 13, "bold"), command=self.go_to_page2)
        back_home_button.place(x=((self.screen_width - back_home_button.winfo_reqwidth() )// 2),y=625)

        start_time = time.time()


    def go_to_page2(self):
        self.master.show_page(Page2)

    def save_everything_for_user(self):
        """Method to Save User's Contents/Progress into Database"""
        global user_ID
        global email
        global start_time
        global progress

        # Stop time progress and calculate elapsed time
        end_time = time.time()
        elapsed_time = end_time - start_time
        progress = progress + elapsed_time

        self.database.save_user_info(user_ID, email, favorites_list, progress)

    def on_closing(self):
        """Method when user wants to exit."""
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()

            try:
                self.save_everything_for_user()
            except NameError:
                print("")
            #stop music if still playing
            

            self.destroy()
            os.system("taskkill /F /T /PID {}".format(os.getpid()))

class Page5(BasePage):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(bg="#808080")
        self.database = Database()
        self.create_window()
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)


    def create_window(self):
        # Creating the main rectangle frame
        main_frame = Frame(self, width=600, height=400, relief='solid', borderwidth=2)
        main_frame.pack(padx=20, pady=20)

        # Creating squares with images and names
        members = [
            ("Bereket", "no_profile.png"),
            ("Bhavik", "no_profile.png"),
            ("Ahmed", "no_profile.png"),
            ("Ghanasham", "no_profile.png"),
            ("Ghazal", "no_profile.png")
        ]
        for i, (name, image_file) in enumerate(members):
            square_frame = Frame(main_frame, width=100, height=100, relief='solid', borderwidth=1)
            square_frame.grid(row=0, column=i, padx=10, pady=10)
            label_image = Label(square_frame)
            label_image.grid(row=0, column=0, padx=10, pady=10)
            label_name = Label(square_frame, text=name)
            label_name.grid(row=1, column=0)

            # Load image
            img = PhotoImage(file=image_file)
            label_image.configure(image=img)
            label_image.image = img  # Keep a reference to avoid garbage collection

        # Creating the explanation text
        explanation_text = """
        Welcome to Aumeter, your ultimate destination for peace,relaxation, and mindfulness. Whether you're a seasoned 
        meditator or just beginning your journey, Aumeter offers a sanctuary where you can find serenity amidst life's chaos.

        Aumeter and its Key Features: 

        Audial Meditation Sessions:
        Immerse yourself in a realm of tranquility with our audial meditation sessions. All supported by scientific research
        and designed to guide you through moments of mindfulness, these sessions utilize soothing sounds, calming music, and
        guided narration to help you find inner peace and clarity. 

        Application Usage Tracker:

        Stay informed and motivated on your meditation journey with our application usage tracker.
        You can view youre progress with Aumeter in your profile page

        Study Music:

        Enhance your focus and productivity with our curated collection of study music. Whether you're studying for exams, working on
        a project, or seeking creative inspiration, our ambient music tracks create an optimal environment for concentration and mental clarity.

        Personalized Favorites Preferences: 
        
        Tailor your meditation experience to suit your unique preferences with our personalized favorites
        feature. Mark your favorite meditation sessions, and study music that resonates with you. 
        """
        explanation_label = tk.Label(self, text=explanation_text, wraplength=900, width = 95, justify="left", font=("Times New Roman", 12))
        explanation_label.place(x=100, y=250)

        self.back_home_button_2 = Button(self,text="Back to Home", width=20, height=3, bg="lightgrey", font=("Arial", 13, "bold"), command=self.go_to_page2)
        self.back_home_button_2.place(x=1200,y=675)

        #image 3
        self.image_5 = PhotoImage(file='image3.png')

        self.new_width2, self.new_height2 = 700 , 700 
        self.image5_resized = self.image_5.subsample(int(self.image_5.width() / self.new_width2),
                                                            int(self.image_5.height() / self.new_height2))
        self.Label_image_5 = Label(self, image=self.image_5, border= 2 ,bg='#C0C0C0', relief='raised')
        self.Label_image_5.place(x=1125, y=280)

    def save_everything_for_user(self):
        """Method to Save User's Contents/Progress into Database"""
        global user_ID
        global email
        global start_time
        global progress

        # Stop time progress and calculate elapsed time
        end_time = time.time()
        elapsed_time = end_time - start_time
        progress = progress + elapsed_time

        self.database.save_user_info(user_ID, email, favorites_list, progress)

    def on_closing(self):
        """Method when user wants to exit."""
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()

            try:
                self.save_everything_for_user()
            except NameError:
                print("")
            #stop music if still playing
            

            self.destroy()
            os.system("taskkill /F /T /PID {}".format(os.getpid()))

    def go_to_page2(self):
        self.master.show_page(Page2)


class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aumeter App")
        self.database = Database()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")
        print("height: ", screen_height)
        print("width: ",screen_width)
        self.current_page = None
        self.show_page(Page1)
        

    def show_page(self, page):
        if self.current_page:
            self.current_page.pack_forget()  # Hide current page
        self.current_page = page(self)  # Create new page
        self.current_page.pack(fill="both", expand=True)  # Show new page

    

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
