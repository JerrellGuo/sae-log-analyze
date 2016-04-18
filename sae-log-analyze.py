#coding=utf-8
import urllib2
from apibus_handler import *
ACCESSKEY = 'your accesskey'
SECRETKEY = 'your secretkey'
apibus_handler = SaeApibusAuthHandler(ACCESSKEY, SECRETKEY)
opener = urllib2.build_opener(apibus_handler)
log_file = opener.open('http://g.sae.sina.com.cn/log/http/2016-04-18/1-access.log') #这里参考api文档说明填写，,我这里获取的是4月18号的所有http访问日志

ips = []
for line in log_file:
    array = line.split(' ')
    ips.append(array[1])

ips.sort()
for i in range(len(ips)):
    print ips[i]
