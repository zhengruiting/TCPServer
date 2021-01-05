from PyQt5.QtCore import QThread, Qt, pyqtSignal
from PyQt5.QtNetwork import QTcpSocket, QHostAddress

clientSocketList = []
class MyClientThread(QThread):
    #连接成功后，发送信号，与self.conSucced结合，用来判断连接是否成功
    cmdSingle = pyqtSignal()
    def __init__(self, ip, port):
        super(MyClientThread, self).__init__()
        self.ip = ip
        self.port = port
        self.clientSocket=None
        #用来接收软甲菜单点击时信号发送过来的字符串，帮助确认时哪个菜单被点击了
        self.recvcmd=None
        self.conSucced = False
    def run(self):
        print("新连接进入")
        #创建套接字
        self.clientSocket = QTcpSocket()
        #连接到服务器
        self.clientSocket.connectToHost(QHostAddress(self.ip), self.port)
        #保存客户端相关信息，后面发送数据需要用到
        clientSocketList.append((self.clientSocket, self.ip, self.port))
        #连接成功自动触发
        self.clientSocket.connected.connect(self.connectSucced)
        #读写数据，这里只用来读数据，写数据单独处理
        self.clientSocket.readyRead.connect(lambda :self.handle_read(self.clientSocket),Qt.DirectConnection)
        #服务器断开连接数自动触发
        self.clientSocket.disconnected.connect(self.dealDisconnected,Qt.DirectConnection)

        self.cmdSingle.connect(self.handle_running)
        self.exec()
    #当连接成功并且有菜单项被点击时处理
    def handle_running(self):
        print(self.conSucced)
        if self.conSucced:
            if self.recvcmd == "FIND":
                self.handle_write("搜索网络")
            elif self.recvcmd == "RF_ON":
                self.handle_write("射频开电")
            elif self.recvcmd == "RF_OFF":
                self.handle_write("射频关电")
            elif self.recvcmd == "STOP":
                self.handle_write("停止")
            else:
                pass
        else:
            pass
    #连接成功时将self.conSucced设置为Ture,同时self.cmdSingle通知槽函数处理
    def connectSucced(self):
        self.conSucced=True
        self.cmdSingle.emit()
    #处理读数据
    def handle_read(self,socket):
        msg = socket.readAll()
        print(msg)
        # self.handle_write("msg")
    #处理写数据
    def handle_write(self,mystr):
        for socket, ip, port in clientSocketList:
            socket.write(mystr.encode("utf-8"))
            #flush是为了让write写入到socket缓存的数据立刻发送出去
            socket.flush()
    #菜单项被点击时触发，str用来标志哪个菜单项被点击
    def handle_single(self,str):
        self.recvcmd = str
        print(str)
        #菜单项点击一次，就要触发一次，然后找到对应的处理
        self.cmdSingle.emit()



    def dealDisconnected(self):
        print("断开连接")
        for sockt,ip,port in clientSocketList:
            sockt.disconnectFromHost()
            sockt.close()
            sockt.deleteLater()
    def winClose(self):
        print("主窗口关闭了")
        clientSocketList.clear()



if __name__ == '__main__':
    pass
