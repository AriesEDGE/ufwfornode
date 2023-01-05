import socket
import threading
import os

##系统依赖（自行安装：ufw,python3
##如果不需要ufw，而使用其他防火墙管理软件，请自行修改命令
##os.system ("sudo ufw allow from "+address[0]+" to any port "+port)

port = "22358" ##节点端口
print ("自动白名单服务器监听开启")
server = socket.socket()
server.bind(("0.0.0.0",8080)) 
server.listen()
while True:
    conn,address = server.accept()
    print(address)
    thread = threading.Thread(args=conn)
    thread.start()
    thread.join()
    r = os.system ("sudo ufw allow from "+address[0]+" to any port "+port)
    response_header = "HTTP/1.1 200 OK\r\n"
    response_header += "Content-Type: text/html; charset=utf-8\r\n"
    response_header += "\r\n"
    response_body = "<h1> UniOreoX 自动白名单系统</h1>"
    response_body += "<p>你的IP地址是："
    response_body += str(address[0])
    response_body += "</p>"
    response_body += "<p> IP白名单添加成功，脚本来源 TG@aries_init，技术支持 油腻 @UniOreoY</p>"
    response = response_header + response_body
    conn.send(response.encode("utf-8"))
    conn.close()
server.close()

