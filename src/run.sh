#!/bin/bash
#yum install zip -y
#yum install unzip -y

#cd /home/mapr/Desktop/CS185C_Counting_Hashtags/data/
#unzip hash.txt.zip 
#mv -f hash.txt /home/mapr/Desktop/CS185C_Counting_Hashtags/src/streamer/processed/hash.txt
 
counter=0
#yum install python-pip -y
#pip install tweepy
#pip install numpy
cd /home/mapr/Desktop/CS185C_Counting_Hashtags/src/streamer/
while [ $counter -lt 3 ]
do
   echo "Creating Tweeter Live Stream File"
   python3.6 TweeterLiveStreamer.py
   counter=`expr $counter + 1`
done

python3.6 DataProcessor.py
