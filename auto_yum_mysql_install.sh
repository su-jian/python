#!/bin/bash
#要实现切换目录的功能用 source 脚本名

#挂载光盘
#自动搭建本地YUM

# read -p 请输入挂载点： $1 
mount_point=/mnt  #取第一个位置变量的值作为挂载点
yum_conf_file=/etc/yum.repos.d/auto_config_yum.repo

ls -d ${mount_point} &> /dev/null || mkdir -p ${mount_point}
 #查看挂载点是否存在，若不存在则创建挂载点
mount /dev/sr0 /mnt &> /dev/null
if ls -d ${mount_point}/Packages &> /dev/null #每个挂载点下都有目录Packages，因此查看挂载点下的Packages来确定是否挂载成功
then
    ls -d /etc/yum.repos.d/bak &> /dev/null || mkdir /etc/yum.repos.d/bak #查看目录bak是否存在，若不存在则创建
    mv /etc/yum.repos.d/*.repo /etc/yum.repos.d/bak
    > ${yum_conf_file}
    cat << eof >> ${yum_conf_file}
[local_yum]
name=local yum
baseurl=file://${mount_point}
gpgcheck=0
enabled=1
eof
 
    yum clean all &> /dev/null
    echo "搭建完成。"
else
    mount /dev/sr0 ${mount_point} &> /dev/null
    mv /etc/yum.repos.d/*.repo /etc/yum.repos.d/bak
    > ${yum_conf_file}
    cat << eof >> ${yum_conf_file}
[local_yum]
name=local yum
baseurl=file://${mount_point}
gpgcheck=0
enabled=1
eof
 
    yum clean all &> /dev/null
    echo "搭建完成。"
fi

mount /dev/sr0 /mnt

#以下是检查软件gcc gcc-c++ make ncurses-devel有没有安装

for software in expect gcc gcc-c++ make ncurses-devel lftp
do
    if ! rpm -q ${software}
    then  
        yum install -y ${software}
    fi
done

#以下是在ftp上下载需要的安装包
cd /tmp
lftp 172.16.1.1 << eof
cd mysql
get boost_1_59_0.tar.gz cmake-3.6.2.tar.gz mysql-5.7.14.tar.gz
quit
eof

#编译安装cmake

tar xf /tmp/cmake-3.6.2.tar.gz -C /usr/local/src/
cd /usr/local/src/cmake-3.6.2/
if ./bootstrap && make && make install
then 
    echo "编译安装cmake成功！"
fi

#编译安装mysql上传boost_1_59_0.tar.gz到linux上，例如上传到/usr/local/src
cp /tmp/boost_1_59_0.tar.gz  /usr/local/src
groupadd mysql
useradd -r -g mysql -s /bin/false mysql
tar xf /tmp/mysql-5.7.14.tar.gz -C /usr/local/src/
cd /usr/local/src/mysql-5.7.14
cmake . -DWITH_BOOST=/usr/local/src 
make
make install
cd /usr/local/mysql 
bin/mysqld --initialize --datadir=/mydata --user=mysql 

#修改mysql的配置文件
sed -ri 's/datadir=.+/datadir=\/mydata/' /etc/my.cnf 
sed -ri 's/socket=.+/socket=\/mydata\/mysql.sock/' /etc/my.cnf 
sed -ri 's/log-error=.+/log-error=\/var\/log\/mysqld.log/' /etc/my.cnf 
sed -ri 's/pid-file=.+/pid-file=\/mydata\/mysqld.pid/' /etc/my.cnf 
echo "编译安装mysql"

#启动mysql
cd  /usr/local/mysql
expect -c "
    spawn bin/mysqld_safe --user=mysql  
    expect {
        \"* Starting mysqld daemon with databases from /mydata\" {send \"\r\" ; exp_continue}
    }  
"
if netstat -an | grep :3306
then
    echo "mysql启动成功！" 
else
    echo "mysql启动失败！"        
fi

#破解密码，实现无密码登录mysql

process=$(ps -ef | grep mysql | grep "^mysql" | awk '{print $2,$3}')
kill -9 ${process}
sed -ri '/symbolic-links=0/a skip-grant-tables' /etc/my.cnf
#重新启动mysql
cd  /usr/local/mysql
expect -c "
    spawn bin/mysqld_safe --user=mysql  
    expect {
        \"*mysqld daemon with databases from /mydata\" {send \r ; exp_continue}
    }  
"
#实现无密码登录mysql
expect -c "
    spawn bin/mysql -uroot -p -S /mydata/mysql.sock
    expect {
        \"*Enter password:\" {send \"\r\" ; exp_continue}
    }  
"

echo "mysql安装成功，现在可以实现无密码登录"

