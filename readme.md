# 节点加白自述

## 使用方法

```shell
bash <(curl -Ls https://github.com/AriesEDGE/ufwfornode/releases/download/real/ufw.sh)
```

# 说明

原理：

ufw防火墙监听白名单



# 注意事项

Python后台监听采用nohup



如果要关闭监听

请使用

`ps -ef|grep python`

查看进程号

杀掉进程

`kill -9 进程号`



查看认证IP的后台log

`cat ./whitelist_out.out`

或者

直接查看ufw当前规则

`ufw status`



**注意**

开启脚本后默认激活 UFW 防火墙，只放行SSH(22)端口与 authport 监听端口，其他端口请手动放行.

# Bug

1.加白后只能直连，无法使用CloudFlare CDN连接

2.部分地区的数据流量可能无法认证

3.双栈鸡获取认证页面会优先显示ipv6，主要是我直接调用了ip.sb的接口，是优先显示ipv6的，当然你用ipv6/ipv4:认证端口 都可用.

# 作者

shell一键作者：

​	Aries: TG频道 

[@aries_init]: https://t.me/aries_init

(写的很烂，大佬勿喷)



Python加白作者

​	UniOreoX： 

​	TG 

[@UniOreoX]: https://t.me/unioreox

​	TG频道: 

[@unichannelx]: https://t.me/unichannelx

油腻牛逼！