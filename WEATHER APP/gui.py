import requests
import json
import pyttsx3
import tkinter as tk

def get_weather():
    city = city_entry.get()
    url=f"https://api.weatherapi.com/v1/current.json?key=1222493bdef340d087a170512231312&q={city}"

    r = requests.get(url)
    wdic = json.loads(r.text)
    temp = wdic["current"]["temp_c"]
    result_label.config(text=f"Current temperature in {city} is {temp} degree Celsius")
    
    engine = pyttsx3.init()
    x = f"Current temperature in {city} is {temp} degree Celsius"
    engine.say(x)
    engine.runAndWait()

# Creating the GUI window
root = tk.Tk()
root.title("Weather App")

city_label = tk.Label(root, text="Enter the name of the city:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
