from pickle import NONE
import pyttsx3
import time
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import shutil
import datetime
import subprocess
from ecapture import ecapture as ec
from database import get_ans_from_memory
from database import get_questions_and_answers

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    
def wishMe():
    
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif  hour>=12 and  hour<18:
        speak("Good afternoon!") 
    else:
        speak("Good evening!")
    speak("Its a lovely day! Welcome")
    speak("I am Your Personal Assistant. Please tell me Miss, How can I assist you??")    
def takeCommand():
    '''
    it takes microphone input from user and returns string output.
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)    
        
        print("Say that again please...")
        return "None"
    return query
 
def username():
    speak("What shall I call you?")
    uname = takeCommand()
    speak("Welcome")
    speak(uname)
    columns = shutil.get_terminal_size().columns
     
    print("-----------------".center(columns))
    print("Welcome Maam.", uname.center(columns))
    print("-----------------".center(columns))
     
if __name__ == "__main__":
    
    wishMe()
    #username()
    while(True):
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query =query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results) 
            
        elif 'open youtube' in query:
            speak('opening youtube..') 
            wb.open("youtube.com")   
            
        elif 'open google' in query:
            speak('opening google..') 
            wb.open("google.com")  
        
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
            
        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")                            
                
        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses.")         
                       
            
            
           
            
        elif "the time" in query:
            print(get_ans_from_memory("What is the time"))
            strTime = str(datetime.datetime.now().strftime("%H:%M:%S"))
            speak(f"Maam, the time is {strTime}")    
            print(strTime)
        elif  get_ans_from_memory(query)!="":
            speak (get_ans_from_memory(query)) 
            #print(get_ans_from_memory(query),"hi")
        else:
            speak("I don't understand Sorry")
            
