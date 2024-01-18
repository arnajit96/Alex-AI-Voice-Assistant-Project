import pyttsx3  # import text to speech
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time


#Speech to Text
def sptext(): 
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data           
        except sr.UnknownValueError:
            print("Not Understood")
# sptext()

# #Text to Speech
def speechtx(x): 
    engine= pyttsx3.init()
    voices= engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)  #voices[0] means male voice and voices[1] means female voice
    rate=engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()
# speechtx("hello Welcome to Jervis Project")


if __name__ =='__main__':
    if "hey alex" in sptext().lower():
        while True:
                data1=sptext().lower() 

                if "your name" in data1: 
                    name="My name is Alex"
                    speechtx(name)
                
                elif "how old are you" in data1:
                    age="I am twenty seven years old"
                    speechtx(age)

                elif 'now time' in data1: 
                    time = datetime.datetime.now().strftime("%I%M%p")
                    speechtx(time)
                
                elif 'open youtube' in data1: 
                    webbrowser.open("https://www.youtube.com/")

                elif 'open whatsapp' in data1: 
                    webbrowser.open("https://www.whatsapp.com/")
            

                elif 'open gmail' in data1: 
                    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
                
                elif "open joke" in data1:
                    joke_1 =pyjokes.get_joke(language="en",category="neutral")
                    print(joke_1)
                    speechtx(joke_1)
                
                
                elif "play song" in data1: 
                    add="C:\\Users\\lenovo\\Music"
                    listsong=os.listdir(add)
                    print(listsong)
                    os.startfile(os.path.join(add,listsong[0]))
                
                
                elif "exit" in data1: 
                    speechtx("thank you")
                    break
                        
                # time.sleep(10)
    else: 
        print("thanks")


   
        



        
        

              




