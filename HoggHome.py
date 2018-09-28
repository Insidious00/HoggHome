import speech_recognition as sr
from gtts import gTTS
import os
import urllib.request
import json

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


#vAmount = int(input("Enter an amount"))
#vFromCurrency = input("Enter the currency of this amount")
#vToCurrency = input("Enter a currency to change this to")

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source,timeout=3,phrase_time_limit=15)

try:
    print("Transcription: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Audio is unintelligable")
except sr.RequestError as e:
    print("cannot obtain results; [0]", format(e))

vAudio = r.recognize_google(audio)
vList = vAudio.split(" ")

Var1 = int(vList[3])
Var2 = str(vList[4])
Var3 = str(vList[6])


vFinal = (converter.convert(Var1, Var2, Var3))
print(vFinal)

vSay = (Var1, Var2, " is equal to ", vFinal, Var3)
vSay = str(vSay)

tts = gTTS(text=str(vFinal), lang='en')
tts.save("pcvoice.mp3")
os.system("start pcvoice.mp3")
