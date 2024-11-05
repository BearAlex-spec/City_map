from opencage.geocoder import OpenCageGeocode
from tkinter import *
import webbrowser

result = ""
def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language = "ru")
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lan = round(results[0]['geometry']['lng'], 2)
            country = results [0]["components"]["country"]
            name_val = results[0]["annotations"]["currency"]["name"]
            osm_url = f"https://www.openstreetmap.org/?mlat={lat}&mlon={lan}"

            if "state" in results[0]["components"]:
                region = results[0]["components"]["state"]
                return {
                    "coordinates": f"широта: {lat}, долгота: {lan} \n Страна: {country} \n Валюта: {name_val} \n Регион: {region}",
                "map_url": osm_url
                        }
            else:
                return {
                    "coordinates": f"широта: {lat}, долгота: {lan} \n Страна: {country} \n Валюта: {name_val}",
                "map_url": osm_url
                        }
        else:
            return "Город не найден"
    except Exception as e:
        return f"Возникла ошибка: {e}"

def show_coordinates(event = None):
    global map_url

    city = entry.get()
    result = get_coordinates(city, key)
    label.config(text = f"Координаты города {city}: \n {result["coordinates"]}")
    map_url = result["map_url"]


def clear_entry():
    label.config(text = "Введите город и нажмите на кнопку")
    entry.delete(0, END)


def show_map():
    if map_url:
        webbrowser.open(map_url)

key = 'c3626e750a6d4b9fa2df917627e3a783'
map_url = ""

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

map_button = Button(text = "Показать карту", command = show_map)
map_button.pack()

button_clear = Button (text = "Очистить поле ввода", command = clear_entry)
button_clear.pack()

window.mainloop()