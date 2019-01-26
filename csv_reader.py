import csv

def readMyFile(filename):
    dict = {}
    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            key  = row[1]
            val = [row[0]] + row[2:]
            if dict.has_key(key):            
                dict[key].append(val)
            else:
                dict[key] = [val]
            
    return dict

dict = readMyFile('ITM_20190121.csv')

print(dict['1084067241'][0])
