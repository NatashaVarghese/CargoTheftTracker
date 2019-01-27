import csv_reader 
import datetime 

def time_warning(dictionary,truckID,i):
    result = dictionary[truckID][9][i].replace("-"," ").split()
    date = datetime.date(int(result[0]),int(result[1]),int(result[2]))
    if date.weekday()==0 or date.weekday()==4 or date.weekday()==5 or date.weekday()==6:
        return True
    return False

def acceleration_warning(dictionary,truckID,i):
    if dictionary[truckID][2][i]=="Acceleration":
        return True
