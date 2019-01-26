import urllib2

def read(latitude,longitude):
    url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key=AIzaSyBW5QZVpvnxWPcemecQBxhxZrjPjxB2bXU'.format(latitude,longitude)
    r = urllib2.urlopen(url)
    print(r.read())

read(49.15563,-123.0172)
