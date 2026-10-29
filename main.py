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
import json


url1 = "https://www.lacentrale.fr/listing?gearbox=MANUAL&makesModelsCommercialNames=TOYOTA%3A%3AVERSO&priceMax=3000&sortBy=priceAsc"
url2 = "https://www.leboncoin.fr/recherche?category=2&text=toyota%20verso&price=min-3000&regdate=2010-max&gearbox=1&u_car_brand=TOYOTA&u_car_model=TOYOTA_Verso&sort=price&order=asc"
url3 = "https://www.autolina.ch/fr/toyota/verso?price=-5000&sort=price_asc"
url4 = "https://www.autoscout24.ch/fr/s/mo-verso/mk-toyota?priceTo=3200&sort%5B0%5D%5Btype%5D=PRICE&sort%5B0%5D%5Border%5D=ASC"


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







""" options6 = uc.ChromeOptions()
drivers6 = uc.Chrome(
    options=options6,
    browser_executable_path="/usr/bin/chromium",
    version_main=154
)

drivers6.get(url3)

# Laisser le temps à la page de charger
time.sleep(5)

html3 = drivers6.page_source
drivers6.close()

soup3 = BeautifulSoup(html3, "lxml")



for script in soup3.find_all('script'):
    if script.string and 'prefetchedListings' in script.string:
        # Regex pour capturer uniquement le bloc JSON contenant les voitures
        # On cherche à partir de "prefetchedListings": { ... }
        pattern = r'"prefetchedListings":\s*(\{.*?\})\s*,\s*"topVehicles"'
        matches = re.search(pattern, script.string)
        
        if matches:
            json_str = matches.group(1)
            
            try:
                # On transforme la chaîne de texte en vrai dictionnaire Python
                data = json.loads(json_str)
                annonces = data.get("content", [])
                
                print(f"--- {len(annonces)} annonces trouvées ---")
                
                for voiture in annonces:
                    # Extraction des données structurées
                    titre = voiture.get("versionFullName", "Titre inconnu")
                    prix = voiture.get("price", "Prix inconnu")
                    km = voiture.get("mileage", "Kilométrage inconnu")
                    annee = voiture.get("firstRegistrationYear", "Année inconnue")
                    id_annonce = voiture.get("id", "")
                    
                    # Reconstruction de l'URL de l'annonce
                    lien = f"https://www.autolina.ch/fr/auto/toyota/verso/{id_annonce}" if id_annonce else "Lien indisponible"
                    
                    print(f"🚗 {titre}")
                    print(f"💰 {prix} CHF | 🛣️ {km} km | 📅 {annee}")
                    print(f"🔗 {lien}")
                    print("-" * 30)
                    
            except json.JSONDecodeError as e:
                print("Erreur de décodage JSON :", e)


optionA = uc.ChromeOptions()

drivers6= uc.Chrome(
    options= optionA,
    browser_executable_path="/usr/bin/chromium",
    version_main=154
)



drivers6.get(url3)

time.sleep(5)

html3=drivers6.page_source

drivers6.close()


soup3=BeautifulSoup(html3, "lxml")

ct=soup3.find_all("div", class_="make-model ng-tns-c75-33")

lst5=[]

for c in ct:
   lst5.append(c.get_text(strip=True))

print(lst5)



pr=soup3.find_all("div", class_="price ng-tns-c75-33")

lst5bis=[]

for p in pr:
   lst5.append(p.get_text(strip=True))

print(lst5bis)


cr=soup3.find_all("div", class_="vehicle-data ng-tns-c75-33")

lst5ter=[]

for c in cr:
   lst5.append(c.get_text(strip=True))

print(lst5ter)


lk=soup3.find_all("div", class_="url-wrapper tr-srp-item ng-tns-c75-33 with-filters")

lst55=[]

for l in lk:
   lst5.append("https://www.autolina.ch/"+l.get("href"))

print(lst55)


lstautolina=list(zip(lst5, lst5ter, lst5bis, lst55))

print(lstautolina)

rep = re.get(url3)
rep.raise_for_status()

soup3 = BeautifulSoup(rep.content, "lxml")

modeles = [
    c.get_text(strip=True)
    for c in soup3.find_all("div", class_="make-model ng-tns-c75-33")
]

prix = [
    p.get_text(strip=True)
    for p in soup3.find_all("div", class_="price ng-tns-c75-33")
]

caracteristiques = [
    c.get_text(strip=True)
    for c in soup3.find_all("div", class_="vehicle-data ng-tns-c75-33")
]

liens = [
    "https://www.autolina.ch/" + l.get("href", "").lstrip("/")
    for l in soup3.find_all(
        "div",
        class_="url-wrapper tr-srp-item ng-tns-c75-33 with-filters"
    )
]

# Vérifier que les sélecteurs renvoient le même nombre d'éléments
print(len(modeles), len(caracteristiques), len(prix), len(liens))

df3 = pd.DataFrame({
    "Modele": modeles,
    "Caracteristiques": caracteristiques,
    "Prix": prix,
    "Liens": liens,
})

print(df3) 


----------------> A reessayer plus tard/Blockage de haut niveau du webmaster"""




options3= uc.ChromeOptions()

driver3= uc.Chrome(
    options= options3,
    browser_executable_path="/usr/bin/chromium",
    version_main=154
)

driver3.get(url4)

time.sleep(5)

html4=driver3.page_source

driver3.close()


soup3=BeautifulSoup(html4, "lxml")

tr=soup3.find_all("h2", class_="css-kbu0wt")

lst6bis=[t.get_text(strip= True) for t in tr]



prx = soup3.find_all("p", class_="css-48bgog")

lst6 = []
for pz in prx:
    prix = pz.get_text(strip=True)
    prix=prix.replace("\xa0", " ")
    lst6.append(prix)



cr=soup3.find_all("p", "css-1crz6ir")

lst6ter=[c.get_text(strip= True, separator= " ") for c in cr]

lk= soup3.find_all("a", class_="css-cxjjkx")

lst66= ["https://www.autoscout24.ch"+l.get("href") for l in lk]


lstAutoscout=list(zip(lst4bis, lst6ter, lst6, lst66))

df3=pd.DataFrame(lstAutoscout, columns=["Modele", "Caracteristiques", "Prix", "Lien"])


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
            f"Nouvelle Toyota Verso!\n"
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


for _, x in df3.iterrows():
    liens=x["Lien"]
    if liens not in annonces_vues:
        nvxmsg = (
            f"Nouvelle Toyota Verso! \n",
            f"Modele : {x["Modele"]}\n",
            f"Caracteristiques: {x["Caracteristiques"]}\n",
            f"Prix: {x["Prix"]} \n",
            f"Lien: {x["Lien"]}\n"
        )
        envoyer_telegram(nvxmsg)
        with open (FICHIER_PILE, "a") as f:
            f.write(liens+ "\n")
            
    else:
        print("erreur doublon")


""" for _, x in df3.iterrows():
    lignes=x[""]


print(df3)

print(lstautolina)
 """

rep=re.get(url3)

print(lst6bis)

print(lst6)

print(lst6ter)

print(lst66)

print(df3)