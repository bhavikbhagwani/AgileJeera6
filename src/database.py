"""
Database class.

This class instantiates the Database, Authentication and Storage used within
this application and contains methods to work with these services
"""

import pyrebase
from tkinter import *

class Database:
    """Database Class."""
    def __init__(self):
        """Init Method."""
        ### database configuration
        self.firebaseConfig = {
            "apiKey": "AIzaSyAOocpYNTxcjEQt6k8dBylG1v6z0FCoH9c",
            "authDomain": "aumeter-76464.firebaseapp.com",
            "projectId": "aumeter-76464",
            "databaseURL": "https://aumeter-76464-default-rtdb.europe-west1.firebasedatabase.app/",
            "storageBucket": "aumeter-76464.appspot.com",
            "messagingSenderId": "190558912756",
            "appId": "1:190558912756:web:61395c95194f00c8ff5ea1",
            "measurementId": "G-JDYXSBLX3D"
        }
        self.firebase = pyrebase.initialize_app(self.firebaseConfig)
        self.database = self.firebase.database()
        self.authentication = self.firebase.auth()
        self.storage = self.firebase.storage()

    def log_in(self, email,password):
        """Method for user logging in."""
        try:
            self.authentication.sign_in_with_email_and_password(email, password)
            user_ID = self.get_user_ID()

            return True, user_ID
        except:

            return False, None

    def sign_up(self, email, password):
        """Method for user signing up."""
        try:
            self.authentication.create_user_with_email_and_password(email, password)
            self.authentication.sign_in_with_email_and_password(email, password)
            user_ID = self.get_user_ID()
            self.add_user(user_ID)

            return True, user_ID
        except:

            return False, None

    def get_user_ID(self):
        """Method to get User ID."""
        user = self.authentication.current_user
        if user:
            return user['localId']
        else:
            return None

    def get_user_email(self):
        """Method to get Email."""
        user = self.authentication.current_user
        if user:
            return user['email']
        else:
            return None

    def add_user(self, user_ID):
        """Method to Add New User."""
        user_info = {"email":self.get_user_email(), "medi_sessions":[1, 2, 3, 4, 5, 6, 7, 8], "music_sessions" : [9, 10 ,11 , 12, 13, 14, 15, 16], "favorites":[], "progress":0}
        self.database.child("Users").child(user_ID).set(user_info)
    

    def get_meditation_list_for_this_user(self, user_ID):
        """Method to get meditation list."""
        this_user = self.database.child("Users").child(user_ID).get().val()
        meditation_sessions_list = this_user["medi_sessions"]

        return meditation_sessions_list

    def get_study_music_list_for_this_user(self, user_ID):
        """Method to get music list."""
        this_user = self.database.child("Users").child(user_ID).get().val()
        study_music_list = this_user["music_sessions"]

        return study_music_list

    def get_favorites_list_for_this_user(self, user_ID):
        """Method to get favorites list."""
        this_user = self.database.child("Users").child(user_ID).get().val()
        favorites_list = this_user.get("favorites",[])
        
        return favorites_list

    def get_progress(self, user_ID):
        """Method to get progress (integer)."""
        this_user = self.database.child("Users").child(user_ID).get().val()
        progress = this_user.get("progress")

        return progress
    
    def save_user_info(self, user_ID, email, favorites_list, progress):
        # Prepare user info
        user_info = {
            "email": email, 
            "medi_sessions":[1,2,3,4,5,6,7,8], 
            "music_sessions" : [9,10,11,12,13,14,15,16], 
            "favorites":favorites_list, 
            "progress":progress
                    }
        
        # Retrieve user ID
        print("User_ID retrieved for this user: ", user_ID)
        try:
            # store user info in database
            self.database.child("Users").child(user_ID).set(user_info)
            print("Data stored in database")
            print(user_info)
        except Exception as e:
            print(f"Error: {e}")
