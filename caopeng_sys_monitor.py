#!/usr/bin/python
import os
##################show menu##################3
def menu():
	menu={1:'cpu info',2:'memory info',3:'disk info',4:'exit'}
	for i,j in menu.items():
		print i,j
#################cpu info########################
def c_info():
	import os
	c_info=os.popen('dstat -c 1 2')
	for i in c_info:
		print i	
###################memory info######################
def m_info():
	import os
	m_info=os.popen('dstat -m 1 2')
	for i in m_info:
		print i	
##########################disk info################
def d_info():
	import os
	d_info=os.popen('dstat -d 1 2')
	for i in d_info:
		print i	

#############################main#######################
def main():
	while True:
		os.system("clear")
		menu()
		cho=raw_input('please input your choice:')
		if cho.isdigit():
			n=int(cho)
			if n>=1 and n<=4:
				if n == 1:
					c_info()
				elif n == 2:
					m_info()
				elif n == 3:
					d_info()
				else:
					exit()
			else:
				print "please input 1-4!"
		else:
			print "please input correct option!"
		a=raw_input('Press Enter to continue!')
###########################################
main()
