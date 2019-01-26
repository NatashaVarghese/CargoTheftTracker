#!/usr/bin/python
import requests

latitude = input("Lat: ")
longitude = input("Long: ")
url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + latitude + "," + longitude + "&key=AIzaSyBW5QZVpvnxWPcemecQBxhxZrjPjxB2bXU"

json_data = requests.get(url).json()

place = json_data['results'][0]['formatted_address']

print(place)

input("")