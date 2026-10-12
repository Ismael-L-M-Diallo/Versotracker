import requests as re
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

url1 = "https://www.lacentrale.fr/listing?gearbox=MANUAL&makesModelsCommercialNames=TOYOTA%3A%3AVERSO&priceMax=3000&sortBy=priceAsc"
url2 = "https://www.leboncoin.fr/recherche?category=2&text=toyota%20verso&price=min-3000&regdate=2010-max&gearbox=1&u_car_brand=TOYOTA&u_car_model=TOYOTA_Verso&sort=price&order=asc"
url3 = "https://www.autolina.ch/fr/toyota/verso?price=-2000&sort=price_asc"
url4 = "https://www.autoscout24.ch/fr/s/mo-verso/mk-toyota?priceTo=2000&sort%5B0%5D%5Btype%5D=PRICE&sort%5B0%5D%5Border%5D=ASC"
url5 = "https://www.autolina.ch/fr/carList?price=-2000&sort=price_asc"


rep1 = re.get(url1)

print(rep1)

html= rep1.content

soup = bs(html, "lxml")

print (soup)


nm= soup.find_all("span", class_="ng-tns-c104-6")

print(nm)

lst=[]

for n in nm:
    ntxt=n.getText(strip=True)
    lst.append(ntxt)

print(lst)