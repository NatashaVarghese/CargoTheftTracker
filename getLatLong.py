import csv_reader 

def latlong(dictionary,truckID):
    for i in range(len(dictionary[truckID][7])):
        print(dictionary[truckID][7][i])
        print(dictionary[truckID][8][i])

latlong(csv_reader.readMyFile('ITM_20190121.csv'),'1084067241') 

