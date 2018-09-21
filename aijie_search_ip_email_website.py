#!/usr/bin/python
# coding = utf-8


'''This program is regular for  ip_address/URL(www)/mail_address.'''
import re

f1 = open('mail.txt').read()
f = re.sub('\s+', '\n', f1).splitlines()

mail_list = []
url_list = []
ip_list = []
for i in f:
    mail = re.search(r'\w+@[a-zA-Z0-9]+\.[a-zA-Z]+$', i)
    url = re.search(r'http://www\.[a-zA-Z0-9]*\.[a-zA-Z]+$', i)
    ip = re.search(r'^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-1][0-9]|22[0-3])(\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3}$', i)
    if mail:
        mail_list.append(mail.group())
    if url:
        url_list.append(url.group())
    if ip:
        ip_list.append(ip.group())

print "number:", len(mail_list), '  content:', mail_list
print "number:", len(url_list), '  content:', url_list
print "number:", len(ip_list), '  content:', ip_list
