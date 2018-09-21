#!/bin/bash

#检查硬盘空间情况（除特殊的），超过80%报异常

disk_name=($(df -hP|sed -n '1!p' |awk '{print $1}'|grep "/dev"|cut -d "/" -f3|tr "\n" " "))

disk_rate=($(df -hP| awk '/^\/dev/{print $5}' | awk -F% '{print $1}'|tr "\n" " "))

for i in ${!disk_rate[@]} 
do
    if ((${disk_rate[$i]}>=80))
    then
        echo -e "磁盘分区${disk_name[$i]}异常----使用率为${disk_rate[$i]}%，已超80%"
    else
        echo -e "磁盘分区${disk_name[$i]}正常"
    fi
done
