#!/bin/bash
#function:bulid local yum
#author:su
#version:1.0
#department:DBA

#mount /mnt to /yum
#[ -d /yum ]||mkdir /yum
mount  /dev/sr0  /mnt

#create local.repo file and backup another repo files to bak directory
cd  /etc/yum.repos.d
[ -d bak ]||mkdir bak
mv  *.repo bak
cat >localyum.repo <<EOF
[local_yum]
name=local 
baseurl=file:///mnt 
enabled=1
gpgcheck=0  
EOF
yum clean all
echo "mount /dev/sr0 /yum" >>/etc/rc.local