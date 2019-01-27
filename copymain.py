import json
from flask import Flask
from flask import Response
from flask import jsonify
from flask import request
#from .blueprints import main
app = Flask(__name__)

import csv_reader
import warningLib

WEEKEND_VAL = 6
ACCEL_VAL = 1
AREA_VAL = 3

HIGH_BAR = 8
MED_BAR = 7
LOW_BAR = 6

trucks = []
events = {}

	# corresponding max warning value (high, med, low)
	# list of high warning stops for each truck 	
def reader():
	data = csv_reader.readMyFile("ITM_20190121.csv")

	warnings = []

	for key in data:
		truck = 'no_VIN_provided'

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
			if warningLib.location_warning(data,key,stops[i]):
				warning[i][1] += AREA_VAL
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
			if warning[i][1] > LOW_BAR:
				truckEvents.append({'lat': data[key][7][j], 'long': data[key][8][j], 'date': data[key][9][j]})

		trucks.append({'vin': truck, 'threatLevel': threatlevel})
		events[truck]=truckEvents

reader()

@app.route('/truckEvents/<truckID>')
def getTruckEvents(truckID):
	return Response(json.dumps({ 'data': events[truckID] }), mimetype='application/json');
	#request.args.get()
	# return str(events[truckID])

@app.route('/trucks')
def getTrucks():
	filteredTrucks = [];
	for truck in trucks:
		if truck['vin'] != 'no_VIN_provided':
			filteredTrucks.append(truck);
	return Response(json.dumps({ 'data': filteredTrucks }), mimetype='application/json')

                  