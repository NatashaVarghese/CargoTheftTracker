from urllib.request import urlopen
import csv_reader
import requests

def location_warnings(dictionary, truckID, index):
    url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key=AIzaSyBW5QZVpvnxWPcemecQBxhxZrjPjxB2bXU'.format(dictionary[truckID][7][index],dictionary[truckID][8][index])
    r = urlopen(url)

    json_data = requests.get(url).json()

    place = json_data['results'][0]['formatted_address']
    place=place.replace(",","").split()
    print(place)
    if "Vancouver" in place or "Toronto" in place or "Montreal" in place or "Peel" in place:
        return True
    return False
        

#print(location_warnings(csv_reader.readMyFile("ITM_20190121.csv"),"1088217019",i))
