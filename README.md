# Splunk + Facebook Messenger

## Requirements

- Server to host <a href="https://www.splunk.com/en_us/download/splunk-enterprise.html" target="_blank">Splunk Enterprise</a> (10GB storage recommended)

For this project, I decided to use AWS (free tier) and set up two EC2 instances. You can read more about the AWS free tier <a href="https://aws.amazon.com/free/" target="_blank">here</a>.

## Instructions

1. Head over to Facebook and <a href="https://www.facebook.com/dyi" target="_blank">download your information</a>. Set the format to `HTML` (default) and media quality to `Low` (media files won't be used for this project), and pick your desired date range. Under `Your Information`, click `Deselect All` and only select `Messages`. Finally, click `Create File`.

2. Your files may take a while to generate, but once they are ready, you will be alerted via email. Once you get a notification that your files are ready, go back to the <a href="http://example.com/" target="_blank">Hello, world!</a> [Download Your Information page](https://www.facebook.com/dyi?tab=all_archives) and download your generated file. (Note: if multiple files are generated, everything after the first one will usually just contain media, so you don't need to download anything besides the first file.)

3. Extract the zip file you just downloaded, and find the `messages` folder inside. Once there, go into the `inbox` folder. Download <a href="http://example.com/" target="_blank">Hello, world!</a> [this Python script](https://raw.githubusercontent.com/sidward35/splunk-messenger/master/parse.py), which will convert all your HTML message files into CSV format, and place it into the `messages/inbox/` directory.

4. In the Python script, set line 6 to `windows = False` if not using Windows. Then run the Python script (I'm using Python 3.6) and you should now have several CSV files generated containing your Facebook Messenger data. Compress all your generated CSV files into zip archives no more than 500 Mb in size, to prepare for upload to Splunk.

5. Now that you've prepared your data to be ingested into Splunk, it's time to get some insights! Download and setup <a href="http://example.com/" target="_blank">Hello, world!</a> [Splunk Enterprise](https://www.splunk.com/en_us/download/splunk-enterprise.html) on a server. Once Splunk has been set up, go into `$SPLUNK_HOME/bin/` and run `./splunk start --accept-license`. Detailed setup instructions can be found <a href="http://example.com/" target="_blank">Hello, world!</a> [here](https://docs.splunk.com/Documentation/Splunk/latest/Installation/Chooseyourplatform).

6. Head over to Splunk Web (`http://<ENTERPRISE-SERVER-IP>:8000`) and login with the credentials you set up in the previous step. Then go to `Settings > Add Data > Upload` and select/drag your compressed archive of CSVs. (Note: you may get a warning `Preview is not supported for this archive file, but it can still be indexed`. You can ignore this message.)

7. Click `Next`, and you should now be at the `Input Settings` page. Next to `Source type`, click `Select`, and search for the `csv` source type. You can leave the `Host` value as is. For `Index`, click `Create a new index`, and set the `Index Name` to `messenger`. You can leave the rest of the settings as-is, or customize as you see fit. Next, click `Review`. Verify that `Source Type` is set to `csv` and `Index` is set to `messenger`, then hit `Submit`.

8. We're almost done! Now that we've ingested Facebook Messenger data into Splunk, all that's left is creating the dashboard. Go to `Dashboards > Create New Dashboard`, and give it a name. At the top-left, switch from `UI` to `Source` mode, and replace the pre-populated XML code with the code from <a href="https://raw.githubusercontent.com/sidward35/splunk-messenger/master/dashboard.xml" target="_blank">this dashboard template</a>. Hit `Save`, and then `Refresh` to reload the dashboard.

9. And that's it! You should now be able to see insights from your Facebook Messenger activity on Splunk. You can continue adding to this dashboard and search your data for more insights, or leave it as-is.


## References

- <a href="http://example.com/" target="_blank">Hello, world!</a> [Splunk Documentation](https://docs.splunk.com/Documentation)
- <a href="http://example.com/" target="_blank">Hello, world!</a> [Facebook Help](https://www.facebook.com/help/1701730696756992)
