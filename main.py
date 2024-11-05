from opencage.geocoder import OpenCageGeocode
from tkinter import *

def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language = "ru")
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lan = round(results[0]['geometry']['lng'], 2)
            return f"широта: {lat}, долгота: {lan}"
        else:
            return "Город не найден"
    except Exception as e:
        return f"Возникла ошибка: {e}"

def show_coordinates(event = None):
    city = entry.get()
    coordinates = get_coordinates(city, key)
    label.config(text = f"Координаты города {city}: \n {coordinates}")

key = 'c3626e750a6d4b9fa2df917627e3a783'

window = Tk()
window.title("Координаты городов")
window.geometry("400x350")

entry = Entry()
entry.pack()
entry.bind("<Return>", show_coordinates)

button = Button( text ="Поиск координат", command = show_coordinates)
button.pack()

label = Label(text = "Введите город и нажмите на кнопку")
label.pack()

window.mainloop()