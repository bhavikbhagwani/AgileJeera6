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
            "5": "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/Calming%20handpan.mp3?alt=media&token=e7062ea9-6a47-4b44-939a-7d8f10f81016"
        }
