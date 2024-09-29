import requests
import tkinter as tk
from tkinter import ttk
import tkintermapview as tkmap
TK_SILENCE_DEPRECATION=1


url = "http://api.open-notify.org/iss-now.json"

lat = ""
long = ""
timestamp = ""
window = tk.Tk()
window.geometry("900x600")
window.title("ISS Tracker")

LAT = tk.StringVar()
LONG = tk.StringVar()
TIME = tk.StringVar()

label1 = ttk.Label(window, textvariable=LAT)
label1.place(x=150, y=20)

label2 = ttk.Label(window, textvariable=LONG)
label2.place(x=300, y=20)

label3 = ttk.Label(window, textvariable=TIME)
label3.place(x=450, y=20)

map = tkmap.TkinterMapView(window, width=800, height=500)
map.place(x=50, y=50)
map.set_zoom(4)
marker1 = map.set_marker(0.0, 0.0)

def getCoordinates():
    global marker1, map
    response = requests.get(url)
    data = response.json()
    lat = data ["iss_position"]["latitude"]
    long = data ["iss_position"]["longitude"]
    timestamp = data["timestamp"]
    map.set_position(float(lat),float(long))
    marker1.delete()
    marker1 = map.set_marker(float(lat),float(long))
    LAT.set("Latitude: " + lat)
    LONG.set("Longitude: "+ long)
    TIME.set("Timestamp:" + str(timestamp))
    window.after(2000, getCoordinates)


window.after(10, getCoordinates)
window.mainloop()


