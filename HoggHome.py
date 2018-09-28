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


vAmount = int(input("Enter an amount"))
vFromCurrency = input("Enter the currency of this amount")
vToCurrency = input("Enter a currency to change this to")

vFinal = (converter.convert(vAmount, vFromCurrency, vToCurrency))
print(vFinal)

vSay = (vAmount, " in ", vFromCurrency, " is equal to ", vFinal, " in ", vToCurrency)
vSay = str(vSay)

tts = gTTS(text=str(vFinal), lang='en')
tts.save("pcvoice.mp3")
os.system("start pcvoice.mp3")




                            
