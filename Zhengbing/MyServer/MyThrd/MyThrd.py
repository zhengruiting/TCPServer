from PyQt5.QtCore import QThread, Qt, pyqtSignal
from PyQt5.QtNetwork import QTcpSocket

socketList = []

def dealRecvMsgE(tcpSocket):
    readData = tcpSocket.readAll()
    print(readData)
# 断开连接
def dealDisconnect(tcpSocket):
    ip = tcpSocket.peerAddress().toString()
    port = str(tcpSocket.peerPort())
    print("主机:" + ip + ";端口：" + port + "断开连接")
    tcpSocket.disconnectFromHost()  # 断开主机
    tcpSocket.close()  # 这个关闭连接
    print(socketList)
    socketList.remove(tcpSocket)
    print(socketList)


class MyThrd(QThread):
    msgSingle = pyqtSignal(str)
    def __init__(self,sip_voidptr):
        super(MyThrd, self).__init__()
        self.tcpSocket = None
        self.msg = None
        self.sock = sip_voidptr

    def run(self):
        self.tcpSocket = QTcpSocket()
        if self.tcpSocket.setSocketDescriptor(self.sock):
            # QTcpSocket缓存接收到新的数据时触发readyRead
            self.tcpSocket.readyRead.connect(lambda:dealRecvMsgE(self.tcpSocket),Qt.DirectConnection)
            # 断开连接时
            self.tcpSocket.disconnected.connect(lambda: self.dealDisconnect(self.tcpSocket), Qt.DirectConnection)
            socketList.append(self.tcpSocket)

            self.msgSingle.connect(self.handle_accept_msg)
            self.finished.connect(self.deleteLater)
        else:
            print("出错了")
        # 因为涉及到线程，这里需要执行这个函数，循环监听(Qt的事件循环)
        self.exec()
    def handle_accept_msg(self,msg):
        for socket in socketList:
            socket.write(msg.encode("utf-8"))
            socket.flush()

    def handle_write1(self,msg):
        print("连接时套接字",socketList)
        self.msg = msg
        self.msgSingle.emit(msg)
    # def dealRecvMsgE(self,tcpSocket):
    #     readData = tcpSocket.readAll()
    #     print(readData)
    # 断开连接
    def dealDisconnect(self,tcpSocket):
        ip = tcpSocket.peerAddress().toString()
        port = str(tcpSocket.peerPort())
        print("主机:" + ip + ";端口：" + port + "断开连接")
        tcpSocket.disconnectFromHost()  # 断开主机
        tcpSocket.close()  # 这个关闭连接
        socketList.remove(tcpSocket)
        print("线程退出")
        self.exit()#退出这一个线程




if __name__ == '__main__':
    pass
