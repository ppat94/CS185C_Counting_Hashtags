#!/bin/bash

counter=0

while [ $counter -lt 3 ]
do
   echo "Creating Tweeter Live Stream File"
   python TweeterLiveStreamer.py
   counter=`expr $counter + 1`
done
python DataProcessor.py
