import pygame
import requests
import io

# Initialize 
pygame.init()

# play audio from a URL
def play_audio(url):
    # Download MP3 file from the URL
    response = requests.get(url)
    mp3_data = io.BytesIO(response.content)

    # Initialize mixer
    pygame.mixer.init()

    # Load MP3 data into Pygame mixer
    pygame.mixer.music.load(mp3_data)

    # Play the loaded MP3 file
    pygame.mixer.music.play()

# Function to pause music
def pause_music():
    pygame.mixer.music.pause()

# Function to unpause music
def unpause_music():
    pygame.mixer.music.unpause()

# Music URLs
music_urls = {
    "1": "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/Weekend.mp3?alt=media&token=ea4bafbb-edc3-460f-84b2-c69ae08da533",
    "2": "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/Pomodoro.mp3?alt=media&token=88242fdb-2079-474d-8926-47ca23a0d021",
    "3": "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/Ondas%20Binaurais%20Aumentar.mp3?alt=media&token=55209620-5dde-4293-bddc-cdfd0237bf2d",
    "4": "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/brown%20noise.mp3?alt=media&token=dd051385-4f9a-43ac-bd29-f018f4665dfe",
    "5": "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/Calming%20handpan.mp3?alt=media&token=e7062ea9-6a47-4b44-939a-7d8f10f81016"
}

# Display options
print("Choose from 1 to 5")

# Main loop
while True:
    user_input = input("Enter your choice (1 to 5), 'p' to pause, 'r' to resume, or 'q' to quit: ")

    if user_input in music_urls:
        play_audio(music_urls[user_input])
    elif user_input == 'p':
        pause_music()
    elif user_input == 'r':
        unpause_music()
    elif user_input == 'q':
        break
    else:
        print("Invalid input. Please try again.")

# Quit pygame
pygame.quit()