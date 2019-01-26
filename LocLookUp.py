from urllib.request import urlopen
import requests

def read(latitude,longitude):
    url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key=AIzaSyBW5QZVpvnxWPcemecQBxhxZrjPjxB2bXU'.format(latitude,longitude)
    r = urlopen(url)
    
    json_data = requests.get(url).json()

    place = json_data['results'][0]['formatted_address']

    print(place)

read(49.15563,-123.0172)
