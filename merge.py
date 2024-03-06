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
    speak(text, "en", save=True, file='song.mp3', speak=True)

def take_command():
    r = sr.Recognizer()
    r.energy_threshold = 2000
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
        talk("hey!, my name is iris ,i'm your personnel assisstant,i would be handling your daily routines and be your secret admirer, virtually! ")

    elif 'search' in command:
        command = take_command()
        user_query = command

        URL = "https://www.google.co.in/search?q=" + user_query
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
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + current_time)

    elif 'information' in command:
        user_query = command
        URL = "https://www.google.co.in/search?q=" + user_query
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36'
        }
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        result = soup.find(class_='LC20lb MBeuO DKV0Md').get_text()
        print(result)
        talk(result)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    # ... (rest of the run_alexa function remains unchanged)

    else:
        talk('Please say the command again.')


def face():
    # ... (face function code remains unchanged)

    face_classifier = cv2.CascadeClassifier(r'emotions.xml')
    classifier = load_model(r'model.h5')
    emotion_labels = ['angry', '', 'fear', 'happy', 'neutral', 'sad', 'surprise']

    cap = cv2.VideoCapture(0)

    labels = []
    count = 0
    while count < 30:
        count += 1
        _, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype('float') / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)

                prediction = classifier.predict(roi)[0]
                label = emotion_labels[prediction.argmax()]
                label_position = (x, y)
                cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                labels.append(label)
                print(labels)

            else:
                cv2.putText(frame, 'No Faces', (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('Emotion Detector', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    sc = max(set(labels), key=labels.count)
    bb = ("you are " + sc)
    return bb


WAKE = "ola"

def talk1(text):
    engine1.say(text)

sca = face()
ccc = sca
tex = ("you are" + ccc)

if 'sad' in tex:
    talk('you are so sad today, can i know the reason ?')
elif 'happy' in tex:
    talk('you are so happy today, tell me y ?')
elif 'angry' in tex:
    talk('you look angry and serious, are u angry with me?')
else:
    talk('you dont have any expression are u human?')

while True:
    text = take_command()
    if text != None:
        if text.count(WAKE) > 0:
            print("i am ready")
            command = take_command()
            run_alexa(command)