import urllib2
import mako
from bs4 import BeautifulSoup as BS

html = urllib2.urlopen("<link-to-web-page>")
soup = BS(html)
data = []


for each_course in soup.findAll('li',{'class':'<class-name>'}):
    inner_text = each_course.text
    data.append(inner_text)


for i in data:
    print (i+"\n")