import csv

ID = []
DeviceSerial = []
VIN=[]
MessageType=[]
ReportType=[]
MsgNum=[]
TripState=[]
ReceivedTimestamp=[]
Latitude=[]
Longitude=[]
MessageXML=[]
ProcessedTimestamp=[]
IsProcessed=[]
CollectionTimestamp=[]
ManufacturerSerial=[]

def readMyFile(filename):
    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            ID.append(row[0])
            DeviceSerial.append(row[1])
            VIN.append(row[2])
            MessageType.append(row[3])
            ReportType.append(row[4])
            MsgNum.append(row[5])
            TripState.append(row[6])
            ReceivedTimestamp.append(row[7])
            Latitude.append(row[8])
            Longitude.append(row[9])
            MessageXML.append(row[10])
            ProcessedTimestamp.append(row[11])
            IsProcessed.append(row[12])
            CollectionTimestamp.append(row[13])
            ManufacturerSerial.append(row[14])

    return ID, DeviceSerial, VIN, MessageType, ReportType, MsgNum, TripState, ReceivedTimestamp, Latitude, Longitude, MessageXML, ProcessedTimestamp, IsProcessed, CollectionTimestamp, ManufacturerSerial


ID,DeviceSerial,VIN, MessageType, ReportType, MsgNum, TripState, ReceivedTimestamp, Latitude, Longitude, MessageXML, ProcessedTimestamp, IsProcessed, CollectionTimestamp, ManufacturerSerial = readMyFile('ITM_20190121.csv')

print(ID[1])
print(DeviceSerial[1])
print(VIN[1])
print(MessageType[1])
print(ReportType[1])
print(MsgNum[1])
print(TripState[1])
print(ReceivedTimestamp[1])
print(Latitude[1])
print(Longitude[1])
print(MessageXML[1])
print(ProcessedTimestamp[1])
print(IsProcessed[1])
print(CollectionTimestamp[1])
print(ManufacturerSerial[1])

