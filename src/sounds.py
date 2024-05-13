import pygame
import io
import requests

class Sounds:
    def __init__(self):
        # Initialize any variables or setup needed for sound handling
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
            9: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/Weekend.mp3?alt=media&token=ea4bafbb-edc3-460f-84b2-c69ae08da533",
            10: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/Pomodoro.mp3?alt=media&token=88242fdb-2079-474d-8926-47ca23a0d021",
            11: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/Ondas%20Binaurais%20Aumentar.mp3?alt=media&token=55209620-5dde-4293-bddc-cdfd0237bf2d",
            12: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/brown%20noise.mp3?alt=media&token=dd051385-4f9a-43ac-bd29-f018f4665dfe",
            13: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/Calming%20handpan.mp3?alt=media&token=e7062ea9-6a47-4b44-939a-7d8f10f81016",
            14: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/romanticizing%20studying%20playlist.mp3?alt=media&token=1dd924bb-b3d9-4b0f-895f-4f20e53d2d9f",
            15: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/%5BCOPYRIGHT%20FREE%5D%201H%20Study%20Music%20%26%20Ambience%20(Oppenheimer%20Style)%20-%20Jeremy%20Brauns%20Music%20%23oppenheimer.mp3?alt=media&token=d70180ed-4beb-45ba-af49-7a587f7990ab",
            16: "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/This%20Playlist%20Will%20Make%20Studying%20Physics%20Seem%20Cool.mp3?alt=media&token=a41eb92c-5319-480b-ae0a-d18ea8139181"
        }

    def get_sound_url(self, number):
        # Method to get the URL of a sound based on its number
        return self.sound_urls_dictionary.get(number)

    def play_sound(self, number):
        # Method to play a sound given its number
        sound_url = self.get_sound_url(number)
        response = requests.get(sound_url)
        sound_file = io.BytesIO(response.content)
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()


    def stop_sound(self):
        # Method to stop the currently playing sound
        pygame.mixer.music.stop()