import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')

count = raw_input('Enter count: ')
pos = raw_input('Enter position: ')

num = int (count)
position = int (pos)

def retreive(url):
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('a')
	l = []
	for tag in tags:
		l.append(tag.get('href', None))
		if len(l) == position:
			return l[position - 1]

print url
for i in range(0, num):
	url = retreive(url)
	print url

