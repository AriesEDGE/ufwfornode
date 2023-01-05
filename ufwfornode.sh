#! /bin/bash

#环境安装
update(){
    sudo apt update
    sudo apt install python3 python3-pip -y
    sudo apt-get install ufw
    clear
    echo "这一步选y就行"
    sudo ufw enable
    sudo ufw default deny
    sudo ufw allow ssh #激活SSH端口
    clear
}

#白名单py
down(){
    #作者TG@unioreox TG频道@unichannelx
    wget -O whitelist.py https://ghproxy.com/github.com/AriesEDGE/AriesEDGE/releases/download/v3ss/autowhite.py
    clear
}

#Main 
rm -rf whitelist.py 
echo "安装依赖环境"
update
down

#节点端口
echo "请输入你的节点的端口"
read ports
sed -i "s/22358/${ports}/g" whitelist.py

#认证端口
echo "请输入认证端口"
read authport
sudo ufw allow ${authport}
sed -i "s/8080/${authport}/g" whitelist.py

clear
echo "你的白名单网址为`curl ip.sb`:${authport}"
echo "此时UFW防火墙已经激活，默认放行SSH端口，以及节点跟认证端口，其他端口请自行放行"

nohup python3 -u whitelist.py > whitelist_out.out 2>&1 &
