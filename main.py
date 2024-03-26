#importing packages

import speech_recognition as sr   #to recognize the words
import win32com.client  
import webbrowser                 #handling web activities        
import os
import datetime
import wikipedia




#importing .py files
from social_accounts import social_account
from social_accounts import websites
from pc_functions import functions_of_pc
from geminiai import *



#defining the function
def said(text):
    buddy_speaker = win32com.client.Dispatch("SAPI.SpVoice")
    buddy_speaker.Speak(text)

def recognize_audio():
    au = sr.Recognizer()  #recognize the voice
    try:
        with sr.Microphone() as source_of_audio:   
            
            audio = au.listen(source_of_audio)
            result = au.recognize_google(audio,language="en-PK")
            print(f"The recognize voice is {result}")
            return result.lower()
    except:
        return "Some error occured sorry for inconvenience  !!"


def greeting():
    present_time = int(datetime.datetime.now().strftime("%H"))  #check the present time

    if 5<present_time<12:
        said("Good Morning Abdul Karim")   #checking the condition 
    elif 12<=present_time<16:
        said("Good Afternoon Karim")
    elif 16<=present_time<20:
        said("Good Evening Karim")
    else:
        said("Good Night Karim")

    said("I am Buddy AI. I am your Assisstant and I would always be here to help you...")


if __name__ =="__main__":
    greeting()
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

        #connecting with wikipedia  
        elif f"wikipedia" in audio:
            said("Searching on wikipedia.........")
            search = audio.split("wikipedia") #remove the wikipedia from the audio 
            result = search[-1] + "in only two sentence"
            
        #connecting with artificial intelligence
        elif  "using artificial intelligence" in audio:      #if you want to use artificial intelligence you must use the word "using artificial intelligencce"
            said("I am working on your data by using artificial intelligence")
            main_gimini(audio) 

        #for quitting the program 
        elif "quit" in audio:
            said("I am Quiting the program. Thanks for your time and in future if you need me you can call me, I would always be here to help you.")
            quit()
        