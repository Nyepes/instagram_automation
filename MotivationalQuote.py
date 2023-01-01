import requests
class MotivationalQuote:
    def getQuote():
        res = requests.get('https://zenquotes.io/api/quotes')
        return res.json()
