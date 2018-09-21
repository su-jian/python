#!/usr/bin/python
import os,commands
def inputinfo():
	aa=raw_input('please input IP Address \033[1m')
	bb=raw_input('\033[0mplease input prefix \033[1m')
	cc=raw_input('\033[0mplease input GATEWAY \033[1m')
	dd=raw_input('\033[0mplease input DNS \033[1m')
	name=commands.getoutput("ifconfig |awk -F: '/eno/{print $1}'").split()
	ee=raw_input('%s\n\033[0mplease choice network name(don\'t input space) '%(name))
	if ee in name:
		i=[aa,bb,cc,dd,ee]
	else:
		i=[aa,bb,cc,dd,name[0]]
	return i
def backup(choice):
	if os.system('cd /etc/sysconfig/network-scripts/ &>/dev/null; cp ifcfg-%s ifcfg-%s.bak &>/dev/null'%(choice[4],choice[4])) :
		print 'backup false'
		return 0
	else:
		print 'backup ok'
		return 1
def set(choice):
	file=open('/etc/sysconfig/network-scripts/ifcfg-%s'%(choice[4]),'w+')
	file.write('TYPE=Ethernet\nBOOTPROTO=none\nNAME=%s\nDEVICE=%s\nONBOOT=yes\nIPADDR=%s\nPREFIX=%s\nGATEWAY=%s\nDNS1=%s\n'%(choice[4],choice[4],choice[0],choice[1],choice[2],choice[3]))
	file.close()
	if os.system('diff ifcfg-%s ifcfg-%s.bak &>/dev/null'%(choice[4],choice[4])):
		print 'update ok'
	#	os.system('ifdown %s ;sleep 2;ifup %s'%(choice[4],choice[4]))
		os.system('service network restart')
	else:
		print 'update false'
choice=inputinfo()
if backup(choice):
	set(choice)
else:
	print 'update false'

