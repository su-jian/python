#!/bin/bash

port=$1

echo_result()
{
    process_name=$(echo "$1" | awk -F"/" '{print $NF}')
    process_name=$(echo ${process_name})
    protocol=$(echo "$1" | awk '{print $1}')
    echo "${process_name}正在侦听：${protocol} ${port}端口"
}

check_port()
{
    tcp_port_info=$(netstat -antp | grep :$1 | grep -w "LISTEN" | head -1)
    udp_port_info=$(netstat -anup | grep :$1 | grep -w "LISTEN" | head -1)

    if [ -z "${tcp_port_info}" ] && [ -z "${udp_port_info}" ]
    then
        echo "$1端口没有侦听"
    elif [ -n "${tcp_port_info}" ] && [ -n "${udp_port_info}" ]
    then
        echo_result "${tcp_port_info}"
        echo_result "${udp_port_info}"
    elif [ -n "${tcp_port_info}" ]
    then
        echo_result "${tcp_port_info}"
    elif [ -n "${udp_port_info}" ]
    then
        echo_result "${udp_port_info}"
    fi
}

if [ -z "${port}" ]
then
    echo "没有指定端口。"
    echo -e "脚本执行方法：\n    bash $0 端口号"
else
    check_port ${port}
fi