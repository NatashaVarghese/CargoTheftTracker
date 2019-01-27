import csv_reader 
import datetime 
#import requests
#from urllib.request import urlopen

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
	if dictionary[truckID][7][index] == "NULL":
		return False
        if dictionary[truckID][7][index]>=43.65 and dictionary[truckID][7][index]<=43.66 and  dictionary[truckID][8][index]>=-79.39 and dictionary[truckID][8][index]<=-79.38:
            print("Toronto")
            return True
        if dictionary[truckID][7][index]>=45.50 and dictionary[truckID][7][index]<=45.51 and  dictionary[truckID][8][index]<=-79.55 and dictionary[truckID][8][index]>=-79.56:
            print("Montreal")
            return True
        if dictionary[truckID][7][index]>=49.26 and dictionary[truckID][7][index]<=49.27 and dictionary[truckID][8][index]<=-123.12 and dictionary[truckID][8][index]>=-123.11:
            print("Vancouver")
            return True

#	url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key=AIzaSyBW5QZVpvnxWPcemecQBxhxZrjPjxB2bXU'.format(dictionary[truckID][7][index],dictionary[truckID][8][index])
#	r = urlopen(url)
#	json_data = requests.get(url).json()
#	place = json_data['results'][0]['formatted_address']
#	place=place.replace(",","").split()
#	if "Vancouver" in place or "Toronto" in place or "Montreal" in place or "Peel" in place:
#		return True
#	return False
