#!/usr/bin/python
import pexpect
import sys
import time
class sshc:
	def __init__(self,user,host,password,command):
		self.user=user
		self.host=host
		self.password=password
		self.command=command
	def ssh(self): 
		child=pexpect.spawn('ssh %s@%s'%(user,host))
#		log='./log_ssh/log_%s'%(time.strftime('%Y%m%d%H%M%S'))
#		log='./log.txt'
#		fout=file(log,'a+')
#		child.logfile=fout
		child.logfile=sys.stdout
		try:
			child.expect('(yes/no)?')
			child.sendline('yes')
			child.expect('password:')
			child.sendline('%s'%(password))
		except pexpect.EOF:
			print 'expect EOF'
		except pexpect.TIMEOUT:
			print 'expect TIMEOUT'
		
		#index=child.expect(['password:','(yes/no)?'])
		#print index
		#if index==0:
		#	child.sendline('yes')
		#else:
		#	child.sendline('%s'%(password))
		
		child.expect('#')
		child.sendline('%s'%(command))
		child.expect('#')
		
#user=raw_input('User:')
#host=raw_input('Host:')
#password=raw_input('Password:')
#command=raw_input('Command:')

f=file('info_ssh.txt','r')
for (i,v) in enumerate(f):
	item=v.split(',')
	user=item[0]	
	host=item[1]	
	password=item[2]	
	command=item[3]	
	print '{x}'.format(x=i+1)
	s=sshc(user,host,password,command)
	s.ssh()
