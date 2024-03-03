from crypt import methods
from flask import Flask, render_template, request, session, jsonify, url_for, redirect
from distutils import command
from email.mime import audio
from tkinter import NO, Label, PhotoImage
from pyparsing import actions, re
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
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle
import os
import pyautogui
import keyboard as k
from googletrans import Translator as Trans
from gtts import gTTS

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

app = Flask(__name__)

@app.route('/')
def display():
    return render_template('mindex.html')

def talk1(text):
    engine.say(text)
    engine.runAndWait()

def talk(text):
    speak(text, 'en', save=True, file='song.mp3', speak=True)

def take_command():
    r = sr.Recognizer()
    r.energy_threshold = 2400
    microphone = sr.Microphone()
    try:
        with microphone as source:
            playsound('iris.mp3')
            audio = r.listen(source, timeout=1000)
            command = r.recognize_google(audio)
            command = command.lower()
            print(command)
        return command
    except sr.UnknownValueError:
        return take_command()

def run_alexa(command):
    print(command)
    if 'who are you' in command:
        talk("hey!, my name is iris, I'm your personal assistant, I would be handling your daily routines and be your secret admirer, virtually!")

    elif 'search' in command:
        command = take_command()
        command = command.replace("search", "")

        URL = "https://www.google.co.in/search?q=" + command
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36'
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
    # ... (face function remains unchanged)

if __name__ == '__main__':
    app.run()

sca = face()
ccc = sca

tex = ("you are" + ccc)

if 'sad' in tex:
    talk('you are so sad today, can I know the reason?')

elif 'happy' in tex:
    talk('you are so happy today, tell me why?')

elif 'angry' in tex:
    talk('you look angry and serious, are you angry with me?')

else:
    talk('you dont have any expression, I hope you are fine')

while True:
    text = take_command()
    if text != None:
        if text.count(WAKE) > 0:
            print("I am ready")
            command = take_command()
            run_alexa(command)