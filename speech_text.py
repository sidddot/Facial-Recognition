import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import pyttsx3


def get_audio():
    r=sr.Recognizer();
    with sr.Microphone() as source:
        audio=r.listen(source)
        said=""
        try:
            said=r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception "+str(e))
    return said
text=get_audio()
if "delivery" in text:
    text_speech = pyttsx3.init()
    text_speech.say("Please keep delivery at the doorstep")
    text_speech.runAndWait()