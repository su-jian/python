#!bin/bash

#实现批量删除用户

read -p "请输入需要删除的用户名前缀:" user_pre
# 判断位置变量是否非空
if [ -z ${user_pre} ]
then
    echo "请输入合法的用户名前缀"
    exit 
fi 

sucss_del=0
if grep "^${user_pre}" /etc/passwd &> /dev/null
then  
    for i in $(grep "^${user_pre}" /etc/passwd|cut -d ":"  -f1) #找出前缀为${user_pre}的用户
    do
        uid=$(id $i|cut -d "(" -f1|cut -d"=" -f2)  #取出${user_pre}的UID号
        if ((${uid}<500)) || ((${uid}>60000))
        then
            echo "$i 是系统用户不能删除"
        else 
            if userdel -r $i &> /dev/null 
            then 
                echo "用户$i已经被成功删除"
            ((sucss_del++))
            else 
                echo "用户$i删除失败"
            fi
        fi
    done
    echo "一共删除的用户数:${sucss_del}个"
    exit
else 
    echo "以${user_pre}开头的用户不存在"
fi    