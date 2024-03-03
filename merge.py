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
            playsound('song.mp3')  # Updated to play 'song.mp3' instead of 'iris.mp3'
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

    elif 'search' in command:
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

    elif 'happy' in command:
        talk("oh i am glad to hear that, do you wanna party?")
        command=take_command()
        if 'yes' in command:
            command=take_command()
            talk('do you want me to play party music!')
            if 'yes' in command:
                talk("let's party")
                list=("Nain Ta Heere (Video) JugJugg Jeeyo","Beyoncé - BREAK MY SOUL","Drake - Falling Back","Eminem ft. CeeLo Green - The King And I","everything sucks")
                n = random.randint(0,4)
                pywhatkit.playonyt(list[n])
                command=take_command 
            else:    
                talk("keep smiling! you'r smile is beautiful")  
        else:
            talk("ok bye")     
    
    elif 'i am hungry' in command:
         talk("do you want to order food , or cook by yourself?") 
         command=take_command()
         if'order food' in command:
            talk("where do u want to order ?")
            command=take_command()
            if command!=None:
                talk('oops! you have not given me permissions to do that')
                talk('sorry i cannot help you with that')
                exit
         elif'cook by myself' in command :
            talk(" do u need any help? ") 
            command=take_command()
            if 'yes' in command:
                talk('name the recipe and i will search releated information for you!')
                command=take_command()
                if command!=None:
                    pywhatkit.playonyt(command)
            else:
                talk('i know you are good at cooking, if you need help let me know')        

    elif "fear" in command :
        talk("Im sorry to hear that. sometimes just breathe. if you can tell me what you're nervous about, I may be able to help you better.")
        command=take_command()   
        
        if "results" in command:
            talk("Thats very understandable. Exam stress is no joke if i can help by playing relaxing music, dont worry about ur results they are just numbers.")
        
        elif "exam" in command:
            talk("All the best for that. if you need me to set alarm just say the words")
            command=take_command()
                
            if "alarm" in command:
                talk("what time do u want me to set alarm")
                command=take_command()
                if command!=None:
                    talk('alarm set for '+command)  
                    

        elif "interview" in command :
            talk("It is normal to feel nervous before an interview. You have to let go of the fear. Think of this as an oppurtunity to dress up and talk about yourself. I hope this will help you relax a bit. if you need me to do anything like set an alarm or reminders please let me know.")
            command=take_command()

            if "alarm" in command:
                talk("what time do u want me to set alarm")
                command=take_command()
                if command!=None:
                    talk('alarm set for '+command)
            else:
                exit

        elif "relationship" in command:
            talk(" Having anxiety in a relationship is ok but on the other hand,  And you should not feel like your doing something wrong Maybe your just afraid to loose that person and so that's why your anxious either way its up to you to decide how the relationship is.")

        elif "stressed"  in command:
            talk(" Everyone gets anxious sometimes,but if your worries and fears are so constant that they interfere with your ability to function and relax, you may have generalized anxiety disorder.do you want suggestions on that")
            command=take_command()    
            if "yes" in command:
                talk(" Cognitive behavioural therapy (CBT) is one of the most effective treatments for GAD. Do you want me to read the full aricle")
                command=take_command()
                if 'yes' in command:
                    wikisearch=wikipedia.summary(format('Cognitive behavioural therapy'))
                    talk(wikisearch)
            else:
                exit

        elif "speaking in  public" in command:    
            talk(" Fear of public speaking is a very common reason to feel anxious. Here's some useful tips that may help:1, Practice your speech in front of a mirror. 2, Practice in front of your friends and family members. 3, When you get on to the stage take a long breathe that relieves your nervousness and keep you calm. 4, And deliver your prepared speech with confidence.")
                            
        elif "talk to stranger" in command:    
            talk(" Fear of talking of people. Did You know that this is one of the most common fear that people have. One of the solution is to talk yourself in front of a mirror. It develops self confidence in you.And don’t talk to impress others because they are nobody for you to impress")   

        elif "anxiety" in command: 
            talk("anxiety maybe caused due to a variety of reason. Here are some things you can try: 1, Exercise, 2, Meditation, 3, Relaxation exercises, including deep breathing, 4, Visualization, 5, Good sleep habits, 6, Healthy dietLearn interpersonal skills for dealing with difficult people and situations")
        
        else:
            talk("sorry i cannot help you with this problem. would you like to consult any doctors ?")
            command=take_command()
            if "yes"in command:
                talk("these ar the list of hospitals near you:")

            else:
                talk("Stay calm and take a deep breath, i feel bad for not having a answer for your problem!")    
                exit

    elif "sad" in command:
        list=("What's been going on in your life lately?","Want to talk? I'm here to listen.","What do you think is making you feel so bad right now?")
        n = random.randint(0,2)
        talk(list[n])
        command=take_command()
        print(command)
        
       
        if 'stress' in command:
            talk( "Are you drinking or using drugs to cope with the stress?")       
            talk("Are you getting between 7 and 9 hours of sleep each night?")
            command=take_command()
            if 'yes' in command:
                talk('hear is what i found on internet for overcoming stress!')
                pywhatkit.search("tips to reduce stress")
            else:
                talk('do you want me to schedule an appointment with a doctor')
                command=take_command()
                if 'yes' in command:
                    talk("these are the doctors that i found")
                    talk("116 Best Stress Management Counselling Doctors In Bangalore")
                   ### urllib.request.urlopen('https://www.practo.com/search/doctors?results_type=doctor&q=%5B%7B%22word%22%3A%22stress%20management%20counselling%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22service%22%7D%5D&city=Bangalore')

        elif 'break up' in command:   
            talk("Sorry about that, u have to move on, hope you find a better one!, I've some jokes for u, if you mant to hear them just tell me!") 
            command=take_command()
            if 'yes' or 'ok' in command:
                talk(pyjokes.get_joke())
                talk( "Some jokes might just put a smile on your face , Just say apple tell me a joke")
                command=take_command()
                if 'yes' or 'ok' or 'joke' in command:
                    talk(pyjokes.get_joke())
                else:
                    exit
            else:
                exit            

        elif 'failed' in command:   

            talk( "dont worry i'm here to cheer you up, every one fails one or the other time in life, take this as your new stone towards achiving your dreams")   
            talk("Here's some motivational videos i found on youtube") 
            list=("One of the Greatest Speeches Ever | Steve Jobs","Steve Harvey's Speech Will Make You Wake Up In Life And Take Action | Motivation","Advice to Young People And His Biggest Regret | Jack Ma | Goal Quest","Most Motivational Speech | Best Inspirational Speech by Sundar Pichai","Dr. APJ Abdul Kalam's Life Advice Will Change Your Future (MUST WATCH) Motivational Speech")
            n = random.randint(0,4)
            pywhatkit.playonyt(list[n])

        elif 'search' in command:
            command=take_command()
            if command!="no":
                pywhatkit.search(command)

        else:
             talk("i don't know what you mean by that, Do you want me to be a web search?") 
             command=take_command()
             if 'yes' in command:
                 talk('What do you want me to search')
                 command=take_command()
                 if command!="no":
                    pywhatkit.search(command)
                    
    elif 'get lost' in command:
        exit(0)

    else:
        talk('Please say the command again.')    

def face():
    face_classifier = cv2.CascadeClassifier(r'emotions.xml')
    classifier =load_model(r'model.h5')
    emotion_labels = ['angry','','fear','happy','neutral', 'sad', 'surprise']

    cap = cv2.VideoCapture(0)

    labels = []
    count=0
    while count <30:
        count+=1
        _, frame = cap.read()
        
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            roi_gray = gray[y:y+h,x:x+w]
            roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)

            if np.sum([roi_gray])!=0:
                roi = roi_gray.astype('float')/255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi,axis=0)

                prediction = classifier.predict(roi)[0]
                label=emotion_labels[prediction.argmax()]
                label_position = (x,y)
                cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                labels.append(label)
                print(labels)
                
            else:
                cv2.putText(frame,'No Faces',(30,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        
        cv2.imshow('Emotion Detector',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
   
    cap.release()
    cv2.destroyAllWindows()
    sc=max(set(labels), key = labels.count)
    bb=("you are "+sc)
    return bb

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