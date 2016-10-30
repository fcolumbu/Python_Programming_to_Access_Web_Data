import urllib
import json

i = 0
sum = 0
data = ''
url = raw_input ('Enter location: ')
print 'Retrieving ', url
connection = urllib.urlopen(url)
data = connection.read()


js = json.loads(data) # deserialize the json
print 'Retrieved ', len(data), ' characters'
# print json.dumps(js, indent = 4)

for item in js['comments']:
#	print 'count', item['count']
	i += 1
	sum += int(item['count'])
print 'Count: ',i
print 'Sum: ',sum