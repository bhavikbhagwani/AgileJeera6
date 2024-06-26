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
            8: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/meditation_8_2.mp3?alt=media&token=4f6ea3b1-b07d-4453-87db-12a74698377e",
            #study music
            9: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/weekend.mp3?alt=media&token=1103b55a-1728-4520-8cad-fcca39cbf0eb",
            10: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/pomodoro.mp3?alt=media&token=600f4b56-4f91-47fd-ae9f-5c0c8aeeabd3",
            11: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/ondas-binaurais.mp3?alt=media&token=d6c7088d-189e-406b-bba6-222d107e5a2b",
            12: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/brown%20noise.mp3?alt=media&token=99bb1efb-85bf-4b3f-8a20-e8e639719971",
            13: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/Calming%20handpan.mp3?alt=media&token=bcf07e4b-c8a6-4e59-930f-6c970557c229",
            14: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/classical.mp3?alt=media&token=141b398a-147b-4754-aaaf-903b6ac07d30",
            15: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/rain-books-and-coffee.mp3?alt=media&token=bb4350e0-345a-472a-a10d-3ae19881ad21",
            16: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/solas.mp3?alt=media&token=06e43d6b-5045-4925-a92f-6416e689a6b0"
        }

        self.sound_to_name_dictionary = {
            1: "Breathing",
            2: "Mindfulness",
            3: "Focus",
            4: "Walking",
            5: "Mantra - AUM",
            6: "Body Scan",
            7: "Fire",
            8: "Mirror Gazing",
            9: "TheWeeknd",
            10: "Pomodoro",
            11: "Binary Waves",
            12: "Brown Noise",
            13: "Calming Handpan",
            14: "Classical Music",
            15: "Rain and Books",
            16: "Solas"
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
            progress = self.database.get_progress(user_ID)
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

        for number in favorite_list_to_show:
            name = self.sounds.get_sound_name(number)
            new_favorites_list_to_show.append(name)
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        progress = progress + elapsed_time

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


class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aumeter App")
        self.database = Database()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")

        self.current_page = None
        self.show_page(Page1)
        

    def show_page(self, page):
        if self.current_page:
            self.current_page.pack_forget()  # Hide current page
        self.current_page = page(self)  # Create new page
        self.current_page.pack(fill="both", expand=True)  # Show new page

    

if __name__ == "__main__":
    try:

        app = MyApp()
        app.mainloop()
    except Exception as e:
        print("an error occurred: ", e)
