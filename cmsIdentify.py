#!/usr/bin/env python
#coding=utf-8
import glob,urllib, urllib2, re, sys


def scan():
    host = sys.argv[1]
    header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    charac = glob.glob('cms/*')
    amount = len(charac)
    count = 0
    for cms in charac:
        for line in open(cms, 'r'):
            line = line.strip().split('------')
            if len(line) != 3:
                continue
            r = urllib2.Request('http://'+host+line[0],headers=header)
            print 'http://'+host+line[0]
            try:
                u = urllib2.urlopen(r)
            except urllib2.URLError:
                continue
            data = u.read().decode('gbk')
            if re.compile(r'(?i)'+line[1]).search(data):
                    print 'Identified: '+host +' is ' + line[2]
                    sys.exit(0)
        count += 1
        print '......finished %.2f%%' % (count*1.0/amount*100)
    print 'can\'t identify it......'

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print '''\
        Example: python cmsIdentify.py www.baidu.com\
        '''
        sys.exit(1)
    scan()
