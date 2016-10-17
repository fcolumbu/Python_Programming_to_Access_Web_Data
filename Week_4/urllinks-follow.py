# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

# This code crawls over a series of URLs

import urllib
import re
from BeautifulSoup import *

url = raw_input('Enter starting URL - ')
position = int(raw_input('Enter position - ')) - 1
depth = int(raw_input('Enter depth - ')) 

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve the anchor tags
tags = soup('a')
#for tag in tags:
for count in range(depth):
	url = tags[position].get('href', None)
	print 'Next URL ',url
	name = re.findall('[A-Z][a-z]+', str(tags[position].contents))
	print name[0]
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)	
	tags = soup('a')