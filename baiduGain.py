#<a target="_blank" href = "http://www.baidu.com/link?url=KhjvccN_yyrPsVMP4XaIuYxNmuWrOupUwz507R2wJRO" data-click
# http://www.baidu.com/s?wd=qq&pn=0
import httplib
from urllib import urlopen
import socket
import re

def getTrueLink(path):
    conn = httplib.HTTPConnection('www.baidu.com')
    conn.request("GET", "/link?url="+path)
    trueLink = conn.getresponse().getheader("Location")
    return trueLink

search = raw_input("enter the search words:")
pn = int(raw_input("How many pages you want to get (each page have ten links) :"))
start = 0
end = (pn-1)* 10
p = re.compile(r'href = "http://www.baidu.com/link\?url=(.*)"')
while start <= end:
    text = urlopen("http://www.baidu.com/s?wd="+search+"&pn="+repr(pn)).read()
    start +=10
    for path in p.findall(text):
        print getTrueLink(path)
