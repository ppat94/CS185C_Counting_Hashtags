hadoop fs -put -f hash.txt /user/input/
mvn clean install
java -jar target/jdbc-hive-1.0-SNAPSHOT-jar-with-dependencies.jar jdbc:hive2://192.168.56.101:10000/default;ssl=false
