#!/usr/bin/python
'''monitor cpu disk and memory used status.'''

import psutil
##############menu##############
def menu():
    print "\t\t\033[1;5;34msystem information\033[0m"
    print "\t\t\033[32m 1.cpu infomation\033[0m"
    print "\t\t\033[33m 2.disk information\033[0m"
    print "\t\t\033[34m 3.memory information\033[0m"
    print "\t\t\033[36m 0.exit\033[0m"    
################cpu_info################
def cpu_info():
    cpu_infor = psutil.cpu_percent()
    com_s = float(cpu_infor)
    print "\033[1;5;34m##########cpu_info################\033[0m"
    print '\t\tyour cpu used ',com_s
    if  com_s > 80:
        print "\t\tnotice!!!,your cpu is top",com_s
    else:
        print "\t\trest your heart"
 ########disk info##################
def disk_info():
    d_g = psutil.disk_usage('/')
    u_p_per = float(d_g.used)/float(d_g.total)*100
    print "\033[1;5;34m######disk_info / ###########\033[0m"
    print "\t\t /  partiton is used  percent",u_p_per
    if 60 < u_p_per < 80 :
        print "\t\tnot enough space"
    elif u_p_per >= 80:
	print "\t\tspace not enough serious"
    else:
	print "\t\trest your heart,you can use continue"
    print "\033[1;5;34m########disk_info /boot#################\033[0m"
    d_b = psutil.disk_usage('/boot')
    b_per = float(d_b.used)/float(d_b.total)*100
    print "\t\t /boot  partiton is used  percent", b_per
    if 60 < b_per < 80 :
        print "\t\tnot enough space"
    elif b_per >= 80:
        print "\t\tspace not enough serious"
    else:
        print "\t\trest your heart,you can use continue"
 #############mem info#####################
def mem_info():
    m_total = psutil.virtual_memory()[0]
    m_used = psutil.virtual_memory()[3]
    m_per = float(m_used)/float(m_total)
    print "\033[1;5;35m############mem_info##########################\033[0m"
    print "\t\tyour memory used percent of ",m_per
    if m_per > 80 :
	print "\t\tmemory not enough"
    elif m_per > 60:
	print "\t\tnotice,your memory will not enough"
    else:
	print "\t\trest your heart"
def main():
	    menu()
	    cho = raw_input('please input your choice:')
	    if cho.isdigit():
	        if int(cho) == 1:
		    cpu_info()
		    aa = raw_input('please press any key to countie')
	        elif int(cho) == 2:
                    disk_info()
		    aa = raw_input('please press any key to countie')
	        elif int(cho) == 3:
                    mem_info()
		    aa = raw_input('please press any key to countie')
	        elif int(cho) == 0:
                    return 80
                else:
		    raw_input('please input number 0~3')
            else:
                print "please input number"
                bb = raw_input('please press any key to continue')
while True:
    import os
    os.system('clear')
    a = main()
    if a == 80:
        break
