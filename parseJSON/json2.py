import json
import urllib

url = raw_input('Enter location: ')
input = urllib.urlopen(url).read()

info = json.loads(input)
print 'User count:', len(info)

#print info['comments']
print len(info['comments'])

data = info['comments']

l = []

for item in data:
    l.append(int (item['count']))
    #print item
print sum(l)

   

