#!/usr/bin/python

import pexpect
import sys
import time
import os

class scpc:
	def __init__(self,file,user,host,password,dir):
		self.file=file
		self.user=user
		self.host=host
		self.password=password
		self.dir=dir
	def scp(self): 
		if os.path.isdir(file):
			child=pexpect.spawn('scp -r %s %s@%s:%s'%(file,user,host,dir))
		else:
			child=pexpect.spawn('scp %s %s@%s:%s'%(file,user,host,dir))
		#log='./log_scp/log_%s'%(time.strftime('%Y%m%d%H%M%S'))
		#fout=file(log,'w')
		#child.logfile=fout
		child.logfile=sys.stdout
		try:
			#child.expect('(yes/no)?')
			#child.sendline('yes')
			child.expect('password:')
			child.sendline('%s'%(password))
			child.expect(pexpect.EOF)
		except pexpect.EOF:
			print 'expect EOF'
		except pexpect.TIMEOUT:
			print 'expect TIMEOUT'
		
#file=raw_input('File:')
#user=raw_input('User:')
#host=raw_input('Host:')
#password=raw_input('Password:')
#dir=raw_input('Dir:')

f=file('info_scp.txt','r')
for (i,v) in enumerate(f):
	item=v.split(',')
	file=item[0]	
	user=item[1]	
	host=item[2]	
	password=item[3]	
	dir=item[4]
	print '{x}'.format(x=i+1)
	s=scpc(file,user,host,password,dir)
	s.scp()
