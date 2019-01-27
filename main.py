<<<<<<< HEAD
import json
from flask import Flask
from flask import Response
app = Flask(__name__)

=======
>>>>>>> dc1c8af5f1ecf6194f35ce0fd81a1b61edccac7e
import csv_reader
import warningLib

WEEKEND_VAL = 5
ACCEL_VAL = 1
AREA_VAL = 2

HIGH_BAR = 7
MED_BAR = 4


class Main:
	# corresponding max warning value (high, med, low)
	# list of high warning stops for each truck 
	def __init__(self):
		data = csv_reader.readMyFile("ITM_20190121.csv")

		self.trucks = []
		self.events = {}


<<<<<<< HEAD
		warnings = []

		for key in data:
			truck = 'no_VIN_provided'
=======
		warning = []
		for i in range(len(stops)):
			warning.append(0)
			if warningLib.time_warning(data,key,stops[i]):
				warning[i] += WEEKEND_VAL
			if warningLib.location_warning(data,key,stops[i]):
				warning[i] += AREA_VAL
			for j in range(1,min(10,len(data[key][0])-stops[i])):
				if warningLib.acceleration_warning(data,key,stops[i]+j):
					warning[i]+= ACCEL_VAL
		warnings.append(max(warning)) if len(warning)>0 else warnings.append(0)
	return warnings

main()
>>>>>>> dc1c8af5f1ecf6194f35ce0fd81a1b61edccac7e

			stops = []
			for i in range(len(data[key][3])-1):
				if data[key][3][i] == "Trip Start" or (data[key][3][i] == "NoMoveTimeout" and data[key][3][i+1] != "NoMoveTimeout"):
					stops.append(i)
					if truck == 'no_VIN_provided' and data[key][3][i] == "Trip Start" and data[key][1][i] != '':
						truck = data[key][1][i]
						#add the info for the TruckID (vim) to the class variable

			warning = []
			maxwarning = 0
			for i in range(len(stops)):
				warning.append([stops[i],0])
				if warningLib.time_warning(data,key,stops[i]):
					warning[i][1] += WEEKEND_VAL
				#if warningLib.location_warning(data,key,stops[i]):
				#	warning[i][1] += AREA_VAL
				for j in range(1,min(10,len(data[key][0])-stops[i])):
					if warningLib.acceleration_warning(data,key,stops[i]+j):
						warning[i][1]+= ACCEL_VAL
				if warning[i][1] > maxwarning:
					maxwarning = warning[i][1]
			
			threatlevel = 0
			if maxwarning > HIGH_BAR:
				threatlevel = 2
			elif maxwarning > MED_BAR:
				threatlevel = 1 

			truckEvents = []
			for i in range(len(warning)):
				j = warning[i][0]
				if warning[i][1] > HIGH_BAR:
					truckEvents.append([data[key][7][j],data[key][8][j],data[key][9][j]])

			self.trucks.append([truck,threatlevel])
			self.events[truck]= truckEvents

	def getTruckEvents(self, truckID):
		return self.events[truckID]

	def getTrucks(self):
		return self.trucks


a = Main()
print(a.getTruckEvents(a.getTrucks()[3][0]))