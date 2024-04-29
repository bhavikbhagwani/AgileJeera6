import pygame
import requests
import io
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class MusicPlayer:
    def __init__(self):
        self.master = Tk()
        self.master.title("Study music")
        self.master.withdraw() 
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
    
        self.master.geometry(f"{screen_width}x{screen_height}")
        # Initialize Pygame
        pygame.init()

        # Music URLs
        self.music_urls = {
            "1": "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/Weekend.mp3?alt=media&token=ea4bafbb-edc3-460f-84b2-c69ae08da533",
            "2": "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/Pomodoro.mp3?alt=media&token=88242fdb-2079-474d-8926-47ca23a0d021",
            "3": "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/Ondas%20Binaurais%20Aumentar.mp3?alt=media&token=55209620-5dde-4293-bddc-cdfd0237bf2d",
            "4": "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/brown%20noise.mp3?alt=media&token=dd051385-4f9a-43ac-bd29-f018f4665dfe",
            "5": "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/Calming%20handpan.mp3?alt=media&token=e7062ea9-6a47-4b44-939a-7d8f10f81016",
            "6": "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/romanticizing%20studying%20playlist.mp3?alt=media&token=1dd924bb-b3d9-4b0f-895f-4f20e53d2d9f",
            "7": "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/%5BCOPYRIGHT%20FREE%5D%201H%20Study%20Music%20%26%20Ambience%20(Oppenheimer%20Style)%20-%20Jeremy%20Brauns%20Music%20%23oppenheimer.mp3?alt=media&token=d70180ed-4beb-45ba-af49-7a587f7990ab",
            "8": "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/This%20Playlist%20Will%20Make%20Studying%20Physics%20Seem%20Cool.mp3?alt=media&token=a41eb92c-5319-480b-ae0a-d18ea8139181"
        }

        # Create GUI elements
        self.label = Label(self.master, text="Select a song:")
        self.label.pack()

        self.song_buttons = []
        for key, value in self.music_urls.items():
            button = Button(self.master, text=f"Song {key}", command=lambda key=key: self.play_song(key))
            button.pack()
            self.song_buttons.append(button)

         # Control Frame
        control_frame = ttk.Frame(self.master)
        control_frame.pack(pady=20)

        play_button = ttk.Button(control_frame, text="▶️", command=self.play_song)
        play_button.grid(row=0, column=0, padx=10)

        unpause_button = ttk.Button(control_frame, text="⏯️", command=self.unpause_music)
        unpause_button.grid(row=0, column=1, padx=10)

        pause_button = ttk.Button(control_frame, text="⏸️", command=self.pause_music)
        pause_button.grid(row=0, column=2, padx=10)

        add_button = ttk.Button(control_frame, text="❤️", command=self.add_to_favorites)
        add_button.grid(row=0, column=3, padx=10)