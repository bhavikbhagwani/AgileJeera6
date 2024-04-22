import pyrebase
from tkinter import *
from tkinter import messagebox

class save_to_data_base:
    def __init__(self):

        self.firebaseConfig = {
        "apiKey" : "AIzaSyDqp5UMRewvQ7AqBK3hUJ-WC35VgiY6IKo",
        "authDomain" : "aumeter-39cb1.firebaseapp.com",
        "projectId" : "aumeter-39cb1",
        "storageBucket" : "aumeter-39cb1.appspot.com",
        "databaseURL" : "https://aumeter-39cb1-default-rtdb.firebaseio.com/",
        "messagingSenderId" : "738275596786",
        "appId" : "1:738275596786:web:5b35e22bd376bef035736b",
        "measurementId" : "G-BHL5KS350N"
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
            messagebox.showinfo("Success","Sign Up Successful, you will be directed to the home page")
            return True
        except:
            messagebox.showerror("Error","Sign up not successful, wrong email or password")
            return False






