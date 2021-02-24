from bs4 import BeautifulSoup
import requests
import json
import sys

sys.stdout = open("Stock.txt", "a")

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