#!/bin/bash

while true
do
  new_ambience=$(dconf dump /desktop/jolla/theme/ | grep active_ambience)
  if [ $new_ambience != $(cat ~/current_ambience.txt) ]
  then
  echo $new_ambience > ~/current_ambience.txt
  /home/nemo/github/lifx/change_light_color.sh
  fi
sleep 10
done
