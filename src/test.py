from bs4 import BeautifulSoup
import urllib2
import requests

url = "https://mcommunity.umich.edu/#profile:immerman"

content = requests.get(url).content;
soup = BeautifulSoup(content)
iframexx = soup.find_all('iframe')
for iframe in iframexx:
    response = urllib2.urlopen(iframe.attrs['src'])
    iframe_soup = BeautifulSoup(response)
print "stuff"
