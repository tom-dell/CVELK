# C.V.E.L.K.

C.V.E.L.K. is a completely free and open-source tool you can use to ingest open-source and even commercial vulnerability feeds into a single location, the ELK stack. Currently there is a hosted version that is free to use for personal, and commercial use, but below there are instructions on how to set this up locally, so you can ingest commercial feeds without breaching contractual agreements.

# Installing 

It's pretty simple process to create your own local version, which is outlined below.

* Install and configure the ELK stack
* Create the following directories
  * /home/cvelk/
  * /home/cvelk/vulnerabilities/
  * /home/cvelk/vulnerabilities/nvd/
  * /home/cvelk/vulnerabilities/circl/
    * and so on for each feed
* Move the parsers to /home/cvelk/
* Move the python script to /home/cvelk/
* Set a cronjob to run the python downloader script every hour

You can find more details in setting up a local version here, in my Medium article: https://medium.com/@tom__dell/creating-your-own-cvel-87331d5aa16e

# New Feeds 
If you want to use a new feed, you'll need to write another parser, and add another function in the python script to download all vulnerabilities modified in the last 24 hours and trigger the new parser.

If you can't figure out how to write a parser for a specific feed, make a issue and include a single vulnerability (preferable CVE-2019-14889) with the headers and footers, and I'll write a parser for you.
