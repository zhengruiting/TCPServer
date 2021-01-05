# from PyQt5 import sip
from PyQt5.QtNetwork import QTcpServer, QHostAddress
from Zhengbing.mythread.MythreadRun import MyThread


class MyTcpServer(QTcpServer):
    def __init__(self, ip, port):
        super(MyTcpServer, self).__init__()
        self.ip = ip
        self.port = port
        if (self.isListening()):
            print("连接正在运行")
        else:
            self.listen(QHostAddress(self.ip), self.port)

    def incomingConnection(self,sip_voidptr):
        print("有新的连接进入")
        self.thread = MyThread(sip_voidptr)

        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()


    def __del__(self):
        pass

if __name__ == '__main__':
    pass

# class MyTcpServer(QObject):
#     def __init__(self, ip, port):
#         super(MyTcpServer, self).__init__()
#         self.tcpserver = QTcpServer()
#         self.tcpserver.incomingConnection = self.incomingConnection
#         if (self.tcpserver.isListening()):
#             print("连接正在运行")
#         else:
#             self.tcpserver.listen(QHostAddress(ip), port)
#         # self.tcpserver.newConnection.connect(lambda: self.dealRead(self.tcpserver))
#
#     def incomingConnection(self, sip_voidptr):
#
#         self.thread2 = MyThread(sip_voidptr)
#         self.thread2.start()
#
#
#     def dealRead(self, tcpserver):
#         # 获取通信套接字
#         tcpsocket = tcpserver.nextPendingConnection()
#         print("1111111111111111")
#         ip = tcpsocket.peerAddress().toString()
#         print("22222222222222222")
#         port = tcpsocket.peerPort()
#         print("4444444444444444444444")
#         name = tcpsocket.peerName()
#         print("333333333333")
#         print(ip, port, name)
