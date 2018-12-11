yum install zip -y
yum install unzip -y

cd /home/mapr/Desktop/CS185C_Counting_Hashtags/data/
unzip hash.txt.zip
yes | cp -rf hash.txt /home/mapr/Desktop/CS185C_Counting_Hashtags/src/streamer/processed/hash.txt

sudo yum install https://centos7.iuscommunity.org/ius-release.rpm
yum install python36u
yum install python36u-pip
python3.6 -m pip install tweepy
python3.6 -m pip install numpy

cd /home/mapr/Desktop/CS185C_Counting_Hashtags/src/jdbc-hive
echo "----------------------------"
echo "Started Cron Job Execution"
while inotifywait -e modify /home/mapr/Desktop/CS185C_Counting_Hashtags/src/streamer/processed; do ./script.sh; done
