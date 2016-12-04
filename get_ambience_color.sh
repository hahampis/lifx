#!/bin/bash

color_type=${1:-highlight}
dconf dump /desktop/jolla/theme/color/ | grep -Po "(?<=^$color_type='#).+(?=')"
