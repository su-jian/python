#!/bin/bash

#查找UID大于等于500小于等于60000的用户

read -p "请输入要查找的目录：" dir

for i in $(cat /etc/passwd |cut -d ":" -f3) #取出所有用户的UID号
do
    if (( i >= 500 && i <= 60000 ))
    then
        user_name=$(grep ":x:$i:" /etc/passwd | cut -d ":" -f1) #取出UID号符合的用户名
        num=$(find ${dir} ! -type d -user ${user_name} | wc -l) #查找该用户在该文件夹下有多少文件
        if (( ${num} >= 1 ))
        then
            echo "${user_name} have ${num} files"
        fi
    fi
done
