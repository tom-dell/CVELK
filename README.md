# CVELK

CVELK is a completely free and open-source tool you can use to ingest open-source and even commercial vulnerability feeds into a single location, the ELK stack. Currently there is a hosted version that is free to use for personal, and commercial use, but below there are instructions on how to set this up locally, so you can ingest commercial feeds without breaching contractual agreements.

# Installing 

It's pretty simple process to create your own local version, which is outlined below.

* Install and configure the ELK stack
* Create the following directories
  * /home/cvelk
  * /home/cvelk/vulnerabilities
  * /home/cvelk/vulnerabilities/nvd
  * /home/cvelk/vulnerabilities/nvd
    * and so on for each feed
* Move the parsers to /home/cvelk/
* Move the python script
* Set a cronjob to run the python script every 24 hours

# New Feeds 
If you want to use a new feed, you'll need to write another parser, and add another function in the python script to download all vulnerabilities modified in the last 24 hours and trigger the new parser.

# To-Do
* Write the downloader script to download the CVEs modified in the last 24 houws for NVD
* Finish the CIRCL parser (includes matching the field names to a standardised format matching the NVD data)
* Add the CIRCL downloader to the python script
* Write a CVE-Details parser
* Add the CVE-Details downloader to the python script
