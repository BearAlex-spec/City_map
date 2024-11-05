from opencage.geocoder import OpenCageGeocode


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

key = 'c3626e750a6d4b9fa2df917627e3a783'
city = "Люберцы"
coordinates = get_coordinates(city, key)
print(f"Координаты города {city}: {coordinates}")