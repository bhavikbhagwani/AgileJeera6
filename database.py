import pyrebase
from tkinter import *
from tkinter import messagebox

class Database:
    def __init__(self):

        self.firebaseConfig = {
            "apiKey": "AIzaSyCZicUBD9oJ4_YqLbXbwaTQFUDpKDHVCWg",
            "authDomain": "aumeter-ee879.firebaseapp.com",
            "projectId": "aumeter-ee879",
            "databaseURL": "https://aumeter-ee879-default-rtdb.europe-west1.firebasedatabase.app/",
            "storageBucket": "aumeter-ee879.appspot.com",
            "messagingSenderId": "971497539312",
            "appId": "1:971497539312:web:bd251242a2feec3a96a435",
            "measurementId": "G-C5MH3PDK39"
        }
        self.firebase = pyrebase.initialize_app(self.firebaseConfig)
        self.database = self.firebase.database()
        self.authentication = self.firebase.auth()
        
      
        
    
    def log_in(self,email,password):
        try:
            self.authentication.sign_in_with_email_and_password(email,password)
            messagebox.showinfo("Success","Log In Successful, you will be directed to the home page")
            return True
        except:
            messagebox.showerror("Error","Log in not successful, wrong email or password")
            return False

    
    def sign_up(self,email,password):
        try:
            self.authentication.create_user_with_email_and_password(email,password)
            self.authentication.sign_in_with_email_and_password(email, password)
            
            user_ID = self.get_user_ID()
            messagebox.showinfo("Success","Sign Up Successful, you will be directed to the home page")
            return True, user_ID
        except:
            messagebox.showerror("Error","Sign up not successful, wrong email or password")
            return False, None
    
    def get_user_ID(self):
        user = self.authentication.current_user
        if user:
            return user['localId']
        else:
            return None
        
    def get_user_email(self):
        user = self.authentication.current_user
        if user:
            return user['email']
        else:
            return None

    def add_user(self, user_ID):
        user_info = {"email":self.get_user_email(), "medi_sessions":[1,2,3,4,5,6,7,8,9,10], "music_sessions" : [11,12,13,14,15], "favorites":[], "progress":0}
        self.database.child("Users").child(user_ID).set(user_info)








