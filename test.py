import urllib
import urllib2



data = {
    "league" : "Breach"
}

encode = urllib.urlencode(data)

html = urllib2.urlopen("http://poe.trade/search",encode)

print html.readlines()
