from PyQt5.QtCore import QThread, QObject,Qt
from PyQt5.QtNetwork import QTcpSocket
import time

# # 处理收发消息
# def dealRecvMsgE(tcpSocket):
#     print("alllllllllllllllllll")
#     readData = tcpSocket.readAll()
#     print(readData)
#     tcpSocket.write(readData)
#
#
# # 断开连接
# def dealDisconnect(tcpSocket):
#     ip = tcpSocket.peerAddress().toString()
#     port = str(tcpSocket.peerPort())
#     print("主机:" + ip + ";端口：" + port + "断开连接")
#     tcpSocket.disconnectFromHost()  # 断开主机
#     tcpSocket.close()  # 这个关闭连接



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

class MyThread(QThread):
    def __init__(self, sip_voidptr):
        super(MyThread, self).__init__()
        self.socket = sip_voidptr

    def run(self):
        tcpSocket = QTcpSocket()
        print("处理线程", QThread.currentThread())
        if tcpSocket.setSocketDescriptor(self.socket):
            # QTcpSocket缓存接收到新的数据时触发readyRead
            tcpSocket.readyRead.connect(lambda: dealRecvMsgE(tcpSocket),Qt.DirectConnection)
            # 断开连接时
            tcpSocket.disconnected.connect(lambda:dealDisconnect(tcpSocket),Qt.DirectConnection)
        else:
            print("出错了")
        #因为涉及到线程，这里需要执行这个函数，循环监听(Qt的事件循环)
        self.exec()

if __name__ == '__main__':
    pass
