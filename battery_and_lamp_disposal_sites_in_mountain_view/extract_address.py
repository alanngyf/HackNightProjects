import urllib2
import json
import sys
import re
from my_domxml import geocode
from my_domxml import createKML

data = urllib2.urlopen("http://www.mountainview.gov/depts/pw/recycling/hazard/default.asp")
page = data.read()
page = page[page.find("Batteries &amp; Lamps"):page.find("BATTERIES ONLY")]
addresses = re.findall("</strong>[^<]+", page)
for i in range(len(addresses)):
	addresses[i] = re.sub("</strong>", "", addresses[i])

locations = []
for address in addresses:
	print address
	geom = json.load(urllib2.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address="+urllib2.quote(address)))
	location = geom['results'][0]['geometry']['location']
	locations.append(location)
	print location
	createKML(address, address)


# reverse lookup
# reverse = []
# for loc in locations:
# 	long_lat = str(loc[u'lat'])+','+str(loc[u'lng'])
# 	geom = json.load(urllib2.urlopen("http://maps.googleapis.com/maps/api/geocode/json?latlng="+long_lat))
# 	a = geom['results'][0]['formatted_address']
# 	print a
# 	reverse.append(a)
