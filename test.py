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

print(converter.convert(1.0, "EUR", "USD"))
print(converter.convert(1.0, "USD", "EUR"))
print(converter.convert(1.0, "CAD", "GBP"))
print(converter.convert(1.0, "CAD", "EUR"))

                            
