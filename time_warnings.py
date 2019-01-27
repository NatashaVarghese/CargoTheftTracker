import csv_reader 
import datetime 

def time_warnings(dictionary,truckID,entry):
    for i in range(len(dictionary[truckID][9])):
        if dictionary[truckID][0][i]==entry:
            result = dictionary[truckID][9][i].replace("-"," ").split()
            date = datetime.date(int(result[0]),int(result[1]),int(result[2]))
            if date.weekday()==0 or date.weekday()==4 or date.weekday()==5 or date.weekday()==6:
                return True
            return False
        
    
print(time_warnings(csv_reader.readMyFile('ITM_20190121.csv'),'1088217019','920007354'))

