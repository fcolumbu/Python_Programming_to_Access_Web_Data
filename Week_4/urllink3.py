# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *
total = 0
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
#    print 'TAG:',tag
#    print 'URL:',tag.get('href', None)
#    print 'Contents:',tag.contents[0]
#    print 'Attrs:',tag.attrs
# The next line gives an additional check that we are reading good data.
    print 'span ',tag.contents[0] 
# The next line computes the sum.	
    total += int(tag.contents[0])
print 'Total= ',total