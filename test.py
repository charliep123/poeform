import urllib
import urllib2
import cfscrape


data = {
    "league" : "Breach"
}

#encode = urllib.urlencode(data)

scrape = cfscrape.create_scraper() 

#html = urllib.urlopen("http://poe.trade") #urllib2.urlopen("http://poe.trade",encode)

print scrape.get("http://poe.trade").content


