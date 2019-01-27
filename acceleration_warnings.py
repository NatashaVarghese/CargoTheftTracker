import csv_reader 

def acceleration_warnings(dictionary,truckID,index):
    if dictionary[truckID][2][index]=="Acceleration":
        return True
    return False            


