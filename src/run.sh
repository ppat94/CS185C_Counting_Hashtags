#!/bin/bash
 
counter=0
cd /home/mapr/Desktop/CS185C_Counting_Hashtags/src/streamer/
while [ $counter -lt 3 ]
do
   echo "Creating Tweeter Live Stream File"
   python3.6 TwitterLiveStreamer.py
   counter=`expr $counter + 1`
done

python3.6 DataProcessor.py
