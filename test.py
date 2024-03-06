from cProfile import run
from distutils import command
from email.mime import audio
from tkinter import NO, Label, PhotoImage
from pyparsing import re
import speech_recognition as sr
import pyttsx3
import pywhatkit
import urllib.request
import datetime
import time
import wikipedia
from sys import argv
import pyautogui
import random
import keyboard as k
from googletrans import Translator as Trans   
from gtts import gTTS
from playsound import playsound
from text_to_speech import speak
import pyjokes
from cgitb import text
from playsound import playsound as PS 
import requests
import multiprocessing
from bs4 import BeautifulSoup
from keras.models import load_model
from time import sleep
from keras.utils import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle
from PIL import Image       
import os          
from googletrans import Translator
from text_to_speech import speak

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('voice', voices[0].id)

def talk1(text):
    engine.say(text)
    engine.runAndWait()

def talk(text):
    speak(text,'en',save=True,file='song.mp3', speak=True)

def take_command():
    r = sr.Recognizer()
    r.energy_threshold = 2000 
    microphone = sr.Microphone()
    try:  
        with microphone as source:
            playsound('song.mp3')  # Modified line: Replaced 'iris.mp3' with 'song.mp3'
            audio = r.listen(source, timeout=1000)  # Added line to capture audio
            command = r.recognize_google(audio)     # Added line to recognize speech
            print(command)
        return command
    except sr.UnknownValueError:
            take_command()

def run_alexa(command):
    print(command)
    
    if 'who are you' in command:
        talk("hey!, my name is iris ,i'm your personnel assisstant,i would be handling your daily routines and be your secret admirer, virtually! ")    

    elif 'search' in command:
        command=take_command()
        command=command.replace("search"," ")

        URL = "https://www.google.co.in/search?q=" + command
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

    # ... (rest of the run_alexa function remains unchanged)

def face():
    # ... (face function code remains unchanged)

WAKE="ola"

sca=face()
ccc=sca

tex=("you are"+ccc)

if 'sad' in tex:
    talk('you are so sad today, can i know the reason ?')

elif 'happy' in tex:
    talk('you are so happy today, tell me y ?')

elif 'angry' in tex:
    talk('you look angry and serious, are u angry with me?')

else:
    talk('you dont have any expression i hope you are fine?')

while True:
    text=take_command()
    if text!=None:
        if text.count(WAKE) > 0:
            print("i am ready")
            command=take_command()
        elif 'later' in text:
            print("i will check back on you later, bye")   
            talk("i will check back on you later, bye")  
            exit(0)