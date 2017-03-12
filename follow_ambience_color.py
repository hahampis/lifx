#!/usr/bin/python

import requests
import subprocess
import sys

token = open('/home/osmc/token').read().strip()
ambience_color = sys.argv[1][2:]

data = {"power": "on", "color" : "#" + ambience_color}
response = requests.put('https://api.lifx.com/v1/lights/all/state',
                         data=data, auth=(token, ''))
