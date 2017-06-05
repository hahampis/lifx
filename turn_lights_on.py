#!/usr/bin/python

import requests
from datetime import datetime
from astral import Astral

def turn_lights_on():
    token = open('/home/osmc/token').read().strip()

    data = {"power": "on", "color": "kelvin:2700 brightness:1.0"}
    response = requests.put('https://api.lifx.com/v1/lights/all/state',
                             data=data, auth=(token, ''))

def get_sunlight_info():
    a = Astral()
    city = a['Athens']
    return city.sun()

if __name__ == '__main__':
    sunlight_info = get_sunlight_info()
    sunrise = sunlight_info['sunrise']
    sunset = sunlight_info['sunset']
    now = datetime.now(tz=sunrise.tzinfo)
    if now > sunset or now < sunrise:
        turn_lights_on()
