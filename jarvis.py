import pyttsx3    #library that will help us to convert text to speech
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from pathlib import Path
import pyautogui


engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices')      #getting details of current voice

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()     #Without this command, speech will not be audible to us.


def wishme():
     hour = int(datetime.datetime.now().hour)
     if hour>=0 and hour<12:
         speak("Good Morning!")
     elif hour>=12 and hour<18:
         speak("Good Afternoon")
     else:
         speak("Good evening")


def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    file_path = Path(r"C:\Users\aishw\OneDrive\Desktop\password.txt")
    f = open(file_path,'r')
    p=f.read()
    server.login('satrao207@gmail.com', p)   #'enable the less secure apps' feature in your Gmail account
    server.sendmail('satrao207@gmail.com', to, content)
    server.close()

if __name__=="__main__":
    speak("hello sathwika")
    #while True:
    if 1:
         query=takeCommand().lower()

         if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed

             speak('Searching Wikipedia...')
             query = query.replace("wikipedia", "")
             results = wikipedia.summary(query, sentences=2)
             speak("According to Wikipedia")
             print(results)
             speak(results)
             """
             webbrowser.open(wikipedia)
             """


         elif "open youtube" in query:
             webbrowser.open("youtube.com")

         elif "open google" in query:
             webbrowser.open("google.com")

         elif 'the time' in query:
             strTime = datetime.datetime.now().strftime("%H %M %S")
             speak(f"the time is {strTime}")

         elif "open file" in query:
             #used to open any file in our system
             path="C:\\Users\\aishw\\OneDrive\\Desktop\\Suvisha"  #path of the file we want to open
             os.startfile(path)    #opening the file using os module startfile method


         elif 'email' in query:
             try:
                 speak("What should I say?")
                 content = takeCommand()
                 to = "sathwika.kesani2007@gmail.com"
                 sendEmail(to, content)
                 speak("Email has been sent!")
             except Exception as e:
                 print(e)
                 speak("Sorry. I am not able to send this email")

         elif 'screenshot' in query:
             image = pyautogui.screenshot()
             image.save('screenshot.png')
             speak('Screenshot taken.')

         """elif 'open website' in query:
             url = 'https://pythonexamples.org'
             webbrowser.register('chrome',
                                 None,
                                 webbrowser.BackgroundBrowser(
                                     "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
             webbrowser.get('chrome').open(url)"""



                 #elif "exit" in query:
           #  exit()


