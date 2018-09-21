#!/usr/bin/env python
import os
import getpass
a=getpass.getuser()
b=os.getuid()
print "longin user is\033[1m",a,"\033[0muid=\033[1m",b,"\033[0m"
c=os.getpid()
d=os.getppid()
print "current process pid is\033[1m",c,"\033[0mcurrent process ppid is\033[1m",d,"\033[0m\n"

aa=os.popen('cat /proc/meminfo').readlines()
print aa[0]
print aa[1]
