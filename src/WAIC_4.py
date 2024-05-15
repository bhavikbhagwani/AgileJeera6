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
        screen_height = self.winfo_screenheight()
        self.database = Database()
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)


        self.title_label = tk.Label(self, text='Aumeter', font=("Algerian", 60),
                            padx=20, pady=20,
                            bg='#D8A9B3')
        self.title_label.pack()

        self.login_body_width = int(screen_width / 3.84)
        self.login_body_height = int(screen_height / 1.728)
        self.login_body_place_x_value = int(screen_width / 30.72)
        self.login_body_place_y_value = int(screen_height / 8.64)

        self.login_body = tk.Frame(self, width=self.login_body_width, height=self.login_body_height, bg="#D8A9B3", highlightthickness=2, highlightbackground="white")
        self.login_body.place(x=self.login_body_place_x_value, y=self.login_body_place_y_value)
        self.login_body.destroy()
        self.login_body = tk.Frame(self, width=self.login_body_width, height=self.login_body_height, bg="#D8A9B3", highlightthickness=2, highlightbackground="white")
        self.login_body.place(x=self.login_body_place_x_value, y=self.login_body_place_y_value)

        self.username_label_place_x_value = int(screen_width / 307.2)
        self.username_label_place_y_value = int(screen_height / 8.64)

        self.username_label = tk.Label(self.login_body, text="Email: ", font=("Forte", 25), bg='#D8A9B3', fg='Black')
        self.username_label.place(x=self.username_label_place_x_value, y=self.username_label_place_y_value)

        self.username_entry_place_x_value = int(screen_width / 15.36)
        self.username_entry_place_y_value = int(screen_height / 5.4)
        self.username_entry_place_width = int(screen_width / 5.48)
        self.username_entry_place_height = int(screen_height / 34.56)

        self.username_entry = tk.Entry(self.login_body, bd=2, relief='ridge')
        self.username_entry.place(x=self.username_entry_place_x_value, y=self.username_entry_place_y_value, width=self.username_entry_place_width, height=self.username_entry_place_height)
        self.username_entry.destroy()
        self.username_entry = tk.Entry(self.login_body, bd=2, relief='ridge')
        self.username_entry.place(x=self.username_entry_place_x_value, y=self.username_entry_place_y_value, width=self.username_entry_place_width, height=self.username_entry_place_height)

        self.password_label_place_x_value = int(screen_width / 307.2)
        self.password_label_place_y_value = int(screen_height / 3.927)

        self.password_label = tk.Label(self.login_body, text='Password: ', font=("Forte", 25), bg='#D8A9B3')
        self.password_label.place(x=self.password_label_place_x_value, y=self.password_label_place_y_value, anchor='w')

        self.pasword_entry_place_x_value = int(screen_width / 15.36)
        self.pasword_entry_place_y_value = int(screen_height / 3.32)
        self.pasword_entry_place_width = int(screen_width / 5.48)
        self.pasword_entry_place_height = int(screen_height / 34.56)

        self.password_entry = tk.Entry(self.login_body, show='*', bd=2, relief='ridge')
        self.password_entry.place(x=self.pasword_entry_place_x_value, y=self.pasword_entry_place_y_value, width=self.pasword_entry_place_width, height=self.pasword_entry_place_height)
        self.password_entry.destroy()
        self.password_entry = tk.Entry(self.login_body, show='*', bd=2, relief='ridge')
        self.password_entry.place(x=self.pasword_entry_place_x_value, y=self.pasword_entry_place_y_value, width=self.pasword_entry_place_width, height=self.pasword_entry_place_height)

        self.login_photo = tk.PhotoImage(file='image1.png')

        

        self.new_width, self.new_height = int(screen_width / 3.84), int(screen_height / 2.16)
        self.additional_image_log_in = self.login_photo.subsample(int(self.login_photo.width() / self.new_width),
                                                        int(self.login_photo.height() / self.new_height))

        addition_number_for_additional_label_place_x_value = int(screen_width / 4.26)
        additional_label_y_value = int(screen_height / 5.76)

        self.additional_label = tk.Label(self, image=self.additional_image_log_in, bg='#D8A9B3', relief='raised')
        self.additional_label.place(x=screen_width - self.new_width + addition_number_for_additional_label_place_x_value, y=additional_label_y_value, anchor='ne')

        meditation_text_label_wrap_length = int(screen_width / 5.12)
        meditation_text_label_place_x_value = int(screen_width / 1.706)
        meditation_text_label_place_y_value = int(screen_height / 1.49)

        self.meditation_text_label = tk.Label(self, text="What you think, you become. \n - Buddha",
                                            font=("Forte", 18), wraplength=meditation_text_label_wrap_length, justify=LEFT, bg='#D8A9B3')
        self.meditation_text_label.place(x=meditation_text_label_place_x_value, y=meditation_text_label_place_y_value)


        login_button_place_x_value = int(screen_width / 13.963)
        login_button_place_y_value = int(screen_height / 1.878)
        login_button_place_width = int(screen_width / 12.8)

        signup_button_place_x_value = int(screen_width / 6.144)
        signup_button_place_y_value = int(screen_height / 1.878)
        signup_button_place_width = int(screen_width / 12.8)
        

        self.login_button = tk.Button(self, text="Login", font=("Forte", 20), bg='white', fg='black', command = self.log_in)
        self.login_button.place(x=login_button_place_x_value, y=login_button_place_y_value, width=login_button_place_width)

        self.signup_button = tk.Button(self, text="Sign Up", font=("Forte", 20), bg='white', fg='black', command = self.sign_up)
        self.signup_button.place(x=signup_button_place_x_value, y=signup_button_place_y_value, width=signup_button_place_width)



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

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        global meditation_sessions_list
        global music_list
        global favorites_list

        self.sounds = Sounds()
        self.database = Database()

        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.configure(bg="#BED7DC")

        heart_image = PhotoImage(file="heart3.png")

        self.home_page_header_width = int(screen_width / 61.44)
        self.home_page_header_height = int(screen_height / 432)
        self.home_page_header_place_x_value = int(screen_width / 6.095)
        self.home_page_header_place_y_value = int(screen_height / 86.4)



        self.home_page_header = Label(self, text="Aumeter", fg="black", bg = "#BED7DC", width=self.home_page_header_width, height=self.home_page_header_height, font=("Algerian", 50))
        self.home_page_header.place(x=self.home_page_header_place_x_value,y=self.home_page_header_place_y_value)

        # Load image
        self.image_4 = PhotoImage(file='image2.png')

        # Define new width and height for the image

        self.new_width, self.new_height = int(screen_width / 17.06), int(screen_height / 9.6)  # Adjust the size as needed

        # Resize the image
        self.image_4_resized = self.image_4.subsample(int(self.image_4.width() / self.new_width),
                                                            int(self.image_4.height() / self.new_height))

        self.additional_label_4_place_x_value = int(screen_width / 10.97)
        self.additional_label_4_place_y_value = int(screen_height / 17.28)

        # Create label with resized image
        self.additional_label_4 = Label(self, image=self.image_4_resized, bg='#D8A9B3', relief='raised')
        self.additional_label_4.place(x=self.additional_label_4_place_x_value, y=self.additional_label_4_place_y_value, anchor='ne')

        self.additional_label_4.bind("<Button-1>", self.display_drop_down_menu)

        self.meditation_body_width = int(screen_width / 3.84)
        self.meditation_body_height = int(screen_height / 2.88)
        self.meditation_body_place_x_value = int(screen_width / 15.36)
        self.meditation_body_place_y_value = int(screen_height / 4.32)

        self.meditation_body = Frame(self, width=self.meditation_body_width, height=self.meditation_body_height, bg="#B3C8CF", highlightthickness=2, highlightcolor="black")
        self.meditation_body.place(x=self.meditation_body_place_x_value, y=self.meditation_body_place_y_value)

        self.buttons_width = int(screen_width / 76.8)
        self.buttons_height = int(screen_height / 288)

        self.buttons_place_x_val = int(screen_width / 2.3167)

        self.fav_button = Button(self,text="View My Favorites", width=self.buttons_width, height=self.buttons_height, bg="lightgrey", font=("Arial", 13, "bold"), command=self.go_to_page3)
        self.fav_button.place(x=self.buttons_place_x_val, y=int(screen_height / 2.88))

        self.profile_button = Button(self,text="View My Profile", width=self.buttons_width, height=self.buttons_height, bg="lightgrey", font=("Arial", 13, "bold"), command=self.go_to_page4)
        self.profile_button.place(x=self.buttons_place_x_val, y=int(screen_height / 2.16))

        self.about_button = Button(self,text="View About Us", width=self.buttons_width, height=self.buttons_height, bg="lightgrey", font=("Arial", 13, "bold"), command=self.go_to_page5)
        self.about_button.place(x=self.buttons_place_x_val, y=int(screen_height / 1.728))

        self.music_body_width = int(screen_width / 3.84)
        self.music_body_height = int(screen_height / 2.88)
        self.music_body_place_x_value = int(screen_width / 1.536)
        self.music_body_place_y_value = int(screen_height / 4.32)

        self.music_body = Frame(self, width=self.music_body_width, height=self.music_body_height, bg="#B3C8CF", highlightthickness=2, highlightcolor="black")
        self.music_body.place(x=self.music_body_place_x_value, y=self.music_body_place_y_value)

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

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()


        for widget in self.meditation_body.winfo_children():
            widget.destroy()

        # Setting the number of rows and columns for the grid layout
        num_rows = 4
        num_columns = 2

        session_frame_width = int(screen_width / 12.8)
        session_frame_height = int(screen_height / 10.8)

        padding_x= int(screen_width / 153.6)
        padding_y = int(screen_height / 86.4)

        add_to_favorites_button_width = int(screen_width / 102.4)

        # Initializing row and column counters
        row = 0
        column = 0
        for session_num in meditation_sessions_list:

            session_frame = Frame(self.meditation_body, width=session_frame_width, height=session_frame_height, bg="#B3C8CF", padx=padding_x, pady=padding_y, highlightbackground="black", highlightthickness=1, highlightcolor="black")
            session_frame.grid(row=row, column=column, padx=padding_x, pady=padding_y, sticky="nsew")  # Add sticky option to stretch the frame

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


            add_to_favorites_button = Button(session_frame, text="Add to Favorites", height=1, width=add_to_favorites_button_width, command=lambda num = session_num: self.add_to_favorites(num))
            add_to_favorites_button.pack(fill="both", expand=True, pady=(5,0))

            # Increment row and column
            row += 1
            if row == num_rows:
                row = 0
                column += 1


    def update_music_display(self):
            """Method to Update Music Frame Display."""

            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screenheight()

            for widget in self.music_body.winfo_children():
                widget.destroy()

            # Setting the number of rows and columns for the grid layout
            num_rows = 4
            num_columns = 2

            session_frame_width = int(screen_width / 12.8)
            session_frame_height = int(screen_height / 10.8)

            padding_x= int(screen_width / 153.6)
            padding_y = int(screen_height / 86.4)

            add_to_favorites_button_width = int(screen_width / 102.4)

            # Initializing row and column counters
            row = 0
            column = 0
            for session_num in music_list:
                session_frame = Frame(self.music_body, width=session_frame_width, height=session_frame_height, bg="#B3C8CF", padx=padding_x, pady=padding_y, highlightbackground="black", highlightthickness=1, highlightcolor="black")
                session_frame.grid(row=row, column=column, padx=padding_x, pady=padding_y, sticky="nsew")  # Add sticky option to stretch the frame

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

                add_to_favorites_button = Button(session_frame, text="Add to Favorites", height=1, width=add_to_favorites_button_width, command=lambda num = session_num: self.add_to_favorites(num))
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

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.database = Database()
        self.sounds = Sounds()

        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.favorites_page_header_width = int(screen_width / 61.44)
        self.favorites_page_header_height = int(screen_height / 432)
        self.favorites_page_header_place_x_value = int(screen_height / 6.095)
        self.favorites_page_header_place_y_value = int(screen_height / 86.4)

        self.favorites_page_header = Label(self, text="My Favorites", fg="black", bg = "lightblue", width=self.favorites_page_header_width, height=self.favorites_page_header_height, font=("Algerian", 50))
        self.favorites_page_header.place(x=self.favorites_page_header_place_x_value,y=self.favorites_page_header_place_y_value)

        self.favorites_body_width = int(screen_width / 2.194)
        self.favorites_body_height = int(screen_height / 1.728)
        self.favorites_body_place_x_value = int(screen_width / 6.144)
        self.favorites_body_place_y_value = int(screen_height / 4.32)

        self.favorites_body = Frame(self, width=self.favorites_body_width, height=self.favorites_body_height, bg="white", highlightthickness=2, highlightcolor="black")
        self.favorites_body.place(x=self.favorites_body_place_x_value, y=self.favorites_body_place_y_value)

        self.back_home_button_width = int(screen_width / 76.8)
        self.back_home_button_height = int(screen_height / 288)
        
        self.back_home_button_place_x_value = int(screen_width / 2.3167)
        self.back_home_button_place_y_value = int(screen_height / 1.3824)


        self.back_home_button = Button(self,text="Back to Home", width=self.back_home_button_width, height=self.back_home_button_height, bg="lightgrey", font=("Arial", 13, "bold"), command=self.go_to_page2)
        self.back_home_button.place(x=self.back_home_button_place_x_value, y=self.back_home_button_place_y_value)

        self.update_favorites_display()

    def update_favorites_display(self):
        """Method to Update Favorites Frame Display."""

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        padding_x= int(screen_width / 153.6)
        padding_y = int(screen_height / 86.4)

        for widget in self.favorites_body.winfo_children():
                widget.destroy()

        if len(favorites_list) == 0:
            text = Label(self.favorites_body, text="No Favorites Yet", font=("Arial", 16, "bold"))
            text.grid(row=0, column=0, padx=padding_x, pady=padding_y)
        else:
            

            # Setting the number of rows and columns for the grid layout
            num_rows = 3
            num_columns = 5

            session_frame_width = int(screen_width / 12.8)
            session_frame_height = int(screen_height / 10.8)

            # Initializing row and column counters
            row = 0
            column = 0
            for session_num in favorites_list:
                session_frame = Frame(self.favorites_body, width=session_frame_width, height=session_frame_height, bg="lightgrey", padx=padding_x, pady=padding_y)
                session_frame.grid(row=row, column=column, padx=padding_x, pady=padding_y, sticky="nsew")  # Add sticky option to stretch the frame

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

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        global favorites_list
        global progress

        self.screen_width = self.winfo_screenwidth()
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.title_label_padding_x = int(screen_width / 76.8)
        self.title_label_padding_y = int(screen_height / 43.2)
        self.title_label_place_x_value = int(screen_width / 10.24)
        self.title_label_place_y_value = int(screen_height / 43.2)

        # Set window title
        self.title_label = Label(self, text='My Profile', font=("Georgia", 25, 'bold'),
                            bg='#808080',
                            padx=self.title_label_padding_x, pady=self.title_label_padding_y)
        self.title_label.place(x = self.title_label_place_x_value , y = self.title_label_place_y_value)

        # Load image
        self.image_2 = PhotoImage(file='image2.png')

        # Define new width and height for the image
        self.new_width, self.new_height = int(screen_width / 25.6), int(screen_height / 14.4)  # Adjust the size as needed

        # Resize the image
        self.image_2_resized = self.image_2.subsample(int(self.image_2.width() / self.new_width),
                                                            int(self.image_2.height() / self.new_height))

        self.additional_label_place_x_value = int(screen_width / 10.97)
        self.additional_label_place_y_value = int(screen_height / 34.56)

        # Create label with resized image
        self.additional_label = Label(self, image=self.image_2_resized, bg='#D8A9B3', relief='raised')
        self.additional_label.place(x=self.additional_label_place_x_value, y=self.additional_label_place_y_value, anchor='ne')


        #image 3
        self.image_3 = PhotoImage(file='image3.png')
        self.image3_resized = self.image_3.subsample(int(self.image_3.width() / self.new_width),
                                                            int(self.image_3.height() / self.new_height))
        
        self.Label_image_3_place_x_value = int(screen_width / 1.28)
        self.Label_image_3_place_y_value = int(screen_height / 4.8)
        self.Label_image_3 = Label(self, image=self.image_3, border= 2 ,bg='#C0C0C0', relief='raised')
        self.Label_image_3.place(x=self.Label_image_3_place_x_value, y=self.Label_image_3_place_y_value, anchor='ne')

        self.update_profile_page()


    def update_profile_page(self):
        """Method to Update Profile Page Display."""

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()


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


        Frame_Text_width = int(screen_width / 2.7927)
        Frame_Text_height = int(screen_height / 1.5428)
        Frame_Text_place_x_value = int(screen_width / 30.72)
        Frame_Text_place_y_value = int(screen_height / 8.22857)
        
        #Frame 
        Frame_Text = Frame(self, width=Frame_Text_width, height=Frame_Text_height, bg='#C0C0C0', highlightthickness=2, highlightbackground="white")
        Frame_Text.place(x=Frame_Text_place_x_value, y=Frame_Text_place_y_value)


        Text_labels_place_x_value = int(screen_width / 307.2)
        Text_label_place_y_value = int(screen_height / 43.2)
        
        #Email inside the frame
        Text_label = Label( Frame_Text ,text="Email: ", font=("Georgia", 20, 'bold'), bg='#C0C0C0', fg='Black')
        Text_label.place(x= Text_labels_place_x_value, y = Text_label_place_y_value)

        Text_label_1_place_y_value = int(screen_height / 11.52)

        Text_label_1 = Label( Frame_Text ,text=f"* {email}", font=("Georgia", 18, 'bold'), bg='#C0C0C0', fg='Black')
        Text_label_1.place(x= Text_labels_place_x_value, y = Text_label_1_place_y_value)

        Text_label_2_place_y_value = int(screen_height / 6.1714)
        Text_label_3_place_y_value = int(screen_height / 4.32)

        #Favorite inside the text frame
        Text_label_2 = Label( Frame_Text ,text="Favorites: ", font=("Georgia", 20, 'bold'), bg='#C0C0C0', fg='Black')
        Text_label_2.place(x= Text_labels_place_x_value, y = Text_label_2_place_y_value)
        Text_label_3 = Label( Frame_Text ,text=bullet_points, font=("Georgia", 20, 'bold'), bg='#C0C0C0', fg='Black')
        Text_label_3.place(x= Text_labels_place_x_value, y = Text_label_3_place_y_value)

        #Progress inside the text frame 


        Text_label_4_place_y_value = int(screen_height / 2.107)
        Text_label_5_place_y_value = int(screen_height / 1.92)

        Text_label_4 = Label( Frame_Text ,text="Time in App: ", 
                            font=("Georgia", 20, 'bold'), 
                            bg='#C0C0C0', fg='Black')
        Text_label_4.place(x= Text_labels_place_x_value, y = Text_label_4_place_y_value)
        Text_label_5 = Label( Frame_Text ,text=f"{formatted_time}", font=("Georgia", 18, 'bold'), bg='#C0C0C0', fg='Black')
        Text_label_5.place(x= Text_labels_place_x_value, y = Text_label_5_place_y_value)

        back_home_button_width = int(screen_width / 76.8)
        back_home_button_height = int(screen_height / 288)
        back_home_button_x_value = int(screen_width / 2.3167)
        back_home_button_y_value = int(screen_height / 1.3824)


        back_home_button = Button(self, text="Back to Home", width=back_home_button_width, height=back_home_button_height, bg="lightgrey", font=("Arial", 13, "bold"), command=self.go_to_page2)
        back_home_button.place(x=back_home_button_x_value,y=back_home_button_y_value)

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

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()


        main_frame_width = int(screen_width / 2.56)
        main_frame_height = int(screen_height / 2.16)
        main_frame_place_x_value = int(screen_width / 4.8)
        main_frame_place_y_value = int(screen_height / 86.4)
        # Creating the main rectangle frame
        main_frame = Frame(self, width=main_frame_width, height=main_frame_height, relief='solid', borderwidth=2)
        main_frame.place(x=main_frame_place_x_value, y=main_frame_place_y_value)

        # Creating squares with images and names
        members = [
            ("Bereket", "no_profile.png"),
            ("Bhavik", "no_profile.png"),
            ("Ahmed", "no_profile.png"),
            ("Ghanasham", "no_profile.png"),
            ("Ghazal", "no_profile.png")
        ]

        square_frame_width = int(screen_width / 15.36)
        square_frame_height = int(screen_height / 8.64)
        padding_x_2 = int(screen_width / 153.6)
        padding_y_2 = int(screen_height / 86.4)

        for i, (name, image_file) in enumerate(members):
            square_frame = Frame(main_frame, width=square_frame_width, height=square_frame_height, relief='solid', borderwidth=1)
            square_frame.grid(row=0, column=i, padx=padding_x_2, pady=padding_y_2)
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
        You can view you're progress with Aumeter in your profile page

        Study Music:

        Enhance your focus and productivity with our curated collection of study music. Whether you're studying for exams, working on
        a project, or seeking creative inspiration, our ambient music tracks create an optimal environment for concentration and mental clarity.

        Personalized Favorites Preferences: 
        
        Tailor your meditation experience to suit your unique preferences with our personalized favorites
        feature. Mark your favorite meditation sessions, and study music that resonates with you. 
        """
        explanation_label_wrap_length = int(screen_width / 1.687)
        explanation_label_width = int(screen_width / 13.963)
        explanation_label_place_x_value = int(screen_width / 15.36)
        explanation_label_place_y_value = int(screen_height / 3.456)

        explanation_label = tk.Label(self, text=explanation_text, wraplength=explanation_label_wrap_length, width = explanation_label_width, justify="left", font=("Times New Roman", 12))
        explanation_label.place(x=explanation_label_place_x_value, y=explanation_label_place_y_value)


        self.new_width, self.new_height = int(screen_width / 25.6), int(screen_height / 14.4)  # Adjust the size as needed
        

        #image 3
        self.image_3 = PhotoImage(file='image3.png')
        self.image3_resized = self.image_3.subsample(int(self.image_3.width() / self.new_width),
                                                            int(self.image_3.height() / self.new_height))
        
        self.Label_image_3 = Label(self, image=self.image_3, border= 2 ,bg='#C0C0C0', relief='raised')
        self.Label_image_3.place(x=int(screen_width / 1.3653), y=int(screen_height / 3.0857))


        back_home_button_2_width = int(screen_width / 76.8)
        back_home_button_2_height = int(screen_height / 288)
        back_home_button_2_place_x_value = int(screen_width / 1.28)
        back_home_button_2_place_y_value = int(screen_height / 1.28)

        self.back_home_button_2 = Button(self,text="Back to Home", width=back_home_button_2_width, height=back_home_button_2_height, bg="lightgrey", font=("Arial", 13, "bold"), command=self.go_to_page2)
        self.back_home_button_2.place(x=back_home_button_2_place_x_value,y=back_home_button_2_place_y_value)

        

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
        print("width: ", screen_width)
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
