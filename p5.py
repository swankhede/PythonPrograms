import socket
import requests

try:
	socket.create_connection(("www.google.com",80))
	print("u r connected")
	city = input("enter city name: ")
	a1 = "http://api.openweathermap.org/data/2.5/weather?"

	a2 = "q=" +city + "&units=metric"
	a3 = "&APPID=fa531e4e62b7ffeb91c7ea854ddf347a"
	api_address = a1+a2+a3
	res1 = requests.get(api_address)
	print(res1)
	
	d = res1.json()
	print(d)
	d1=d['main']['temp']
	print("temperature =",d1)
	
	
except OSError as e:
	print("issue ",e)
	
