import requests

api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=681129093360f287882497921529c3af&q='
city = input("City name?: ")

url = api_address + city

json_data = requests.get(url).json()
formatted_clouds = json_data['weather'][0]['description']
formatted_temp = json_data['main']['temp']

celsius = (formatted_temp - 273.15)
celdec = "%.2f" % celsius

fahrenheit = ((formatted_temp * (9 / 5)) - 459.67)
fahdec = "%.2f" % fahrenheit

temppref = input("Do you want temperature in C or F?: ")
temppref = temppref.upper()

print("The weather calls for", formatted_clouds)
if temppref == 'C':
    print("The temperature is:", celdec, "degrees Celsius")
elif temppref == 'F':
    print("The temperature is:", fahdec, "degrees Fahrenheit")