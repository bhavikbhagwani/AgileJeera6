from tkinter import *

# Main window 
Window = Tk()
Window.title("Aumeter")

# Get the screen width and height
screen_width = Window.winfo_screenwidth()
screen_height = Window.winfo_screenheight()

# Set the geometry of the window to fill the entire screen
Window.geometry(f"{screen_width}x{screen_height}+0+0")

#background for the window
Window.config(background='#D8A9B3')

title_label = Label(Window, text='Aumeter', font = ("Algerian", 60),
                     padx= 20, pady= 20,
                     bg='#D8A9B3')
title_label.pack()

#icon
icon = PhotoImage(file='icon.png')
Window.iconphoto(True, icon)

# StringVar objects to store the username and password
username_var = StringVar()
password_var = StringVar()


# Username label 
username_label = Label(Window, text="Username: ", font=("Forte", 25), bg='#D8A9B3', fg='Black')
username_label.place(x=5, y=240 )

# Username entry field
username_entry = Entry(Window, textvariable=username_var ,bd=2, relief= 'ridge')
username_entry.place(x=100, y=300 , width= 280)

# Password label
password_label = Label(Window, text='Password: ', font=("Forte", 25), bg='#D8A9B3')
password_label.place(x=5, y=360, anchor='w')

# Password entry field
password_entry = Entry(Window, textvariable=password_var,show='*', bd = 2, relief='ridge') 
password_entry.place(x = 100, y = 400, width=280)


#Another lable
additional_image = PhotoImage(file='image1.png')

# Reduce image size
new_width, new_height = 400, 400  # Adjust the size as needed
additional_image = additional_image.subsample(int(additional_image.width() / new_width), int(additional_image.height() / new_height))

# Additional label with resized image
additional_label = Label(Window, image=additional_image,bg='#D8A9B3', relief='raised')
additional_label.place(x=screen_width - new_width + 360, y=150, anchor='ne')

#medittiation word
meditation_text_label = Label(Window, text= "Inhale the future, exhale the past." , 
                              font=("Forte", 18), wraplength=300, justify=LEFT, bg='#D8A9B3')
meditation_text_label.place(x= 900, y=580)


login_button = Button(Window, text="Login", font=("Forte", 20), bg='white', fg='black', )
login_button.place(x=170, y=480, width=120)

Window.mainloop()