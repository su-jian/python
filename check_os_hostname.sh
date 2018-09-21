#!/bin/bash 

#检查OS和主机名

OS_name=$(uname)
var_num=$(uname -r)

host_name=$(hostname)
echo -e "该机OS：${OS_name}\n版本：${var_num}\n主机名：${host_name}"