# !flask/bin/python 

import sys

from flask import Flask, render_template, request, redirect, Response
import random, json
from urllib.request import urlopen
import requests

def read(latitude,longitude):
    url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key=AIzaSyBW5QZVpvnxWPcemecQBxhxZrjPjxB2bXU'.format(latitude, longitude)

    json_data = requests.get(url).json()
    place = json_data['results'][0]['formatted_address']
    # print(place)
    return place

read(49.15563, -123.0172)

app = Flask(__name__)

@app.route('/map.html')
def output():
	# serve index template
    place = read(49.15563, -123.0172)
    return render_template('map.html', address2 = place)

if __name__ == '__main__':
	# run!
	app.run()