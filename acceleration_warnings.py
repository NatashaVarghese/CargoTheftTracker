import csv_reader 

def acceleration_warnings(dictionary,truckID,entry):
    for i in range(len(dictionary[truckID][2])):
        if dictionary[truckID][2][i]=="Acceleration" and dictionary[truckID][0][i]==entry:
            return True
            

print(acceleration_warnings(csv_reader.readMyFile('ITM_20190121.csv'),'1088214013','922454770'))

