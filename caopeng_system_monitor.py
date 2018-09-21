#!/usr/bin/python
# coding:utf-8
#author:caopeng
#date:2016-09-19
#function:system information and system monitor

import psutil,os
######################menu###############################
def menu():
	print '\033[32;5m*'*10,'MENU','*'*10,'\033[0m'
	menu={1:'memory useage',2:'cpu useage',3:'disk useage',4:'memory monitor',5:'cpu monitor',6:'disk monitor',7:'exit'}
	for i,j in menu.items():
		print '\033[33m',i,'.',j,'\033[0m'
###########memory monitor##################
def m_mem():
	m_info = psutil.virtual_memory()
	m_per = m_info.percent
	if m_per > 60 and m_per < 80:
		print '\033[31mWARNING!the memory useage is more than 60%!\033[0m'
	elif m_per >= 80:
		print '\033[31mWARNING!Memory is not enough!!!\033[0m'
	else:
		print '\033[35mMemory is ok!\033[0m' 

###############cpu monitor###########
def m_cpu():
	c_info=psutil.cpu_times_percent()
	c_used = 1-c_info.idle
	if c_used > 80:
		print '\033[36mWARNING!CPU useage is not enough!!!\033[0m'
	else:
		print '\033[35mCPU is ok!\033[0m'

#####################disk monitor##################
def m_disk():
	boot_info=psutil.disk_usage('/boot')
	boot_per=boot_info.percent
	g_info=psutil.disk_usage('/')
	g_per=boot_info.percent
	if g_per > 60 and g_per < 80:
		print '\033[31mWARNING!the / disk useage is  more than 60%!\033[0m'
	elif g_per > 80:
		print '\033[31mWARNING!the / disk is not enough!!!\033[0m'
	else:
		print '\033[35m/ disk is ok!\033[0m'

	if boot_per > 60 and boot_per < 80:
		print '\033[31mWARNING!the /boot disk useage is  more than 60%!\033[0m'
	elif boot_per > 80:
		print '\033[31mWARNING!the /boot disk is not enough!!!\033[0m'
	else:
		print '\033[35m/boot disk is ok!\033[0m'

#####################check memory#########
def c_m():
	m_info = psutil.virtual_memory()
	m_per = m_info.percent
	m_t=m_info.total/1024/1024
	m_u=m_info.used/1024/1024
	m_f=m_info.free/1024/1024
	print '\033[34m@@@@@Memroy useage@@@@@\ntotal:%d M'%m_t,'used:%d M'%m_u,'free:%d M'%m_f,'percent: ',m_per,'%\033[0m'

#####################check cpu######
def c_c():
	c_info=psutil.cpu_times_percent()
	print '\033[34m@@@@@CPU useage@@@@@\nuser:',c_info.user,'system:',c_info.system,'idle:',c_info.idle,'\033[0m'

############################check disk#####
def c_d():
	d_info=psutil.disk_partitions()
	print '\033[34m@@@@@disk partitions@@@@@'
	for i in d_info:
		print i
	else:
		print '\033[0m'

################main######################
def main():
        while True:
                os.system('clear')
                menu()
                cho=raw_input('\033[36mplease input choice:\033[0m')
                if cho.isdigit():
                        b=int(cho)
                        if b == 1:
                                c_m()
                        elif b == 2:
                               	c_c()
                        elif b == 3:
                                c_d()
                        elif b == 4:
                                m_mem()
			elif b == 5:
				m_cpu()
			elif b == 6:
				m_disk()
			elif b == 7:
				exit()
                        else:
                                print '\033[31mplease input 1-7!\033[0m'
                else:
                        print '\033[31mplease input correct options!\033[0m'
                r=raw_input('\033[36mPress ENTER to continue!\033[0m')

##############
main()
