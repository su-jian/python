#!bin/bash

#猜10以内的随机数

ran_number=$(expr $RANDOM % 10)
times=0
echo "大家猜猜0-9的随机数，你一共有3次机会"
while :
do
    read -p "请输入你猜测的价格数目：" num
    ((times++))
    if ((${num} == ${ran_number}))
    then
        echo "你答对了就是:$num，你一共猜了$times次"
        exit
    elif ((${times} == 3))
    then 
        echo "你猜了3次没机会了"
        exit 
    elif ((${num} > ${ran_number}))
    then 
        echo "太高啦，你还有$((3-$times))次机会"
    else
        echo "太低啦，你还有$((3-$times))次机会"
    fi 
done 