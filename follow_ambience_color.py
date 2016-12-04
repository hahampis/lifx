#!/usr/bin/python

import requests
import subprocess
import sys

token = open('/home/osmc/github/lifx/token').read().strip()
ambience_color = sys.argv[1][2:]

data = {"color" : "#" + ambience_color}
response = requests.post('https://api.lifx.com/v1/lights/all/effects/pulse',
                         data=data, auth=(token, ''))
