A set of scripts for making my LIFX lights follow the ambience color of my Jolla phone.

detect_ambience.sh: Runs on the phone. Triggered by Situations app when situation is "At home".
It is supposed to run "forever" (until Situations app detects I'm not at home and kills it) and it will check every 10 seconds
whether there has been an ambience change.

change_light_color.sh: Runs on the phone.It is basically a helper script and calls other scripts which do the actual work.
It can be eliminated in the future.

get_ambience_color.sh: Runs on the phone. Gets the current ambience color ("highlight" type by default).

follow_ambience_color.py: Runs on my raspberry pi currently. Only reason is that my phone doesn't have the required python packages (requests, pip, ...). Takes an RGB color code as argument and sets it as the lights' current color.

This is very draft work. A lot of things can (and will) be done better obviously!
