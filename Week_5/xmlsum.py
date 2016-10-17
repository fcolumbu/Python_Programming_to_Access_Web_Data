import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_317863.xml'

sum = 0
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)
counts = tree.findall('comments/comment')
items = len(counts)

for i in range(items):
	print counts[i].find('count').text
	sum += int(counts[i].find('count').text)

print 'Number of items: ', items
print 'Sum = ', sum

