import pygame
import urllib.request

pygame.init()


def play_audio(url):
    try:
        # Download 
        urllib.request.urlretrieve(url, "temp_audio.mp3")

        # Load 
        pygame.mixer.music.load("temp_audio.mp3")

        # Play 
        pygame.mixer.music.play()

        # Wait for audio to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print("Error playing audio:", e)

# UPDATED URLS FOR ALL NEW STORAGE LINKS
music_urls = {
    "1": "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/Weekend.mp3?alt=media&token=ea4bafbb-edc3-460f-84b2-c69ae08da533",
    "2": "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/Pomodoro.mp3?alt=media&token=88242fdb-2079-474d-8926-47ca23a0d021",
    "3": "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/Ondas%20Binaurais%20Aumentar.mp3?alt=media&token=55209620-5dde-4293-bddc-cdfd0237bf2d",
    "4": "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/brown%20noise.mp3?alt=media&token=dd051385-4f9a-43ac-bd29-f018f4665dfe",
    "5": "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/Calming%20handpan.mp3?alt=media&token=e7062ea9-6a47-4b44-939a-7d8f10f81016"
}

# display options and get user input
def display_options():
    dispaly = """1.weekend
2.pomodoro
3.ondas
4.brown_noise
5.calming_med
6.exit"""
    return f"Select a music option:\n{dispaly}\np: Pause\nn: Next\nOr type 'exit' to quit."

# Main 
while True:
    print(display_options())
    user_input = input("Enter option: ")

    if user_input.lower() == "exit":
        break

    if user_input.lower() == "p":
        pygame.mixer.music.pause()
    elif user_input.lower() == "n":
        pygame.mixer.music.stop()
    elif user_input in music_urls:
        play_audio(music_urls[user_input])
    else:
        print("Invalid option. Please try again.")




