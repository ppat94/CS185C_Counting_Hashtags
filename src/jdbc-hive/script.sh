hadoop fs -put -f /home/mapr/Desktop/CS185C_Counting_Hashtags/src/streamer/processed/hash.txt /user/input/
mvn clean install
java -jar target/jdbc-hive-1.0-SNAPSHOT-jar-with-dependencies.jar jdbc:hive2://192.168.56.101:10000/default;ssl=false
yes | cp -rf record.json /home/mapr/Desktop/CS185C_Counting_Hashtags/pure-js/record.json
cd /home/mapr/Desktop/CS185C_Counting_Hashtags/pure-js/
npm install
npm start
 
