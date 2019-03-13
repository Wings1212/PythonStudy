from socket import *
BUFSIZ = 1024
SERVER_IP = '192.168.74.1'
SERVER_PORT = 8880
SERVER_ADDR = (SERVER_IP, SERVER_PORT)
tcpserversocket = socket(AF_INET, SOCK_STREAM)
tcpserversocket.bind(SERVER_ADDR)
tcpserversocket.listen(128)
print('已开启监听。。')
while True:
    tcpclientsocket, client_addr = tcpserversocket.accept()
    get_mes = tcpclientsocket.recv(BUFSIZ)
    if not get_mes:
        print('客户端请求关闭')
        break
    print('服务器接收的消息是：{0}'.format(get_mes.decode(encoding='gbk', errors='strict')))
    send_mes = input('请输入你往客户端发送的消息：')
    if not send_mes:
        print('服务器请求关闭')
        break
    tcpclientsocket.send(send_mes.encode(encoding='gbk', errors='strict'))
tcpserversocket.close()
print('已关闭！')
