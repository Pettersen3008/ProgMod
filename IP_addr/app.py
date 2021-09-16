import socket
from ip2geotools.databases.noncommercial import DbIpCity

url = input('Skriv inn en ip eller url: ')
IP = socket.gethostbyname(url)
response = DbIpCity.get(IP, api_key='free')

print('IP: ', IP)
print('Contry: ', response.country)
print('City: ', response.city)
print('Region: ', response.region)
print('Latitude: ', response.latitude)
print('Longtude: ', response.longitude)