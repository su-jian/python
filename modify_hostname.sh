#!/bin/bash

#根据当前主机的IP地址的最后1段的数字来配置本机的机器名

read -p "请输入主机的前缀:" host_pre
read -p "请输入主机的域名:" host_rea
ip_all=$(ifconfig bond0|sed -rn 's/.+addr:([0-9.]+).*/\1/p')
ip_tail=$(echo ${ip_all}|cut -d "." -f4)

#判断/etc/syscofig/network下是否含有相同内容的行
    if ! cat /etc/sysconfig/network "${host_pre}${host_rea}" &> /dev/null
    then  
        sed -in "s/^HOSTNAME.*/HOSTNAME=${host_pre}${ip_tail}\.${host_rea}/" /etc/sysconfig/network
    fi
echo "当前的机器名已经修改为: ${host_pre}${ip_tail}.${host_rea}"
echo -e "\n\n\t****************/etc/sysconfig/network文件的内容************\n"
cat /etc/sysconfig/network
#判断/etc/hosts下是否含有相同内容的行
    if  cat /etc/hosts|grep "${ip_all}" &> /dev/null
    then
        sed -in "s/^${ip_all}.*/${ip_all}${host_pre}${ip_tail}\.${host_rea} ${host_pre}${ip_tail}/" /etc/hosts
    else
        sed -in "\$a ${ip_all}${host_pre}${ip_tail}\.${host_rea} ${host_pre}${ip_tail}"  /etc/hosts
    fi

echo -e "\n\n\t************/etc/hosts文件的内容*************\n"
cat /etc/hosts
