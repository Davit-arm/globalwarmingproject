from bs4 import BeautifulSoup
import requests
import pandas as pd
import random 
import string
from urls import fact_text, vid1, vid2, vid3, vid4, url, url2 , url3
from TTOKEN import api_key


def gb():
    response = requests.get(url) 
    bs = BeautifulSoup(response.text,"lxml")
    definition = bs.find('p', class_='topic-paragraph').text
    return definition


def ef():
    response = requests.get(url2) 
    bs = BeautifulSoup(response.text,"lxml")
    temp = bs.find('ul', 'wp-block-list')
    paragraphs = temp.find_all('li')
    rand = random.choice(paragraphs).text
    return rand

def vd():
    videos = random.choice([vid1, vid2, vid3, vid4])
    return videos

def pl():
    facts = random.choice(fact_text)
    return facts

def gp(length):
    elements = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(elements) for _ in range(length))
    return password


def fc():
    flip = random.randint(0, 2)

    if flip == 0:
        return "heads"
    else:
        return "tails"
def api(cities):  
    
    for city in cities:
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
        res = requests.get(url).json()

    try:
        temp = res['current']['temp_c']
        condition = res['current']['condition']['text']
        info = f"**{city.title()}**\n🌡 {temp}°C\n☁️ {condition}"
    except:
        info = f"**couldnt get weather info about `{city}`"

    return info
