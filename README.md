# CS185C_Counting_Hashtags

Note: All the following commands should be executed using the root user with password “mapr”.
1. Download the .ova image from the following link:
>https://drive.google.com/open?id=1zqmiNRkLkquSRdOB7QbsMUjNu5WucwGi

2. Import the .ova image in VirtualBox and start the virtual machine

3. Start the virtual machine from the virtual box and wait for it be up completely.

4. Now, on your host computer, ssh into machine using mapr user and the ip: 192.168.56.101 using the following command:
>ssh mapr@192.168.56.101

Note: On being prompted for password, enter password as “mapr”

5. If there is trouble in logging into the virtual machine and error message “WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!” is displayed, then,  execute the following command:
>ssh-keygen -R 192.168.56.101 

6. Open a new tab in terminal and ssh into VM using the command mentioned in step 4.

7. Navigate to the CS185C_Counting_Hashtags/src using the following command:
cd Desktop/CS185C_Counting_Hashtags/src

8. Grant permissions and execute the start.sh script by using the following command. Make sure to log in as root and enter the password as “mapr”
>su root
>chmod +x run.sh
>./start.sh

You will be prompted to “replace hash.txt?” for which, enter “y” as a response.
Further you will also be prompted to “replace __MACOSX/._hash.txt?” for which, enter “y” as the response.

9. Now let this process run. Run the run.sh in another tab which we opened earlier and make sure to connect as root.
>cd Desktop/CS185C_Counting_Hashtags/src

a) Grant permissions and execute the run.sh script by using the following command:
>chmod +x run.sh
>./run.sh

The above script will perform twitter streaming and terminate after 30 seconds.

b) In the cron job terminal, you will see the JDBC code, node module getting built. The web server starts after that.

10. To find the trending tweets, open the following URL in the Safari web browser:
>http://0.0.0.0:8080
     
11. Now select the search-box and hit the Enter key 2 times to show all the current trends in the world. (Data visualization can sometimes take time to populate the data on the webpage due to large volume of data).

12.  Type a hash-tag, for example, “thanksgiving2018” and hit Enter key twice to see the change in the data and view only trends related to the hashtag specified in the searchbox.

Following is the link to video tutorial:
>https://drive.google.com/open?id=1vuQF1cHBG_lbDL2EIVE_2CAls88OkaA3



