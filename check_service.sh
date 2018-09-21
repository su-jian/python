#!bin/bash

#检查服务状态
check()
{
        for i 
        do 
            if  service $i status &> /dev/null
            then
                echo "$i 状态正常"
            elif (($?==1))
            then
                echo "$i服务不存在，请检查问题"
            else
                service $i restart &> /dev/null && echo "$i 重启后已经ok" || echo "$i 服务有问题"
            fi
        done
}
check $@
