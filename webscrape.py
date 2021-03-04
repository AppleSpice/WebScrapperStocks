import requests
from bs4 import BeautifulSoup
import pyrebase

import json
import sys

#pip install pyrebase4
#pip install requests
#pip install bs4
#pip install lxml




sys.stdout = open("Stock.txt", "w")

GMESource = requests.get('https://finance.yahoo.com/quote/GME?p=GME&.tsrc=fin-srch').text
TSLASource = requests.get("https://finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-srch").text
BESTSource = requests.get("https://finance.yahoo.com/quote/BEST?p=BEST&.tsrc=fin-srch").text

GMESoup = BeautifulSoup(GMESource, 'lxml')
TSLASoup = BeautifulSoup(TSLASource, 'lxml')
BESTSoup = BeautifulSoup(BESTSource, 'lxml')

GMEStock = GMESoup.find(class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").text
TSLAStock = TSLASoup.find(class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").text
BESTStock = BESTSoup.find(class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").text

#print(GMEStock)
#print(TSLAStock)
#print(BESTStock)

Prices = {
	"GME": GMEStock,
	"TSLA": TSLAStock,
	"BEST": BESTStock
}

PricesJSON = json.dumps(Prices)

print(PricesJSON)
####################################
firebaseConfig={'apiKey': "AIzaSyC35YsYOpc39pFYIEW-CF5fz1qLXz0PtzY",
    'authDomain': "stockpricetracker-9bea8.firebaseapp.com",
    'databaseURL': "https://stockpricetracker-9bea8-default-rtdb.firebaseio.com",
    'projectId': "stockpricetracker-9bea8",
    'storageBucket': "stockpricetracker-9bea8.appspot.com",
    'messagingSenderId': "370504356378",
    'appId': "1:370504356378:web:ac97eac490cadb3e9d77a3",
    'measurementId': "G-P4DNY76G07"}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

db.push(Prices)



#https://www.youtube.com/watch?v=s-Ga8c3toVY
#https://www.youtube.com/watch?v=rKuGCQda_Qo THIS IS OLD