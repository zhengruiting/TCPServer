from PyQt5.QtNetwork import QTcpServer, QHostAddress
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from Zhengbing.mythread.MyThreadObject import MyTcpThread


# 线程开始的地方
class MyTcpServer(QTcpServer):
    startThreadSignal = pyqtSignal()  # 定义一个信号
    def __init__(self, ip, port):
        super(MyTcpServer, self).__init__()
        if self.isListening():
            print("连接正在运行")
        else:
            self.listen(QHostAddress(ip), port)

    # 这里每个变量前面都要加self
    def incomingConnection(self, sip_voidptr):
        print("有新的连接进入")
        self.thread = QThread()  # 创建一个线程
        self.tcpthread = MyTcpThread(sip_voidptr)

        self.tcpthread.moveToThread(self.thread)  # 将线程移动

        # 进入线程处理
        self.startThreadSignal.connect(self.tcpthread.dealSocket)
        self.thread.start()  # 这里只是开启了线程，但并未执行
        self.startThreadSignal.emit()  # 这里才开始触发信号执行
if __name__ == '__main__':
    pass
