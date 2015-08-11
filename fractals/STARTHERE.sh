#!/bin/bash

cd /home/pi/raspberry-pi/fractals/

while true
do
printf "\n\n~~~~Welcome to the fractal demo!~~~~\n\nHit enter to begin:\n"
read input
python ./fractaldemo.py
done
