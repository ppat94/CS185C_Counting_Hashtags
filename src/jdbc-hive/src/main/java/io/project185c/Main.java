package io.project185c;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Properties;

import org.codehaus.jettison.json.JSONArray;
import org.codehaus.jettison.json.JSONException;
import org.codehaus.jettison.json.JSONObject;

import com.jcraft.jsch.JSch;
import com.jcraft.jsch.JSchException;
import com.jcraft.jsch.Session;

public class Main {


	private static final String JDBC_DRIVER_NAME = "org.apache.hive.jdbc.HiveDriver";
	private static String connectionUrl;

	public static void main(String[] args) throws IOException, JSchException, JSONException {

		// Get url Connection
		connectionUrl = "jdbc:hive2://192.168.56.101:10000/default";
		Connection con = null;
		JSONArray mainJson = new JSONArray();

		//==== Select data from Hive Table
		String sqlDropTable = "DROP TABLE tweets_table";
		String sqlExternalTable = "CREATE EXTERNAL TABLE IF NOT EXISTS tweets_table(id BIGINT, hashtag VARCHAR(300), longitude DOUBLE, latitude DOUBLE) COMMENT 'tweet data' ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE LOCATION '/user/input'";
		String sqlStatementCreate = "CREATE TABLE IF NOT EXISTS tweets_table(id BIGINT, hashtag VARCHAR(300), longitude DOUBLE, latitude DOUBLE) COMMENT 'tweet data' STORED AS ORC";

		String sqlStatementSelect = "SELECT * from tweets_table";
		try {
			// Set JDBC Hive Driver
			Class.forName(JDBC_DRIVER_NAME);
			// Connect to Hive
			con = DriverManager.getConnection(connectionUrl,"root","");
			// Init Statement
			Statement stmt = con.createStatement();
			stmt.execute(sqlDropTable);
			stmt.execute(sqlExternalTable);
			stmt.execute(sqlStatementSelect);

			FileWriter write = new FileWriter(new File("record.json"));
			ResultSet res = stmt.executeQuery(sqlStatementSelect);
			    while (res.next()) {
			    	String record = res.getString(1) + "," + res.getString(2)+"," + res.getString(3)+"," + res.getString(4);
			    	System.out.println(record);
			    	JSONObject json = new JSONObject();
					json.put("_id", res.getString(1));
					json.put("hashtags", res.getString(2));
					json.put("long",res.getString(3));
					json.put("lat",res.getString(4));
					mainJson.put(json);
			    	System.out.println(res.getString(1) + "," + res.getString(2)+"," + res.getString(3)+"," + res.getString(4));
			      }
			    write.write(mainJson.toString());
			    write.flush();
			   	write.close();
			    System.exit(0);
		} catch (Exception e) {
			System.out.println(e.getMessage());
			} finally {
			try {
				con.close();
			} catch (Exception e) {
				// swallow
			}
		}

	}
}
