"""Sounds class."""
import pygame
import io
import requests

"""
    This class handles playing sounds for different activities such as meditation
    and study music.

    Attributes:
    - sound_urls_dictionary (dict): A dictionary containing URLs of different
      sound files mapped to their respective identifiers.
    - sound_to_name_dictionary (dict): A dictionary mapping sound identifiers
      to their corresponding names.

    Methods:
    - get_sound_url(number): Returns the URL of the sound file associated with
      the given number.
    - get_sound_name(number): Returns the name of the sound associated with the
      given number.
    - play_sound(number): Plays the sound associated with the given number.
    - stop_sound(): Stops the currently playing sound.
    """

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
            7: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/meditation_not_yet.mp3?alt=media&token=8b365f56-0498-45d9-a3c5-96d6bf42ab1b",
            8: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/meditation_not_yet.mp3?alt=media&token=8b365f56-0498-45d9-a3c5-96d6bf42ab1b",
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
            7: "MS7",
            8: "MS8",
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