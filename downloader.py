from datetime import datetime, timedelta
import requests

def nvd():
    # save the date of 24 hours ago as last_mod_date, then format it for use in the API call
    last_mod_date = str(datetime.today() - timedelta(hours=1))[:-3]
    last_mod_date = (last_mod_date.replace(".", ":").replace(" ", "T") + "%20UTC%2B10:00")
    url = "https://services.nvd.nist.gov/rest/json/cves/1.0?modStartDate="
    page_limit = "&resultsPerPage=2000"
    nvd_vulns = requests.get(url + last_mod_date + page_limit)
    # open and save nvd_$date, then save the response
    todays_vulns = open("/home/CVELK/vulnerabilities/nvd/nvd_" + str(datetime.today()) + ".txt", "w+")
    todays_vulns.write(nvd_vulns.text)
    todays_vulns.close()
    os.system("sudo /usr/share/logstash/bin/logstash -f /home/CVELK/logstash_parsers/nvd.conf")


def circl():
    # we grab the datetime again, in case the first function takes a while to run
    last_mod_date = str(datetime.today() - timedelta(days=1))[:-3]

nvd()
