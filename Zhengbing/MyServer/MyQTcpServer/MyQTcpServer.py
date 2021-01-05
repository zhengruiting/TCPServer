from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtNetwork import QTcpServer, QHostAddress
from Zhengbing.MyServer.MyThrd.MyThrd import MyThrd


class MyQTcpServer(QTcpServer):
    msgSingle4 = pyqtSignal(str)
    def __init__(self, ip, port):
        super(MyQTcpServer, self).__init__()
        self.ip = ip
        self.mythread = None
        self.port = port
        if (self.isListening()):
            print("连接正在运行")
        else:
            self.listen(QHostAddress(self.ip), self.port)
        print("aaaaaaaaaaaaaa")
    def handle_msgSingle(self,msg):
        self.msgSingle4.emit(msg)

    def incomingConnection(self,sip_voidptr):
        print("新的连接进入")
        self.mythread = MyThrd(sip_voidptr)
        # self.msgSingle4.connect(self.mythread.handle_write1)
        self.mythread.finished.connect(self.mythread.deleteLater)
        self.mythread.start()


if __name__ == '__main__':
    pass