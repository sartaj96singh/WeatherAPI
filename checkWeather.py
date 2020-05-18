import requests

api_key = ''
api_address='http://api.openweathermap.org/data/2.5/weather?appid=' + api_key + '&q='
city = input('City Name :')
url = api_address + city
json_data = requests.get(url).json()
format_add = json_data['main']['temp']
description = json_data['weather'][0]['description']
fahrenheit = (format_add * 9/5 - 459.67)

print('It is going to be %s in %s' % (description, city))
print('The current temp in %s is %.2f degree Fahrenheit' % (city, fahrenheit))
print('Enjoy this time!')
