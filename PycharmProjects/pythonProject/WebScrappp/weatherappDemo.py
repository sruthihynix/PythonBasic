import requests

from pprint import pprint
# pprint() function and print also has similar functionality.
# But the only difference is pprint-> prints complex data structures.

API_key = "8cefe843c62ddb5c677a3ad578145d74"
# API_key = "Your API key"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
# f=open('cityWeather','w')
city_name = input("Enter a city Name : ")
Final_url = base_url + "appid=" + API_key + "&q=" + city_name

weather_data = requests.get(Final_url).json()

print("\nCurrent Weather Data Of " + city_name + ":\n")
# pprint(weather_data)  # pprint print all the details about the weather inthe  given city
# x=weather_data
# f.write(x)
# f.close()
temp = weather_data['main']['temp'] # to print tempreature
print(temp)
