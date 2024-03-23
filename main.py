#importing packages

import speech_recognition as sr   #to recognize the words
import win32com.client  
import webbrowser                 #handling web activities        
import os
import datetime




#importing .py files
from social_accounts import social_account
from social_accounts import websites
from pc_functions import functions_of_pc




#defining the function
def said(text):
    buddy_speaker = win32com.client.Dispatch("SAPI.SpVoice")
    buddy_speaker.Speak(text)

def recognize_audio():
    au = sr.Recognizer()
    try:
        with sr.Microphone() as source_of_audio:
            au.pause_threshold = 0.6
            audio = au.listen(source_of_audio)
            result = au.recognize_google(audio,language="en-PK")
            print(f"The recognize voice is {result}")
            return result.lower()
    except:
        return "Some error occured sorry for inconvenience  !!"

        

if __name__ =="__main__":
    said("Hello Karim How are you..I am Buddy Your assisstant I would always be here to help you.")
    while True:
        print("listening...")
        audio =recognize_audio()

        #Search all your accounts and then open the required account
        for account in social_account:
            if f"open my {account[0]} account" in audio:
                said(f"opening your {account[0]} account.")
                webbrowser.open(account[1])


        #Search all websites and check what website you want to open 
        for site in websites:
            if f"open {site[0]}" in audio:
                said(f"Opening {site[0]}")
                webbrowser.open(site[1])
        
        #Pc functionalities
        for function in functions_of_pc:
            if f"open {function[0]}" in audio:
                said(f"Opening {function[0]}")
                os.startfile(function[1])
                
        if f"what is the time" in audio:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            said(f"time is {time}")                        
                

        