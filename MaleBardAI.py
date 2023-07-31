#######################################################################################################################

import speech_recognition as sr
import pyaudio
import pyttsx3
import datetime as dt
from datetime import date, timedelta
#import pywhatkit as kit
import wikipedia as wiki
import webbrowser as wb
from plyer import notification
from bs4 import BeautifulSoup
import requests
import pyjokes
import json
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import calendar
from tkinter import *
from collections import namedtuple
from lxml import html
#import sounddevice as sd
#from scipy.io.wavfile import write
import wavio as wv
import  playsound
import sys as sy
import turtle
import os
import pytz
import random as rd
#from diction import translate
from translate import Translator
from sys import platform
import smtplib
import os
import socket
import sys
import pyjokes
import psutil
import pyautogui
import smtplib
from requests import get
from bs4 import BeautifulSoup
from gtts import gTTS
from playsound import playsound
#import ecapture as ec
import  wolframalpha
import time
######################################################################################################################

import pyttsx3
import speech_recognition as sr
from bardapi import Bard
import os


###################################################
# Set up the text-to-speech engine
# engine = pyttsx3.init()
# engine.setProperty('rate', 150)
#####################################################
# ###############################################
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')                                            # Female Voices
engine.setProperty('voice', voices[0].id)
# ################################################
# Create a speech recognition object
recognizer = sr.Recognizer()

# Set the Bard API key
os.environ["_BARD_API_KEY"] = "ZAgjFKYCAghEXJynj79i9qJr0qhAt8urVrNVnCKA3ApQkCwdrJtH_eVLUmcUY2TVO22rJg."

# Define a function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello, how are you, sir?")




def wishMe():
    speak("Welcome back! Sir")
    print(" ")
    hour = int(dt.datetime.now().hour)
    year = int(dt.datetime.now().year)
    month =(dt.datetime.now().strftime("%B-%m"))
    date = (dt.datetime.now().strftime("%A-%d"))

    #UTC = pytz.utc
    #IST = pytz.timezone('Asia/kolkata')

    Time = dt.datetime.now().strftime("%I:%M:%S %p")
    cur_date = dt.datetime.now().strftime("%d. %m. %Y, %A")
    print("Date", cur_date)
    speak("Sir Today Date is")
    speak(cur_date)

    print("This Time Now", Time)
    speak("the current Time Now is")
    speak(Time)

    speak('Sir  You are Village Today Weather')
    city = 'rangapuram'
    apiKey = '591a35045c6de641dae242c118676369'
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=metric')
    x = response.json()
    if x["cod"] != "404":
        y = x['main']
        temperature = x['main']["temp"]
        pressure = x['main']["pressure"]
        humidity = x['main']["humidity"]
        desc = x["weather"][0]["description"]
        weather_detail = f'Sir Current temperature is {temperature}, pressure is {pressure} hPa, humidity is {humidity} %, Weather condition is {desc}'
        print(weather_detail)
        speak(weather_detail)


    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!  Hope your day is filled with joy and happiness.")

    elif hour > 1 and hour < 15:
        speak("Good Afternoon! Sir")

    elif hour >= 15 and hour < 19:
        speak("Good Evening! Sir")

    elif hour >= 19 and hour < 24:
        speak("Good Night! Sir now, and rest. Today was a test, You passed it, you’re past it. Now breathe till unstressed")


    #else:


    speak("Bard at your service! Please tell me how can I help you? Sir")


wishMe()









def reply(question):
    prompt = f'Sriram: {question}\n Jarvis: '
    response = Bard().get_answer(prompt)
    answer = response['content']
    return answer

# Define a function to listen for speech and convert it to text
def takeCommand():
    with sr.Microphone() as source:
        print("Listening...")
        speak('I am listening....')
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print("Sriram Said: {}\n".format(query))
        return query
    except Exception as e:
        print("Please say that again, sir...")
        speak('Please say that again, sir...')
        return "None"

while True:
    query = takeCommand()
    if query is not None and query.lower() == "exit":
        break
    else:
        response = reply(query)
        print("Jarvis: {}\n".format(response))
        speak(response)


################################################################################################################