
import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')
print url

data = urllib.urlopen(url).read()

tree = ET.fromstring(data)
lst = tree.findall('comments/comment')

l = []
for item in lst:
	l.append(int (item.find('count').text))
	#print 'Comments number:',item.find('count').text
print sum(l)