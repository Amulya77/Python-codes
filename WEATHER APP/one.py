import requests
import json

import pyttsx3


city=input("Enter the name of the city: ")

url=f"https://api.weatherapi.com/v1/current.json?key=1222493bdef340d087a170512231312&q={city}"

r=requests.get(url)

#print(r.text)
# print(type(r.text))
wdic=json.loads(r.text)
print(wdic["current"]["temp_c"])

engine = pyttsx3.init()
x=f"Current temperature in {city} is {wdic['current']['temp_c']} degree celsius"
engine.say(x)
engine.runAndWait()