import csv_reader 
import datetime 
from urllib.request import urlopen
import requests

def time_warning(dictionary,truckID,i):
    result = dictionary[truckID][9][i].replace("-"," ").split()
    date = datetime.date(int(result[0]),int(result[1]),int(result[2]))
    if date.weekday()==0 or date.weekday()==4 or date.weekday()==5 or date.weekday()==6:
        return True
    return False

def acceleration_warning(dictionary,truckID,i):
    if dictionary[truckID][2][i]=="Acceleration":
        return True

def location_warning(dictionary, truckID, index):
    url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key=AIzaSyBW5QZVpvnxWPcemecQBxhxZrjPjxB2bXU'.format(dictionary[truckID][7][index],dictionary[truckID][8][index])
    r = urlopen(url)

    json_data = requests.get(url).json()

    place = json_data['results'][0]['formatted_address']
    place=place.replace(",","").split()
    if "Vancouver" in place or "Toronto" in place or "Montreal" in place or "Peel" in place:
        return True
    return False

