#!/bin/bash

#根据菜单选择显示或者修改网口信息，默认网关

#显示IP地址及掩码
display_ip_mask()
{
    read -p "请输入网口名称: " interface_name
    if ifconfig ${interface_name} &> /dev/null
    then
        ip_addr=$(ifconfig ${interface_name} | sed -rn 's/.*addr:(\S+).*/\1/p')
        netmask=$(ifconfig ${interface_name} | sed -rn 's/.*Mask:(\S+)/\1/p')
        echo "${interface_name}的IP:${ip_addr}"
        echo "${interface_name}的掩码:${netmask}"
    else
        echo "网口名称错误或者不存在，请重新输入！"
    fi
}

#显示默认网关
display_gateway()
{
    gateway=$(route -n | sed -rn 's/^0.0.0.0\s+(\S+).*/\1/p')
    echo "默认网关：${gateway}"
}

#校验IP是否合法
verify_ip()
{
    if ! echo "$1" | egrep "^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[01][0-9]|22[0-3])(\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3}$" &> /dev/null
    then
        echo "输入的IP不合法!"
        exit
    fi
}

#修改IP及掩码
modify_ip_mask()
{
    read -p "请输入网口名称: " interface_name
    if ifconfig ${interface_name} &> /dev/null
    then
        interface_config="/etc/sysconfig/network-scripts/ifcfg-${interface_name}"

        read -p "请输入新IP: " ip_addr
        verify_ip ${ip_addr}    #校验IP是否合法

        read -p "请输入子网掩码: " netmask
        #校验掩码是否合法
        if ! echo "${netmask}" | egrep "^255(\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3}$" &> /dev/null
        then
            echo "输入的子网掩码不合法!"
            exit
        fi

        #存放网口配置文件先备份再修改，否则新建
        if [ -f "${interface_config}" ]
        then
            cp -a ${interface_config} ${interface_config}.bak
            sed -in -e "/^IPADDR=/c IPADDR=${ip_addr}" -e "/^NETMASK=/c NETMASK=${netmask}" ${interface_config}
        else
            cat << eof > ${interface_config}
DEVICE=${interface_name}
TYPE=Ethernet
ONBOOT=yes
NM_CONTROLLED=yes
BOOTPROTO=static
IPADDR=${ip_addr}
NETMASK=${netmask}
eof
        fi

        old_ip_addr=$(ifconfig ${interface_name} | sed -rn 's/.*addr:(\S+).*/\1/p')
        if ifdown ${interface_name} ; ifup ${interface_name} &> /dev/null
        then
            if grep "^${old_ip_addr}" /etc/hosts &> /dev/null
            then
                sed -in "s/^${old_ip_addr}/${ip_addr}/" /etc/hosts
            fi
            rm -f ${interface_config}.bak
            echo "修改成功。"
        else
            #修改失败恢复配置文件
            if [ -f "${interface_config}.bak" ]
            then
                cp -a ${interface_config}.bak ${interface_config}
            else
                rm -f ${interface_config}
            fi
            echo "修改失败。"
        fi
    else
        echo "网口名称错误或者不存在，请重新输入！"
    fi
}

#修改默认网关
modify_gateway()
{
    read -p "请输入新网关地址：" gateway
    verify_ip ${gateway}
    gateway_config="/etc/sysconfig/network"
    cp -a ${gateway_config} ${gateway_config}.bak
    if route -n | grep "^0.0.0.0" &> /dev/null
    then
        old_gateway=$(route -n | sed -rn 's/^0.0.0.0\s+(\S+).*/\1/p')
        route del default gw ${old_gateway}
        if route add default gw ${gateway} &> /dev/null
        then
            sed -in "/^GATEWAY=/c GATEWAY=${gateway}" ${gateway_config}
            echo "修改成功。"
        else
            cp -a ${gateway_config}.bak ${gateway_config}
            route add default gw ${old_gateway}
            echo "网关地址与本机IP不在同一个网段，修改失败。"
        fi
    fi
}

PS3="请选择："
select choose in "查看网口IP" "查看默认网关" "修改IP" "修改默认网关" "退出"
do
    case ${choose} in
        查看网口IP)
            display_ip_mask
            ;;
        查看默认网关)
            display_gateway
            ;;
        修改IP)
            modify_ip_mask
            ;;
        修改默认网关)
            modify_gateway
            ;;
        退出)
            exit
            ;;
        *)
            echo "选择错误！"
            ;;
    esac
    break
done