# Splunk + Facebook Messenger

## Requirements

- Server to host [Splunk Enterprise](https://www.splunk.com/en_us/download/splunk-enterprise.html) (10GB storage recommended)

For this project, I decided to use AWS (free tier) and set up two EC2 instances. You can read more about the AWS free tier [here](https://aws.amazon.com/free/).

## Instructions

1. Head over to Facebook and [download your information](https://www.facebook.com/dyi). Set the format to `HTML` (default) and media quality to `Low` (media files won't be used for this project), and pick your desired date range. Under `Your Information`, click `Deselect All` and only select `Messages`. Finally, click `Create File`.
![Step 1](https://i.imgur.com/wVlv0aN.png)

2. Your files may take a while to generate, but once they are ready, you will be alerted via email. Once you get a notification that your files are ready, go back to the [Download Your Information page](https://www.facebook.com/dyi?tab=all_archives) and download your generated file. (Note: if multiple files are generated, everything after the first one will usually just contain media, so you don't need to download anything besides the first file.)
![Step 2 - Part 1](https://i.imgur.com/zvK0O67.png)
![Step 2 - Part 2](https://i.imgur.com/mSdzOX5.png)

3. Extract the zip file you just downloaded, and find the `messages` folder inside. Once there, go into the `inbox` folder. Download [this Python script](https://raw.githubusercontent.com/sidward35/splunk-messenger/master/parse.py), which will convert all your HTML message files into CSV format, and place it into the `messages/inbox/` directory.

4. In the Python script, set line 6 to `windows = False` if not using Windows. Then run the Python script (I'm using Python 3.6) and you should now have several CSV files generated containing your Facebook Messenger data. Compress all your generated CSV files into zip archives no more than 500 Mb in size, to prepare for upload to Splunk.
![Step 4](https://i.imgur.com/fTx9yBA.png)

5. Now that you've prepared your data to be ingested into Splunk, it's time to get some insights! Download and setup [Splunk Enterprise](https://www.splunk.com/en_us/download/splunk-enterprise.html) on a server. Once Splunk has been set up, go into `$SPLUNK_HOME/bin/` and run `./splunk start --accept-license`. Detailed setup instructions can be found [here](https://docs.splunk.com/Documentation/Splunk/latest/Installation/Chooseyourplatform).

6. Head over to Splunk Web (`http://<ENTERPRISE-SERVER-IP>:8000`) and login with the credentials you set up in the previous step. Then go to `Settings > Add Data > Upload` and select/drag your compressed archive of CSVs. (Note: you may get a warning `Preview is not supported for this archive file, but it can still be indexed`. You can ignore this message.)
![Step 6 - Part 1](https://i.imgur.com/TZL5sJS.png)
![Step 6 - Part 2](https://i.imgur.com/sGMZ7D9.png)

7. Click `Next`, and you should now be at the `Input Settings` page. Next to `Source type`, click `Select`, and search for the `csv` source type. You can leave the `Host` value as is. For `Index`, click `Create a new index`, and set the `Index Name` to `messenger`. You can leave the rest of the settings as-is, or customize as you see fit. Next, click `Review`. Verify that `Source Type` is set to `csv` and `Index` is set to `messenger`, then hit `Submit`.
![Step 7 - Part 1](https://i.imgur.com/U8m8Qo9.png)
![Step 7 - Part 2](https://i.imgur.com/ZDIGyL1.png)

8. We're almost done! Now that we've ingested Facebook Messenger data into Splunk, all that's left is creating the dashboard. Go to `Dashboards > Create New Dashboard`, and give it a name. At the top left, switch from `UI` to `Source` mode, and replace the current XML code with the code from [this dashboard template](https://raw.githubusercontent.com/sidward35/splunk-messenger/master/dashboard.xml). Hit `Save`, and then `Refresh` to reload the dashboard.
![Step 8 - Part 1](https://i.imgur.com/OMlNelE.png)
![Step 8 - Part 2](https://i.imgur.com/zRXZS0v.png)

9. And that's it! You should now be able to see insights from your Facebook Messenger activity on Splunk. You can continue adding to this dashboard and search your data for more insights, or leave it as-is.


## References

- [Splunk Documentation](https://docs.splunk.com/Documentation)
- [Facebook Help](https://www.facebook.com/help/1701730696756992)
