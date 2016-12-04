#!/bin/sh

ssh osmc@osmc /home/osmc/github/lifx/follow_ambience_color.py $(/home/nemo/github/lifx/get_ambience_color.sh)
