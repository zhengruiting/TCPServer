from PyQt5.QtNetwork import QTcpSocket, QHostAddress


class MyTcpSocket(QTcpSocket):
    def __init__(self, ip, port):
        super(MyTcpSocket, self).__init__()
        self.ip = ip
        self.port = port
        self.connectToHost(QHostAddress(self.ip), self.port)
        self.connected.connect(lambda: print("连接成功"))
        self.disconnected.connect(self.dealDisconnected)
        # self.readyRead.connect(self.handle_read)

    # 处里服务器发送过来的信息
    def handle_read(self):
        msg = self.readAll()
        print(msg)
        self.write("zhengbing".encode("utf-8"))

    # 处理客户机发送给服务器的信息
    def handle_write(self, msg):
        self.write(msg.encode("utf-8"))

    # 断开连接
    def dealDisconnected(self):
        while self.state() > 0:
            print("断开连接")
            self.disconnectFromHost()
            self.close()
            self.deleteLater()
        else:
            print(self.state())

if __name__ == '__main__':
    MyTcpSocket("127.0.0.1", 8888)
