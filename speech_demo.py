MODIFIED CODE:

```python
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
        make()


def run_alexa(command):
    if ('search') in command:
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
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

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

    elif 'happy' in command:
        talk("let's party ouuta soul ,do you want to have some beverages or hot drinks?")
        command = take_command()
        if 'beverages' in command:
            talk("oh thanks for giving me information i will use it for future reference")
        elif 'hot drinks' in command:
            talk("oh thanks for giving me information i will use it for future reference")
        else:
            talk("bye")

    elif 'my day was good' in command:
        talk("why don't you enjoy your night by going out for some candle light dinner with your soulmate")

    elif 'how awesome am i' in command:
        talk("you get motivated everytime when good things happen to you , keep up the good work going , i am always there with you virtually , just wake me up")

    elif 'i am hungry' in command:
        talk("do you want to order food , or cook by yourself?")
        command = take_command()
        if 'order food' in command:
            talk('oops! you have not given me permissions to do that')
            talk('sorry i cannot help you with that')
            exit
        elif 'cook by myself' in command:
            talk(" do u need any help? ")
            command = take_command()
            if 'yes' in command:
                talk('name the recipe and i will search releated information for you!')
                command = take_command()
                if command != None:
                    pywhatkit.playonyt(command)
            else:
                talk('i know you are good at cooking, if you need help let me know')

    elif "i am nervous" in command:
        talk("Im sorry to hear that. sometimes it helps just to breathe.if you can tell me what you're nervous about, I may be able to help you better.")
        command = take_command()

        if "i am nervous about my exam" in command:
            talk("Thats very understandable. Exam stress is no joke if i can help by playing relaxing music or setting reminders to study, just let me know.")

        elif "i have exam tomorrow" in command:
            talk("All the best for that. if you need me to look up something for you or set any alarms just say the words")
            command = take_command()
            if "search" in command:
                talk("")
            elif "alarm" in command:
                talk("what time do u want me to set alarm")
                command = take_command()
                if command != None:
                    talk('alarm set for ' + command)
            else:
                exit

        elif "interview" in command:
            talk("It is normal to feel nervous before an interview. You have to let go of the fear. Think of this as an oppurtunity to dress up and talk about yourself. I hope this will help you relax a bit. if you need me to do anything like set an alarm or reminders please let me know.")
            command = take_command()

            if "alarm" in command:
                talk("what time do u want me to set alarm")
                command = take_command()
                if command != None:
                    talk('alarm set for ' + command)
            else:
                exit

        elif "relationship" in command:
            talk(" Having anxiety in a relationship is ok but in the other hand no because if you have anxiety that means you feel like your doing something wrong. And you should not feel like your doing something wrong Maybe your just afraid to loose that person and so that's why your anxious either way its up to you to decide how the relationship is.")

        elif "stressed" in command:
            talk(" Everyone gets anxious sometimes,but if your worries and fears are so constant that they interfere with your ability to function and relax, you may have generalized anxiety disorder.do you want suggestions on that")
            command = take_command()
            if "yes" in command:
                talk(" Cognitive behavioural therapy (CBT) is one of the most effective treatments for GAD. Do you want me to read the full aricle")
                command = take_command()
                if 'yes' in command:
                    wikisearch = wikipedia.summary(format('Cognitive behavioural therapy'))
                    talk(wikisearch)

            else:
                exit

        elif "speaking in public" in command:
            talk(" Fear of public speaking is a very common reason to feel anxious. Here's some useful tips that may help:1, Practice your speech in front of a mirror. 2, Practice in front of your friends and family members. 3, When you get on to the stage take a long breathe that relieves your nervousness and keep you calm. 4, And deliver your prepared speech with confidence.")

        elif "speaking to stranger" in command:
            talk(" Fear of talking of people. Did You know that this is one of the most common fear that people have. One of the solution is to talk yourself in front of a mirror. It develops self confidence in you.And don’t talk to impress others because they are nobody for you to impress")

        elif "prevent anxiety" in command:
            talk("anxiety maybe caused due to a variety of reason. Here are some things you can try:1,Exercise,2,Meditation,3,Relaxation exercises, including deep breathing,4,Visualization,5,Good sleep habits,6,Healthy dietLearn interpersonal skills for dealing with difficult people and situations")
        else:
            talk("sorry i cannot help you with this problem. would you like to consult any doctors ?")
            command = take_command()
            if "yes" in command:
                talk("these ar the list of hospitals near you:")

            else:
                talk("Stay calm and take a deep breath, i feel bad for not having a answer for your problem!")
                exit

    elif "sad" in command:
        list = ("What's been going on in your life lately?", "Want to talk? I'm here to listen.", "What do you think is making you feel so bad right now?")
        n = random.randint(0, 2)
        talk(list[n])
        command = take_command()
        print(command)
        if 'headache' in command:
            talk("Are you getting between 7 and 9 hours of sleep each night?")
        elif 'stress' in command:
            talk("Are you drinking or using drugs to cope with the stress?")
        elif 'lonely' in command:
            talk("im sorry that you are feeling that way , if you want me to call someone just ask!!")

        elif 'break' in command:
            talk("Sorry about that, u have to move on, hope you find a better one!, I've some jokes for u, if you mant to hear them just tell me!")
            command = take_command()
            if 'yes' or 'ok' in command:
                talk(pyjokes.get_joke())
                talk("Some jokes might just put a smile on your face , Just say apple tell me a joke")
                command = take_command()
                if 'yes' or 'ok' or 'joke' in command:
                    talk(pyjokes.get_joke())
                else:
                    exit
            else:
                exit

        elif 'failed' in command:
            talk("dont worry i'm here to cheer you up, every one fails one or the other time in life, take this as your new stone towards achiving your dreams")

        elif 'ball' in command:
            talk("Here's some happy music from youtube")
            list = ("Baarishein", "Woh Raat", "Jaan Nisaar", "Khush to Hai Na", "Bin Tere - Reprise")
            n = random.randint(0, 4)
            pywhatkit.playonyt(list[n])

        elif 'search' in command:
            command = take_command()
            if command != None and command != "no":
                soup = BeautifulSoup(pywhatkit.search(command), "html.parser")
                talk(soup.title.text)
        else:
            talk("i don't know what you mean by that, Do you want me to be a web search?")
            command = take_command()
            if 'yes' in command:
                talk('What do you want me to search')
                command = take_command()
                if command != None and command != "no":
                    soup = BeautifulSoup(pywhatkit.search(command), "html.parser")
                    talk(soup.title.text)

    elif 'get lost' in command:
        close()

    else:
        talk('Please say the command again.')


WAKE = "iris"

while True:
    text = take_command()
    if text != None:

        if text.count(WAKE) > 0:
            print("i am ready")
            command = take_command()
            run_alexa(command)
```