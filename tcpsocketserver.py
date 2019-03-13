from socketserver import BaseRequestHandler, TCPServer


class MyServerHandler(BaseRequestHandler):
    '''继承socketserver模块中的BaseRequestHandler，并重写handel方法。此tcp服务器属于半双工通信方式'''
    def handle(self):
        while True:
            self.recv_data = self.request.recv(1024)
            print('{0}发送的消息。'.format(self.client_address[0]))
            print(self.recv_data.decode('gbk', 'strict'))
            if not self.recv_data:
                print('客户端请求关闭。')
                break
            self.send_data = input('请服务器发送消息：')
            self.request.send('服务器回送消息:{0}'.format(self.send_data).encode('gbk', 'strict'))


# 创建tcpserver的服务套接字
serversocket = TCPServer(('192.168.74.1', 8800), MyServerHandler)
# 调用TCPServer的server_forever方法使其处于一直服务状态
serversocket.serve_forever()
serversocket.server_close()
