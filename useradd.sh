#!bin/bash

read -p "请输入用户名的前缀: " username_pre
read -p "请输入用户的数目: " user_amount
if ((user_amount>20)) 
then
    echo "最多只能同时新建20个用户"
    exit
fi

success_n=0
for i in $(seq ${user_amount})
do
    username="${username_pre}${i}"
    if id ${username}  &> /dev/null
    then
        echo " ${username} 已存在"
        continue
    else
        if useradd ${username} &> /dev/null
        then 
            echo "123" | passwd -stdin ${username} &> /dev/null
            ((success_n++))
            echo "创建用户${username}成功"
        else    
            echo "创建用户${username}失败"
        fi    
    fi 
done 
echo "一共创建的用户数:${success_n}"
