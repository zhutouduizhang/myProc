__author__ = 'junmoxiao'
#! /usr/bin/env python
import httplib, sys, socket


def scan():
    host = sys.argv[1]
    path = sys.argv[2]
    dictionary = sys.argv[3]
    speed = sys.argv[4]
    catalog = open(dictionary,'r')
    count = 0
    while 1:
        line = catalog.readline()
        count += 1
        if not line:
            break
    statics = count
    print 'will test %d path' % statics
    catalog.seek(0)
    count = 0
    header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}  

    while 1:
        dic = catalog.readline()
        if not dic:
            break
        dic = dic.strip()
        conn = httplib.HTTPConnection(host)
        try:
            conn.request(speed,path+dic,headers=header)
            r1 = conn.getresponse()
        except httplib.BadStatusLine, socket.error:
            continue
        status = r1.status
        if path == '/':
            path = ''
        if status == 200:
            print 200, 'http://'+host+path+dic
        elif status == 403:
            print 403, 'http://'+host+path+dic
        count += 1 
        if count % 100 == 0:
            print '\t.....completed:%d(%.2f%%)' % (count, count*1.0/statics*100)
    conn.close()
    
if __name__ == '__main__':
    if len(sys.argv) != 5:
        print '''\
        python dirscan.py host path dictionary HttpMethod
        Example: python dirscan.py www.baidu.com / catalog.txt HEAD
        Example: python dirscan.py www.baidu.com /user catalog.txt GET\
        '''
        sys.exit(1)
    else:
        scan()
    
    
    
    
