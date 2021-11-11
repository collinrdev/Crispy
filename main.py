#Crispy Projecttt
#Authors: Isiah Stevens, Collin Rittschof
#Special thanks: EVANGELOS

import tkinter as tk
import urllib.request
import json
#Grabs IP geolocation data from a website and stores it ina dictionary
with urllib.request.urlopen("https://geolocation-db.com/json") as url:
    data = json.loads(url.read().decode())
#print(data)

#spool up GUI
window = tk.Tk()
window.title("How Crisp Are You?")
window.geometry("320x96")


#Pulls values from data and stores them in variables
longitude = data.get('longitude')
latitude = data.get('latitude')
ip = data.get('IPv4')

#prints longitude, latitude and IPv4 address
#coordinates = "Longitude:",longitude, "Latitude:", latitude
ipText = "IPv4: " + ip
coordText = "Longitude:" + str(longitude) + " Latitude: " + str(latitude)


#function to convert latitude to percent distance from the prime miridian
percent = ((abs(latitude) / 180) * 100) - 100
crisp = abs(round(percent,1))
chip = 100 - crisp
#print("You are:",crisp, "% Crisp")
#print("You are:",chip, "% Chip")
crispText = "You are: " + str(crisp) + "% Crisp"
chipText = "You are: " + str(chip) + "% Chip"

#output text to the GUI
greeting4 = tk.Label(text = coordText)
greeting3 = tk.Label(text = ipText)
greeting = tk.Label(text = crispText)
greeting2 = tk.Label(text = chipText)

greeting4.pack()
greeting3.pack()
greeting.pack()
greeting2.pack()

#window.mainloop()
#longitude_to_percent(latitude)

