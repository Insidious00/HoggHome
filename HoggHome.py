#importing External Libraries

import speech_recognition as sr
from gtts import gTTS
import os
import urllib.request
import json

#Defining the functions for conversion

class CurrencyConverter:

    rates = []
    
    def __init__(self,url):
        req = urllib.request.Request(url)
        data = urllib.request.urlopen(req).read()
        data = json.loads(data.decode('utf-8'))
        self.rates = data["rates"]

    def convert(self,amount, from_currency, to_currency):
        initial_amount = amount
        if from_currency != "EUR":
            amount = amount / self.rates[from_currency]
        if to_currency == "EUR":
            return initial_amount, from_currency, '=', amount, to_currency
        else:
            return initial_amount, from_currency, '=', amount * self.rates[to_currency], to_currency

converter = CurrencyConverter("http://data.fixer.io/api/latest?access_key=4202c616ed8a0df8ee176544488d5560")

#Voice Recognition

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source,timeout=3,phrase_time_limit=15)
#voice transcription
try:
    print("Transcription: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Audio is unintelligable")
except sr.RequestError as e:
    print("cannot obtain results; [0]", format(e))

#Seperating data from string of (audio)

vAudio = r.recognize_google(audio)
vList = vAudio.split(" ")

#setting Data from (Audio) to variables

Var1 = int(vList[3])
Var2 = str(vList[4].upper())
Var3 = str(vList[6].upper())

#Converting variables in functions

vFinal = (converter.convert(Var1, Var2, Var3))
print(vFinal)

#Creating/ executing MP3 File

tts = gTTS(text=str(vFinal), lang='en')
tts.save("pcvoice.mp3")
os.system("start pcvoice.mp3")


                            
