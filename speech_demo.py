from distutils import command
from email.mime import audio
from tkinter import NO
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import random
from playsound import playsound
import pyjokes
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def make():
    take_command()

def close():
    exit(0)

def take_command():
    r = sr.Recognizer()
    r.energy_threshold = 2000 
    microphone = sr.Microphone()
    try:  
        with microphone as source:
            playsound('song.mp3')  # Modified line: changed from 'iris.mp3' to 'song.mp3'
            audio = r.listen(source,timeout=1000)
            command = r.recognize_google(audio)
            command = command.lower()
            print(command)
        return command
    except sr.UnknownValueError:
            make()

def run_alexa(command):
    if ('search') in command:
        command=take_command()
        user_query = command

        URL = "https://www.google.co.in/search?q=" + user_query
        headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36'
        }
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        result = soup.find(class_='VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf').get_text()
        print(result)
        talk(result)

    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
 
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'information' in command:
          
        user_query = command
        URL = "https://www.google.co.in/search?q=" + user_query
        headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36'
        }
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        result = soup.find(class_='LC20lb MBeuO DKV0Md').get_text()
        print(result)
        talk(result)

    elif 'joke' in command:
        talk(pyjokes.get_joke())      

    elif 'happy' in command :
        talk("let's party ouuta soul ,do you want to have some beverages or hot drinks?") 
        command=take_command()
        if 'beverages' in command :
            talk("oh thanks for giving me information i will use it for future reference") 
        elif 'hot drinks' in command:
            talk("oh thanks for giving me information i will use it for future reference") 
        else:
            talk("bye")     
    # ... (rest of the function remains unchanged)

WAKE="iris"

while True:
    text=take_command()
    if text!=None:
        if text.count(WAKE) > 0:
            print("i am ready")  
            command=take_command()
            run_alexa(command)