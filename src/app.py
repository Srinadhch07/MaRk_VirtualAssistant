import calendar
from datetime import datetime
import google.generativeai as genai
from os import name,system
from getpass import getpass
import webbrowser
import time
from  random import *
import  os
import ast
import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
import datetime
import sys
from sys import platform
import pyjokes
import cv2
import subprocess


# Resurces allocation


webbrowser.register("termux-open '%s'",None)
news=["https://www.eenadu.net/latest-news",
"https://timesofindia.indiatimes.com/home/headlines",
"https://www.bbc.com/news/world"]
listen_tech=["https://youtube.com/@TEDx",
"https://youtube.com/@Prasadtechintelugu",
"https://youtube.com/@telugutechhafiz",]
listen_music=["https://youtube.com/@7clouds",
"https://youtube.com/@TseriesTelugu",
"https://youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ",
"https://youtube.com/@SonyMusicIndia",
"https://youtube.com/@lofimusicchannel3935"]
listen_news=["https://youtube.com/@etvtelangana",
"https://youtube.com/@BBCNews",
"https://youtube.com/@V6NewsTelugu"]

recognition_failure = [
    "Sorry, I didn't catch that. Can you please rephrase your request?",
    "I didn't understand what you said. Could you repeat it slowly?",
    "There seems to be some background noise. Can you speak a little louder?",
    "Hmm, that wasn't clear. Would you like to try again?",
    "I need a little more information. Can you rephrase your question?",
    "Give that another shot. I'm ready when you are.",
    "Is there anything else I can help you with?",
    "Would you like to try typing your request instead?",
    "My ears are a bit fuzzy today. Can you say that again?",  # Lighthearted
    "Seems like the gremlins are messing with my microphone. Try again?",  # Playful
    "Uh oh, gotta reboot my circuits. Speak up after I'm ready!",  # Informal
]

late_responses = [
    "I'm on it! This might take a few seconds.",
    "Just digging up that information for you. Stay tuned.",
    "Searching for the answer. I'll get back to you shortly.",
    "Hold on a sec, I'm thinking!",  # Informal
    "Sure thing! Give me a moment to crunch some numbers.",
    "Don't blink, I'm almost there!",  # Informal
    "Processing your request. Please wait a moment.",
    "I'm currently retrieving the information. I'll let you know as soon as it's available.",
    "Thank you for your patience. I'll have an answer for you shortly.",
    "Making good progress! Should be ready in a few seconds.",
    "Looks like this might take a bit longer. Is there anything else I can help you with in the meantime?"
]


goodbye_responses = [
    "Goodbye, Sir. Have a productive day.",
    "It was a pleasure assisting you, Sir. Please don't hesitate to call upon me again.",
    "Thank you for using my services, Sir. Until next time.",
    "See you later, Sir! Have a good one.",
    "Alright Sir, catching you later.",
    "Off you go, Sir! Don't be a stranger.",  # Use with caution
    "Is there anything else I can help you with today, Sir?",
    "Standing by, Sir. Let me know if you need anything else.",
    "At your service, Sir. Don't hesitate to call.",
    "Don't forget about me, Sir! I'll be here waiting patiently.",  # Playful
    "Farewell, Sir! May your day be filled with efficiency and success!",  # Slightly exaggerated
    "Bummer! But hey, duty calls. Until next time, Sir!",  # Informal
]

greeting_responses = {
    "greetings": {
        "initial": [
            "How can I be of service today?",
            "Welcome, Sir! It's a pleasure to assist you.",
            "Hello, Sir! Ready to tackle your day? Let me know how I can help.",
        ],
        "returning": [
            "Welcome back, Sir! Glad to see you again.",
            "At your service again, Sir. What can I do for you today?",
            "Ready to pick up where we left off, Sir? Just let me know.",
            "Did you have a productive break, Sir? Anything I can help with now?"  # If Sir has been away for a while
        ]
    }
}



genai.configure(api_key="AIzaSyD9a47SJ5kKfmMKpX8A2c5ox_CsYp_E52o")
    # Set up the model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
    }

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    ]

model = genai.GenerativeModel(
        model_name="gemini-1.0-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

convo = model.start_chat(history=[])



#Setting up speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#Speech function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Command method
def command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak anything ...")
        speak("I'm listening Sir")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        #sr.pause_threshold=1
        audio = recognizer.listen(source,timeout=5)
        print("listen completed...")
        try:
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
            return text
        except sr.UnknownValueError:
            print("Mark : Could not understand audio")
            speak(choice(recognition_failure))
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Methods to Finalize the MArk

def clear():
    if name=="nt":
        _=system('cls')
    if name=='posix':
        _=system('clear')
def calculator():
        try:
            speak("Enter the your Math Expression")
            value=eval(input("Mark : Enter Expression\nYOU\t: "))
            speak(f"The answer is {str(value)}")
            print("Mark : SOLUTION :",value,"\n")
        except:
            print("Mark : Invalid Expression.")
def chrome():
    speak("Opening Chrome ")
    os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
def cmd():
    speak("Opening Command prompt")
    os.system("start cmd")

def notepad():
    speak("Opening Notepad")
    os.startfile("C:\\Windows\\System32\\notepad.exe")

def calculator():
    speak("Opening Calculator")
    os.startfile("C:\\Windows\\System32\\calc.exe")
def browser():
        webbrowser.register("termux-open '%s'",None)
        speak("What would you like to search sir.")
        url=command()
        #url = input("Search : ")
        webbrowser.open_new("https://www.google.com/search?q="+url)


# Main Mark Project starts

class Mark:
    def __init__(self) -> None:
        if platform == "linux" or platform == "linux2":
            self.chrome_path = '/usr/bin/google-chrome'

        elif platform == "darwin":
            self.chrome_path = 'open -a /Applications/Google\\ Chrome.app'

        elif platform == "win32":
            self.chrome_path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
        else:
            print('Unsupported OS')
            exit(1)
        webbrowser.register(
            'chrome', None, webbrowser.BackgroundBrowser(self.chrome_path)
        )
        time=int(datetime.datetime.now().hour)
        if time >=0 and time < 12:
            speak("Good Morning sir")
            greet=['initial']
        elif time >=12 and time < 18:
            speak("Good Afternoon sir")
            greet=['returning']
        else:
            speak("Good Evening sir")
            
        speak("I'm Mark version 1.0,"+choice(greeting_responses["greetings"]["returning"]))
        

    def wfile(self,response_cache):
        with open("cloud.txt","w+") as f1:
         data=str(response_cache)
         wf1=f1.write(data)
    def database_setup(self):
            with open("cloud.txt","a+") as f4:
                a=os.stat("cloud.txt").st_size
                if a==0:
                    response_cache={}
                    self.wfile(response_cache)
                    pass
                else:
                    pass
            #print("Mark :", choice(greeting_responses))
            #speak(choice(greeting_responses))
    def Execute(self):
            #prompt=input("You : ")
            prompt=command()
            if prompt is None:
                return
            #prompt=input("\nYou\t: ")
            prompt=prompt.lower()
            query=prompt.lower()
            #while "shut your mouth" not in prompt and "play music" not in prompt and "exit" not in prompt and "open news" not in prompt and "listen news" not in prompt and "play music on youtube" not in prompt and "clear the screen" not in prompt and "open calculator" not in prompt and "open notepad" not in prompt:
             
                 
            if prompt=="history":
                    with open("cloud.txt",'r') as f:
                        rf=f.read()
                        rdic=ast.literal_eval(rf)
                        rdic=rdic.keys()
                        rdic=list(rdic)
                        rdic.reverse()
                        count=1
                        print("Mark :")
                        for i in rdic:
                            print(count," - ",i,"\n")
                            count+=1     
            elif "exit" in query or "shut your mouth" in query or "turn off" in query or 'shut down' in query or 'shutdown' in query:
                speak(choice(goodbye_responses)+"This is Mark Version 1.0 Signing Off")
                sys.exit()       
            elif "open news" in prompt:
                new=webbrowser.open_new_tab(choice(news))
            elif "listen news" in prompt and "news" in prompt:
                new=webbrowser.open_new_tab(choice(listen_news))
            elif "play music on youtube" in prompt and "music" in prompt and "youtube" in prompt:
                new=webbrowser.open_new_tab(choice(listen_music))
            elif prompt=="listen tech" or prompt== "l tech":
                new=webbrowser.open_new_tab(choice(listen_tech))
            
            elif "clear the screen" in query and "screen" in query:
                clear()
                speak("Sir, I had cleared the screen. Anything else to do ?")
            elif "open" in query and 'calculator' in query:
                calculator()
            elif "open" in query and 'notepad' in query:
                notepad()
            elif 'close ' in query and 'chrome' in query:
                speak("Okay sir closing chrome")
                os.system("taskkill /f /im chrome.exe")

            elif "chrome"  in query:
                speak("Searching on google"+choice(late_responses))
                query=query.replace("chrome","")
                webbrowser.open_new("https://www.google.com/search?q="+query)

            elif "open youtube" in query:
                speak("Opening Youtube sir")
                webbrowser.open_new("https://www.youtube.com/")
            elif "open facebook" in query:
                speak("Opening Facebook")
                webbrowser.open_new("https://www.facebook.com/")           

            elif "open" in query and 'instagram' in query:
                speak("opening instagram")     
                webbrowser.open_new("https://www.instagram.com/")      

            elif "open" in query and 'twitter' in query:
                speak("Opening Twitter")     
                webbrowser.open_new("https://x.com/home")
            elif "open whatsapp" in query and 'twitter' in query:
                speak("Opening whatsapp")
                webbrowser.open_new("https://web.whatsapp.com/")
                

            elif "open browser" in query and "browser" in query:
                browser()
            elif "open " in query and "command prompt" in query or "open cmd" in query :
                cmd()
            
            elif "open" in query and "calculator" in query:
                calculator()
            
            elif "joke" in query:
                joke = pyjokes.get_joke()
                print("Mark :",joke)
                speak(joke)
            elif "open camera" in query or "camera" in query:
                cap =cv2.VideoCapture(0)
                while True:
                    ret,img=cap.read()
                    cv2.imshow('webcam',img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break
                cap.release()
                cv2.destroyAllWindows()
            elif "play" in query and "youtube" not in query and "music" in query:
                speak("Playing songs")
                dir='F:\\Music'
                songs=os.listdir(dir)
                rd=choice(songs)
                #for song in songs:
                if rd.endswith('.mp3'):
                        os.startfile(os.path.join(dir,rd))
            elif "close music" in query or 'stop music' in query or "stop" in query and "music" in query:
                speak("Okay sir closing Music player")
                os.system("taskkill /f /im Microsoft.Media.Player.exe")

            elif "wikipedia" in query:
                speak("searching in wikipedia"+choice(late_responses))
                query=query.replace("wikipedia","")
                results=wikipedia.summary(query,sentences=2)
                speak('From Wikipedia')
                speak(results)
            
            elif 'sleep' in query:
                speak(" Okay sir I am taking break now")
                sys.exit()

            elif "my" in query and 'name' in query:
                speak("Your name is SRINADH and you are 21 years old boy sir.")
            
            elif 'your' in query and 'name' in query:
                speak("This is Mark version 1.0")
            
            elif "shutdown" in query or "shut down" in query and 'system' in query:
                speak("Yes sir, I am shutting down the system in 5 seconds")
                time.sleep(5)
                os.system("shutdown /s /t 0")
            
            elif "restart" in query and 'system' in query:
                speak("Yes sir, I am restarting the system in 5 seconds")
                time.sleep(5)
                subprocess.run(["shutdown", "/r", "/t", "0"])
            elif "close" in query and "notepad" in query:
                speak("Okay sir closing Notepad")
                os.system("taskkill /f /im notepad.exe")

            elif "close" in query and 'command prompt' in query:
                speak("Okay sir closing cmd")
                os.system("taskkill /f /im cmd.exe")

            elif "close visual studio" in query or 'close vs code' in query:
                speak("Okay sir closing visual studio")
                os.system("taskkill /f /im code.exe")


            elif "close all apps" in query or 'close' in query and 'all' in query and 'apps' in query:
                speak("Okay sir closing visual studio")
                os.system("taskkill /f /im cmd.exe")
                #os.system("taskkill /f /im explorer.exe")
                os.system("taskkill /f /im Microsoft.Media.Player.exe")
                os.system("taskkill /f /im chrome.exe")
                os.system("taskkill /f /im notepad.exe")
            elif 'voice' in query:
                if 'female' in query:
                    engine.setProperty('voice', voices[1].id)
                else:
                    engine.setProperty('voice', voices[0].id)
                speak("Hello Sir, I have switched my voice. How is it?")
            elif 'open' in query and 'vs code' in query:
                if platform == "win32":
                    os.startfile(
                        "C:\\Users\\gs935\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
                elif platform == "linux" or platform == "linux2" or "darwin":
                    os.system('code .')
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f'Sir, the time is {strTime}')

            elif 'remember' in query and 'me' in query:
                speak("what should i remember sir")
                rememberMessage = command()
                speak("you said me to remember"+rememberMessage)
                remember = open('data.txt', 'w')
                remember.write(rememberMessage)
                remember.close()

            elif 'do you remember anything' in query or 'forgetting' in query and 'anything' in query:
                remember = open('data.txt', 'r')
                speak("you said me to remember that" + remember.read())

            
            
            
            else:
                #speak('I am Connected to internet')
                with open("cloud.txt","r") as f2:
                    rf2=f2.read()
                    #dictioanry  read from file
                    rdic=ast.literal_eval(rf2)
                    if prompt in rdic and prompt!="clear":
                            print("Mark :",rdic[prompt])
                            speak(rdic[prompt])
                            
                    elif prompt!="edit" and prompt!="change":
                        if prompt not in rdic:
                            try:
                                #speak(choice(late_responses))
                                convo.send_message("Your  my personal assistant. Your job is to answer all my questions in a friendly mannar and make the answer is simple (3 lines) for below query:\n "+prompt)
                                response=str(convo.last.text)
                                filtered_response=response.replace("**","||")
                                
                                #print("Mark :",filtered_response)
                                speak(filtered_response)
                            except:
                                print("Mark : I'm sorry the prmopt you have entered is violating safety measures.")
                                rdic[prompt]=response
                                self.wfile(rdic)
                                


# MaRk initialization

if __name__ == "__main__":
    start=Mark()
    start.database_setup()
    while True:
        start.Execute()