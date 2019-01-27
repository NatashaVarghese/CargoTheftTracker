import csv
import operator

def readMyFile(filename):
    dict = {}
    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)

        sortedList = sorted(csvReader,key=operator.itemgetter(13))

        next(csvReader,None)    #for getting rid of header file

        for row in sortedList:

            # key is the Device Serial
            # value is [ID                   (0),
            #           Vin                  (1),
            #           MessageType          (2),
            #           ReportType           (3),
            #           MsgNum               (4),
            #           TripState            (5),
            #           ReceivedTime         (6),
            #           Latitude             (7),
            #           Longitude,           (8),
            #           CollectionTimeStamp  (9),
            #           ManufacturerSerial   (10)]

            key  = row[1]
            if key in dict:            
                dict[key][0].append(row[0])
                dict[key][1].append(row[2])
                dict[key][2].append(row[3])
                dict[key][3].append(row[4])
                dict[key][4].append(row[5])
                dict[key][5].append(row[6])
                dict[key][6].append(row[7])
                dict[key][7].append(row[8])
                dict[key][8].append(row[9])
                dict[key][9].append(row[13])
                dict[key][10].append(row[14])
            else:
                dict[key] = [[row[0]],[row[2]],[row[3]],[row[4]],[row[5]],
                [row[6]],[row[7]],[row[8]],[row[9]],[row[13]],[row[14]]]
    return dict
