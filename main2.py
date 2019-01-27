#!/usr/bin/env python

import json
from flask import Flask
from flask import Response
app = Flask(__name__)

import csv_reader
import warningLib

WEEKEND_VAL = 5
ACCEL_VAL = 1
AREA_VAL = 2


@app.route('/')
def baseRoute():
	data = csv_reader.readMyFile("ITM_20190121.csv")

	warnings = []

	for key in data:

		stops = []
		for i in range(len(data[key][3])-1):
			if data[key][3][i] == "Trip Start" or (data[key][3][i] == "NoMoveTimeout" and data[key][3][i+1] != "NoMoveTimeout"):
				stops.append(i)

		warning = []
		for i in range(len(stops)):
			warning.append(0)
			if warningLib.time_warning(data,key,stops[i]):
				warning[i] += WEEKEND_VAL
			# if warningLib.location_warning(data,key,stops[i]):
				# warning[i] += AREA_VAL
			for j in range(1,min(10,len(data[key][0])-stops[i])):
				if warningLib.acceleration_warning(data,key,stops[i]+j):
					warning[i]+= ACCEL_VAL
		warnings.append(max(warning)) if len(warning)>0 else warnings.append(0)
	##return(" ".join(warnings))
	##return (tuple(warnings), 200)
	return Response(json.dumps(warnings), mimetype='application/json')
