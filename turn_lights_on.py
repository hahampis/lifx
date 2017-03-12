#!/usr/bin/python

import requests

token = open('/home/osmc/token').read().strip()

data = {"power": "on", "color": "kelvin:2700 brightness:1.0"}
response = requests.put('https://api.lifx.com/v1/lights/all/state',
                         data=data, auth=(token, ''))
