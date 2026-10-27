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
from urllib.parse import urljoin


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



base_url = "https://www.lacentrale.fr/"
lst1 = []

for a in soup.find_all("a", href=True):
    href = a["href"]
    if "auto-occasion-annonce" in href:
        lst1.append(urljoin(base_url, href))



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



pr2 = soup2.find_all(
    "div",
    class_="text-callout text-on-surface leading-sz-20! flex flex-wrap items-center font-bold"
)

lst4 = []

for p in pr2:
    texte = p.get_text(strip=True)
    texte = texte.replace("\u202f", "").replace("\xa0", "")
    lst4.append(texte)

print(lst4)

lst4bis=[]

titres = soup2.find_all("p", class_="text-body-1-highlight text-on-surface line-clamp-(--line-clamp) text-ellipsis group-hover/adcard:text-main-variant transition-colors duration-300 ease-in-out")


for t in titres:
    lst4bis.append(t.get_text(strip=True))

lst4ter=[]

carac= soup2.find_all("div", class_="f399Ya_lightParams text-body-2 text-on-surface inline-flex flex-wrap items-baseline mt-sm")

for c in carac:
    lst4ter.append(c.getText(strip= True, separator= " "))

lst44 = []
liens_vus = set()

base_url2 = "https://www.leboncoin.fr"
link = soup2.find_all("a", href=True)

for l in link:
    href = l["href"]
    if "/ad/voitures/" in href:
        url = urljoin(base_url2, href)
        if url not in liens_vus:
            lst44.append(url)
            liens_vus.add(url)




rep=re.get(url3)

print(rep)

html3=rep.content

soup3=BeautifulSoup(html3, "lxml")

ct=soup3.find_all("div _ngcontent-serverapp-c75", class_="ng-tns-c75-17")

lst5=[]

for c in ct:
    c.get_text(strip= True)
    lst5.append

print(lst5)


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

lst6=[]

for p in pr:
    p.get_text(strip= True)
    lst6.append

print(lst6)


lstCentrale= list(zip(lst2[1:], lst[1:], lst1[1:]))

print(lstCentrale)

df1=pd.DataFrame(lstCentrale, columns=["Characteristiques", "Prix", "Lien"])

print(df1)

print(lst1)

load_dotenv()

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise RuntimeError("token invalide")

CHAT_ID = -1003698921393

def envoyer_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message }
    re.post(url, data=payload)

FICHIER_PILE="bd_anti-doublons.txt"

if not os.path.exists(FICHIER_PILE):
    with open(FICHIER_PILE, "w") as f:
        pass

with open(FICHIER_PILE, "r") as f:
    annonces_vues=f.read().splitlines()


for _, x in df1.iterrows():
    link= x["Lien"]
    if link not in annonces_vues:
        nv_message = (
            f"Nouvelle Toyota Verso !\n "
            f"{x['Characteristiques']}\n"
            f"Prix : {x['Prix']}\n"
            f"Lien : {link}"
            )
        envoyer_telegram(nv_message)
        with open(FICHIER_PILE, "a") as f:
            f.write(link+ "\n")

    else:
        print("error")

print(lst4)
print(lst4bis)
print(lst4ter)
print(lst44)

lstBC=list(zip(lst4bis, lst4ter, lst4, lst44))

print(lstBC)

df2=pd.DataFrame(lstBC, columns=["Titre", "Caracteristiques", "Prix", "Lien"])

print(df2)

for _, x in df2.iterrows():
    liens=x["Lien"]
    if liens not in annonces_vues:
        nv_mssage=(
            f"Nouvelle Toyota Verso\n"
            f"{x["Titre"]}\n"
            f"Prix: {x["Prix"]}\n"
            f"Caracteristiques: {x["Caracteristiques"]}\n"
            f"Lien: {liens}\n"
        )

        envoyer_telegram(nv_mssage)

        with open(FICHIER_PILE, "a") as f:
            f.write(liens+"\n")

    else:
        print("Erreur doublon")