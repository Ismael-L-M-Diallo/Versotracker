import requests as re
import unittest
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import time
from bs4 import BeautifulSoup
import pandas as pd
import os
from dotenv import load_dotenv

url1 = "https://www.lacentrale.fr/listing?gearbox=MANUAL&makesModelsCommercialNames=TOYOTA%3A%3AVERSO&priceMax=3000&sortBy=priceAsc"
url2 = "https://www.leboncoin.fr/recherche?category=2&text=toyota%20verso&price=min-3000&regdate=2010-max&gearbox=1&u_car_brand=TOYOTA&u_car_model=TOYOTA_Verso&sort=price&order=asc"
url3 = "https://www.autolina.ch/fr/toyota/verso?price=-2000&sort=price_asc"
url4 = "https://www.autoscout24.ch/fr/s/mo-verso/mk-toyota?priceTo=2000&sort%5B0%5D%5Btype%5D=PRICE&sort%5B0%5D%5Border%5D=ASC"
url5 = "https://www.autolina.ch/fr/carList?price=-2000&sort=price_asc"
url6= "https://www.lacentrale.fr/listing?gearbox=MANUAL&makesModelsCommercialNames=TOYOTA%3A%3AVERSO&priceMax=10000&sortBy=priceAsc"


options = uc.ChromeOptions()

driver = uc.Chrome(
    options=options,
    browser_executable_path="/usr/bin/chromium",
    version_main=154  # Aligne le driver sur la version 154 de ton Chromium
)


driver.get(url1)

time.sleep(5)

html1=driver.page_source

driver.close()


soup = BeautifulSoup(html1, "lxml")


pp=soup.find_all("div", class_="Text_Text_text Text_Text_subtitle-large vehiclecardV2_vehiclePrice__En33S")

lst=[]

for p in pp:
    lst.append(p.get_text(strip=True))

print(lst[1:])


lst2=[]


tt0=soup.find_all("div", class_="vehiclecardV2_informationsContainer__wEUWL vehiclecardV2_informationsContainer__isRowFormat__NLhZT")

for t in tt0:
    lst2.append(t.get_text(strip=True, separator= " "))


print(lst2[1:])

lst3=[]


tt2=soup.find_all("H2", class_="Text_Text_text Text_Text_subtitle-medium Text_Text_bold vehiclecardV2_title__vc1e9")

for t in tt2:
    lst3.append(t.get_text(strip=True, separator= " "))


print(lst3[1:])

options2 = uc.ChromeOptions()

driver2 = uc.Chrome(
    options=options2,
    browser_executable_path="/usr/bin/chromium",
    version_main=154  # Aligne le driver sur la version 154 de ton Chromium
)


driver2.get(url2)

time.sleep(5)

html2=driver2.page_source

driver2.close()



soup2=BeautifulSoup(html2, "lxml")



pr2=soup2.find_all("p", class_="sr-only")

lst3=[]

for p in pr2:
    x=p.get_text(strip=True)
    y=x.replace("\u202f", "")
    y=y.replace("\xa0", "")
    lst3.append(y)

print(lst3)


url3= "https://www.autolina.ch/fr/toyota/verso?sort=price_asc"

rep=re.get(url3)

print(rep)

html3=rep.content

soup3=BeautifulSoup(html3, "lxml")

ct=soup3.find_all("div _ngcontent-serverapp-c75", class_="ng-tns-c75-17")

lst4=[]

for c in ct:
    c.get_text(strip= True)
    lst4.append

print(lst4)


options3= uc.ChromeOptions()

driver3= uc.Chrome(
    options= options3,
    browser_executable_path="/usr/bin/chromium",
    version_main=154
)

url4= "https://www.autoscout24.ch/fr/s/mo-verso/mk-toyota?sort%5B0%5D%5Btype%5D=PRICE&sort%5B0%5D%5Border%5D=ASC"

driver3.get(url4)

time.sleep(5)

html4=driver3.page_source

driver3.close()

soup3=BeautifulSoup(html4, "lxml")


pr=soup3.find_all("div", class_="css-1vv03rk")

lst4=[]

for p in pr:
    p.get_text(strip= True)
    lst4.append

print(lst4)


lstCentrale= list(zip(lst2[1:], lst[1:]))

print(lstCentrale)

df1=pd.DataFrame(lstCentrale, columns=["Characteristiques", "Prix"])

print(df1)

load_dotenv()

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise RuntimeError("token invalide")

CHAT_ID = -1003698921393

def envoyer_centrale(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message }
    requests.post(url, data=payload)

FICHIER_PILE="bd_anti-doublons.txt"

