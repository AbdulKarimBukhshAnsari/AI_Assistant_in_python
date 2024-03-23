#importing packages

import speech_recognition as sr   #to recognize the words
import win32com.client  
import webbrowser                 #handling web activities        

#defining the function
def said(text):
    buddy_speaker = win32com.client.Dispatch("SAPI.SpVoice")
    buddy_speaker.Speak(text)

def recognize_audio():
    au = sr.Recognizer()
    try:
        with sr.Microphone() as source_of_audio:
            audio = au.listen(source_of_audio)
            result = au.recognize_google(audio,language="en-PK")
            print(f"The recognize voice is {result}")
            return result
    except:
        return "Some error occured sorry for inconvenience  !!"

        

if __name__ =="__main__":
    said("Hello Karim How are you..I am Buddy Your assisstant I would always be here to help you.")
    print("listening...")
    audio =recognize_audio().lower()
    #my social account
    social_account = [["facebook","https://www.facebook.com/kareem.ansari.3939"],
                      ["linkedin","https://www.linkedin.com/in/abdul-karim-bukhsh-ansari-56b0292b3"],
                      ["gmail","https://mail.google.com/mail/u/0/#inbox"]]
    for account in social_account:
        if f"open my {account[0]} account" in audio:
            said(f"opening your {account[0]} accounty.")
            webbrowser.open(account[1])

    #All websites

    websites = [
    ["facebook", "https://www.facebook.com"],
    ["instagram", "https://www.instagram.com"],
    ["twitter", "https://twitter.com"],
    ["linkedin", "https://www.linkedin.com"],
    ["youtube", "https://www.youtube.com"],
    ["reddit", "https://www.reddit.com"],
    ["pinterest", "https://www.pinterest.com"],
    ["tumblr", "https://www.tumblr.com"],
    ["snapchat", "https://www.snapchat.com"],
    ["whatsapp", "https://www.whatsapp.com"],
    ["google", "https://www.google.com"],
    ["amazon", "https://www.amazon.com"],
    ["ebay", "https://www.ebay.com"],
    ["netflix", "https://www.netflix.com"],
    ["twitch", "https://www.twitch.tv"],
    ["wikipedia", "https://www.wikipedia.org"],
    ["yahoo", "https://www.yahoo.com"],
    ["bing", "https://www.bing.com"],
    ["apple", "https://www.apple.com"],
    ["microsoft", "https://www.microsoft.com"]
]
    for site in websites:
        if f"open {site[0]}" in audio:
            said(f"Opening {site[0]}")
            webbrowser.open(site[1])
    
    

    