import sys
from PyQt5.QtCore import QObject, QThread
from PyQt5.QtNetwork import QTcpSocket


# 处理收发消息
def dealRecvMsgE(tcpSocket):
    readData = tcpSocket.readAll()
    print(readData)
    tcpSocket.write(readData)


# 断开连接
def dealDisconnect(tcpSocket):
    ip = tcpSocket.peerAddress().toString()
    port = str(tcpSocket.peerPort())
    print("主机:" + ip + ";端口：" + port + "断开连接")
    tcpSocket.disconnectFromHost()  # 断开主机
    tcpSocket.close()  # 这个关闭连接

socktList = []
# 线程开始的地方
class MyTcpThread(QObject):
    def __init__(self, sip_voidptr):
        super(MyTcpThread, self).__init__()
        self.socket = sip_voidptr
        print("这是线程里面", QThread.currentThread())

    # 处理每一个客户端连接
    def dealSocket(self):
        tcpSocket = QTcpSocket()#通信套接字
        if tcpSocket.setSocketDescriptor(self.socket):
            socktList.append(tcpSocket)
            # QTcpSocket缓存接收到新的数据时触发readyRead
            tcpSocket.readyRead.connect(lambda: dealRecvMsgE(tcpSocket))
            # 断开连接时
            tcpSocket.disconnected.connect(lambda: dealDisconnect(tcpSocket))
        else:
            print("出错了")
