import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk

url = "https://weather.com/en-IN/weather/today/l/8942645b881fd43fc86ed2d932370e550513245460cabb6a48b38a3089406d92"
master = Tk()
master.title("Weather App")
master.config(bg = "white")

def getWeather():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    location = soup.find('h1',class_="CurrentConditions--location--1Ayv3").text
    temperature = soup.find('span', class_="CurrentConditions--tempValue--3KcTQ").text
    weatherPrediction = soup.find('div', class_="CurrentConditions--phraseValue--2xXSr").text

    locationLabel.config(text=location)
    temperatureLabel.config(text=temperature)
    weatherPredictionLabel.config(text=weatherPrediction)
    temperatureLabel.after(60000,getWeather)
    master.update()

locationLabel = Label(master, font=("Calibri bold", 20),bg="white")
locationLabel.grid(row=0, sticky="W", padx=40)
temperatureLabel = Label(master, font=("Calibri bold", 70), bg="white")
temperatureLabel.grid(row=1, sticky="W", padx=40)
weatherPredictionLabel = Label(master, font=("Calibri bold", 15), bg="white")
weatherPredictionLabel.grid(row=2, sticky="W", padx=40)

getWeather()
master.mainloop()
