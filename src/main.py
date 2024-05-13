from pages import Page1, Page2 , Page3, Page4
import os
import time
from tkinter import messagebox
import pygame
from database import Database
import tkinter as tk

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
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def show_page(self, page):
        if self.current_page:
            self.current_page.pack_forget()  # Hide current page
        self.current_page = page(self)  # Create new page
        self.current_page.pack(fill="both", expand=True)  # Show new page

    def save_everything_for_user(self):
        """Method to Save User's Contents/Progress into Database"""
        global start_time
        global progress
        global user_ID

        # Stop time progress and calculate elapsed time
        end_time = time.time()
        elapsed_time = end_time - start_time
        progress = progress + elapsed_time

        favorites_list = []
        
        # Prepare user info
        user_info = {
            "email": self.database.get_user_email(), 
            "medi_sessions":[1,2,3,4,5,6,7,8], 
            "music_sessions" : [9,10,11,12,13,14,15,16], 
            "favorites":favorites_list, 
            "progress":progress
                    }
        
        # Retrieve user ID
        print("User_ID retrieved for this user: ", user_ID)
        try:
            # store user info in database
            self.database.database.child("Users").child(user_ID).set(user_info)
            print("Data stored in database")
            print("favorite list stored: ", favorites_list)
            print("progress sotred: ", progress)
        except Exception as e:
            print(f"Error: {e}")

    def on_closing(self):
        """Method when user wants to exit."""
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):

            self.save_everything_for_user()
            #stop music if still playing
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()

            self.destroy()
            os.system("taskkill /F /T /PID {}".format(os.getpid()))

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
