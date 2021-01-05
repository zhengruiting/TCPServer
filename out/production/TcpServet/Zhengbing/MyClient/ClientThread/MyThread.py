from PyQt5.QtCore import QThread, Qt
from PyQt5.QtNetwork import QTcpSocket, QHostAddress

clientSocketList = []


class MyClientThread(QThread):
    def __init__(self, ip, port):
        super(MyClientThread, self).__init__()
        self.ip = ip
        self.port = port

    def run(self):
        print("新连接进入")
        self.clientSocket = QTcpSocket()

        self.clientSocket.connectToHost(QHostAddress(self.ip), self.port)
        clientSocketList.append((self.clientSocket, self.ip, self.port))
        self.clientSocket.connected.connect(lambda: print("连接成功"))

        self.clientSocket.readyRead.connect(lambda:self.handle_read(self.clientSocket),Qt.DirectConnection)

        self.clientSocket.disconnected.connect(self.dealDisconnected,Qt.DirectConnection)
        self.exec()

    def handle_read(self,socket):
        msg = socket.readAll()
        print(msg)
        self.handle_write()

    def handle_write(self):
        for socket, ip, port in clientSocketList:
            socket.write("郑兵".encode("utf-8"))

    def handle_runing_single(self, str):
        print(str)

    def dealDisconnected(self):
        print("断开连接")
        self.clientSocket.disconnectFromHost()
        self.clientSocket.close()
        self.clientSocket.deleteLater()

    def winClose(self):
        print("主窗口关闭了")
        for socket,ip,port in clientSocketList:
            print(socket)
        # self.clientSocket.disconnectFromHost()
        # self.clientSocket.close()
        # self.deleteLater()
        clientSocketList.clear()


if __name__ == '__main__':
    pass
