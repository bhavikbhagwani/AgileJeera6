import pyrebase
from tkinter import *
from tkinter import messagebox

class Database:
    def __init__(self):

        self.firebaseConfig = {
            "apiKey": "AIzaSyAOocpYNTxcjEQt6k8dBylG1v6z0FCoH9c",
            "authDomain": "aumeter-76464.firebaseapp.com",
            "projectId": "aumeter-76464",
            "databaseURL":"https://aumeter-76464-default-rtdb.europe-west1.firebasedatabase.app/",
            "storageBucket": "aumeter-76464.appspot.com",
            "messagingSenderId": "190558912756",
            "appId": "1:190558912756:web:61395c95194f00c8ff5ea1",
            "measurementId": "G-JDYXSBLX3D"
        }
        self.firebase = pyrebase.initialize_app(self.firebaseConfig)
        self.database = self.firebase.database()
        self.authentication = self.firebase.auth()
        self.storage = self.firebase.storage()
        
      
        
    
    def log_in(self,email,password):
        try:
            self.authentication.sign_in_with_email_and_password(email,password)
            user_ID = self.get_user_ID()
            
            return True, user_ID
        except:
            
            return False, None

    
    def sign_up(self,email,password):
        try:
            self.authentication.create_user_with_email_and_password(email,password)
            self.authentication.sign_in_with_email_and_password(email, password)

            user_ID = self.get_user_ID()
            
            return True, user_ID
        except:
            
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
        user_info = {"email":self.get_user_email(), "medi_sessions":[1,2,3,4,5,6,7,8], "music_sessions" : [9,10,11,12,13,14,15,16], "favorites":[], "progress":0}
        self.database.child("Users").child(user_ID).set(user_info)

    def get_meditation_list_for_this_user(self, user_ID):
        this_user = self.database.child("Users").child(user_ID).get().val()
        meditation_sessions_list = this_user["medi_sessions"]
        return meditation_sessions_list

    def get_study_music_list_for_this_user(self, user_ID):
        this_user = self.database.child("Users").child(user_ID).get().val()
        study_music_list = this_user["music_sessions"]
        return study_music_list

    def get_favorites_list_for_this_user(self, user_ID):

        this_user = self.database.child("Users").child(user_ID).get().val()
        favorites_list = this_user.get("favorites",[])
        
        return favorites_list

    def get_progress(self, user_ID):
        this_user = self.database.child("Users").child(user_ID).get().val()
        progress = this_user.get("progress")

        return progress
