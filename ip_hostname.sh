#!/bin/bash
menu(){
	echo "************************menu********************"
	echo -e "\t\t\t 1.配置主机名"
	echo -e "\t\t\t 2.配置ip,子网掩码,dns服务器地址,网关"
	echo -e "\t\t\t 3.查看ip信息和主机名"
	echo -e "\t\t\t 4.退出"

}
####################
#配置主机名
host(){
	read -p "请输入你想要修改的主机名" name
	sed -i  "/HOSTNAME/c HOSTNAME=$name" /etc/sysconfig/network
	hostname $name
}
####################
#配置ip,网关,子网掩码,dns服务器地址
ip_get(){
	read -p "please input network card:" card
	read -p "please input ip address:" ip
	read -p "please input NETMAKS:" net
	read -p "please input GATEWAY:" get
	read -p "please input DNS1:" dns

	>ip.txt
	echo $ip >ip.txt
	cat ip.txt|egrep '\b([1-9]|[1-9][0-9]|1[01][0-9]|12[0-6])(\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}\b'
	aa=($(echo $?))
	if (( $aa == 0 ))
	then
        echo "the ip address is class A, $ip"
	else
        cat ip.txt|egrep '\b(12[89]|1[3-8][0-9]|19[01])(\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}\b'
        bb=($(echo $?))
        if (( $bb==0 ))
        then
            echo "the ip address is class B,$ip"
        else
            cat ip.txt|egrep '\b(19[2-9]|2[0-1][0-9]|22[0-3])(\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}\b'
            cc=($(echo $?))
            if (($cc==0))
            then
                echo "the ip address is class C,$ip"
            else
                echo "please input lawful ip address!"
                break;
            fi
        fi

	fi
	ping -c1  $ip &>/dev/null

	e=($(echo $?))
	if [[ $e == 0 ]]
	then
        echo "the ip address is useing,please input other ip address."
	else
        sed -i "{
		/IPADDR/c IPADDR=$ip
        	/NETMAKS/c NETMAKS=$net 
        	/GATEWAY/c GATEWAY=$get 
        	/DNS1/c DNS1=$dns 
                    }" /etc/sysconfig/network-scripts/ifcfg-$card
        service network restart &>/dev/null
		echo "successful"
	fi
}
###################
#查看ip信息和主机名
check(){
	read -p "请输入想要查看ip信息的网卡:" card
	IP=$(ifconfig $card|sed -rn "s/.*inet addr(\S+).*/\1/p")
	HOST=$(hostname)
	echo "ip address:$IP"
	echo "主机名:$HOST"
	echo "dns server is $(cat /etc/resolv.conf|tail -2)"
	echo "router ip is $(route -n|egrep "^0.0.0.0"|awk '{print $2}')"

}
######################
main(){
	clear
  	while true 
  	do
        menu
        read -p"  please input your choice(1-4) :" choice
        case $choice in
        1)
                host
                ;;
        2)
                ip_get
                ;;
        3)
                check
                ;;
        4)
                exit
                ;;
        *)    break;;

        esac
        read -p "         please put any key to continue " key
        clear
  	done
}
main	
	

