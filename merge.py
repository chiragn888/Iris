from cProfile import run
from distutils import command
from email.mime import audio
from tkinter import NO
from pyparsing import re
import speech_recognition as sr
import pyttsx3
import pywhatkit
import urllib.request
import datetime
import wikipedia
from sys import argv
import random
from playsound import playsound
from text_to_speech import speak
import pyjokes
import requests
import multiprocessing
import time
from bs4 import BeautifulSoup
from keras.models import load_model
from time import sleep
from keras.utils import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

engine1 = pyttsx3.init()
voices = engine1.getProperty('voices')
engine1.setProperty('voice', voices[1].id)

def talk(text):
    speak(text,"en",save=True,file='song.mp3', speak=True)

def take_command():
    r = sr.Recognizer()
    r.energy_threshold = 2000 
    microphone = sr.Microphone()
    try:  
        with microphone as source:
            playsound('iris.mp3')
            audio = r.listen(source,timeout=1000)
            command = r.recognize_google(audio)
            command = command.lower()
            print(command)
        return command
    except sr.UnknownValueError:
            take_command()

def run_alexa(command):
    print(command)
    
    if 'who are you' in command:
        talk("hey!, my name is iris ,i'm your personnel assisstant,i would be handling your daily routines and be your secret admirer, virtually! ")    
    # ... (rest of the function remains unchanged)

def face():
    # ... (rest of the function remains unchanged)

WAKE="ola"

def talk1(text):
    engine1.say(text)

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
        talk('you dont have any expression are u human?')    

while True:  
    text=take_command()
    if text!=None:
     if text.count(WAKE) > 0:
        print("i am ready")  
        command=take_command()
        run_alexa(command)