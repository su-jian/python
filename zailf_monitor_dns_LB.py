#!/usr/bin/python

import dns.resolver
import os
import httplib

iplist=[]
domain=raw_input('Enter host name:')

def get_ip():
	try:
		A=dns.resolver.query(domain,'A')
		for i in A:
			iplist.append(i.address)
		print iplist
	except:
		print "dns resolver error!"

def checkip(ip):
	url=ip+":80"
	global getcontent
	getcontent=''
	conn=httplib.HTTPConnection(url)

	try:
		httplib.socket.setdefaulttimeout(5)
		conn.request('GET','/var/www/index.html')
		r=conn.getresponse()
		getconntent=r.read(9)
	except:
		getconntent='aa'
	finally:
		if getconntent=='<!DOCTYPE':
			print ip+' is ok'
		else:
			print ip+' is error'
			return ip

get_ip()
	
if len(iplist)>0:
	error=[]
	for ip in iplist:
#		checkip(ip)
		error.append(checkip(ip))
		print error
else:
	print 'Sorry,can\'t resolver the host name'








