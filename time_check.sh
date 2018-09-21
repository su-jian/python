#!bin/bash

#时间检查

#time_ck函数产生相差的小时和分钟数
time_ck()
{   seconds=$(($1-time_now))   
    hours=$((seconds/3600)) 
    minutes=$((seconds%3600/60+1))    
}
#error函数选择超出时间$1 60秒内的时间
error()
{
    ((differ=time_now-$1))
    [ ${differ} -lt 60 ]
}
class_time=$(date +%s -d "09:00")
lunch_time=$(date +%s -d "12:00")
pm_class_time=$(date +%s -d "14:00")
after_school_time=$(date +%s -d "17:30")
time_now=`date +%s`

    if ((time_now<${class_time}))
    then
        time_ck ${class_time}
        echo "离上午上课还差${hours}小时${minutes}分钟。"
    elif error ${class_time}
    then 
        echo "上午上课时间到，躁起来，骚年们"
    elif ((time_now<${lunch_time}))
    then
        time_ck ${lunch_time}
        echo "离中午吃饭时间还有${hours}小时${minutes}分钟。"
    elif error ${lunch_time}
    then
        echo "开饭喽，同志们冲啊"
    elif ((time_now<${pm_class_time}))
    then
        time_ck ${pm_class_time}
        echo "午休，离下午上课时间还有${hours}小时${minutes}分钟。"
    elif error ${pm_class_time}
    then 
        echo "下午上课时间到，躁起来，骚年们"
    elif ((time_now<${after_school_time}))
    then
        time_ck ${after_school_time}
        echo "离放学时间还有${hours}小时${minutes}分钟。"
    else 
        echo "已经放学"
    fi 
