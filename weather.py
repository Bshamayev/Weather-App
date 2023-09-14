#Brian Shamayev
#Weather App
import requests
import config

def getCoords():
    city = input("Enter City: ")
    state = input("Enter State: ")
    country = input("Enter Country: ")

    base_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit=1&appid={config.appid}"
    response = requests.get(base_url)
    data = response.json()
    latitude = data[0]['lat']
    longitude = data[0]['lon']
    return latitude,longitude

def getWeather(lat, lon):
    base_url =  f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid={config.appid}"
    response = requests.get(base_url)
    data = response.json()
    temperature = data['main']['temp']
    return temperature

def main():
    lat,lon = getCoords()
    temperature = getWeather(lat,lon)
    print("Temperature: " + str(temperature))


if __name__ == "__main__":
    main()
