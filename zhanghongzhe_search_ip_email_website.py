#!/usr/bin/python

import re

url_list = []
email_list = []
ip_list = []

f = open('1.txt')

for line in f:
    ff=re.sub("\s+","\n",line).splitlines()
    for i in ff:
        if re.search(r'http://www\..*\.(com|cn|edu)', i):
            url_list.append(re.search('http://www\..*\.(com|cn|edu)', i).group())
        elif re.findall(r'[0-9a-zA-Z_]+@([0-9]+|[a-z]+)\.(com|cn|edu)', i):
            email_list.extend(re.findall(r"[0-9a-zA-Z_]+@\w+\.[a-zA-Z]+", i))
        elif re.findall(r'(([1-9]|[1-9][0-9]|1[0-9][0-9]|2[01][0-9]|22[0-3])(\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3})', i):
            all_ip=re.findall(r'^(([1-9]|[1-9][0-9]|1[0-9][0-9]|2[01][0-9]|22[0-3])(\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3})$', i)
            for i in all_ip:
                ip_list.append(i[0])

print url_list, email_list, ip_list

print "url:", len(url_list)
print "email:", len(email_list)
print "ip:", len(ip_list)
