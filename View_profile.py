from tkinter import *

email = 'ahmednur10@gmail.com'

#if time is return string
time = '17.5432'
formatted_time = "{:.2f}".format(float(time))

#list of favorit 
 
favorite = ['studymusic 1' , 'studymusic 2']
bullet_points = '\n'.join([f'* {item}' for item in favorite])

#Should be able retrive does values.
"""def get_favorite_email_progress(self):
    user_ID = self.get_user_ID()
    if user_ID:
        user_data = self.database.child("Users").child(user_ID).get().val()
        if user_data:
            favorite_list = user_data.get('favorites')
            email = user_data.get('email')
            progress = user_data.get('progress')
        return favorite_list, email, progress
    return None, None, None """

# Create profile window
profile_window = Tk()
profile_window.config(background='#808080')
# Get screen dimensions
screen_width = profile_window.winfo_screenwidth()
screen_height = profile_window.winfo_screenheight()

# Set window geometry
profile_window.geometry(f"{screen_width}x{screen_height}")

# Set window title
title_label = Label(profile_window, text='Profile', font=("Georgia", 25, 'bold'),
                    bg='#808080',
                    padx=20, pady=20)
title_label.place(x = 150 , y = 20)

# Load image
additional_image = PhotoImage(file='image2.png')

# Define new width and height for the image
new_width, new_height = 60,60  # Adjust the size as needed

# Resize the image
additional_image_resized = additional_image.subsample(int(additional_image.width() / new_width),
                                                      int(additional_image.height() / new_height))

# Create label with resized image
additional_label = Label(profile_window, image=additional_image_resized, bg='#D8A9B3', relief='raised')
additional_label.place(x=140, y=25, anchor='ne')

#Frame 
Frame_Text = Frame(profile_window, width=500, height=560, bg='#C0C0C0', highlightthickness=2, highlightbackground="white")
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
Text_label_5 = Label( Frame_Text ,text=f"   {formatted_time}", font=("Georgia", 20, 'bold'), bg='#C0C0C0', fg='Black')
Text_label_5.place(x= 5, y = 450)

#image 3
image_3 = PhotoImage(file='image3.png')

new_width2, new_height2 = 800 , 800 
image3_resized = image_3.subsample(int(image_3.width() / new_width),
                                                      int(image_3.height() / new_height))
Label_image_3 = Label(profile_window, image=image_3, border= 2 ,bg='#C0C0C0', relief='raised')
Label_image_3.place(x=1200, y=180, anchor='ne')
# Run the Tkinter event loop
profile_window.mainloop()

