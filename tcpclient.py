from socket import *
BUFSIZ = 1024
SERVER_IP = '192.168.74.1'
SERVER_PORT = 8880
SERVER_ADDR = (SERVER_IP,SERVER_PORT)
tcpclientsocket = socket(AF_INET, SOCK_STREAM)
tcpclientsocket.connect(SERVER_ADDR)
print('已连接。。。')
while True:
    mes = input('请你输入您要发送的消息：')
    if not mes:
        print('客户端请求关闭！')
        break
    tcpclientsocket.send(mes.encode(encoding='gbk', errors='strict'))
    print('已发送。。。')
    res = tcpclientsocket.recv(BUFSIZ)
    if not res:
        print('服务器请求关闭!')
        break
    print('服务器发送的消息是：{0}'.format(res.decode(encoding='gbk', errors='strict')))
tcpclientsocket.close()
print('已关闭！')



