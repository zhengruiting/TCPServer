from PyQt5.QtCore import QObject, pyqtSignal
from Zhengbing.tcp.TcpClientObject import MyTcpSocket

clientList = []
class MyClientThread(QObject):
    closeSingle = pyqtSignal()

    def __init__(self, ip, port):
        super(MyClientThread, self).__init__()
        self.ip = ip
        self.port = port

    def handle_client(self):
        self.client = MyTcpSocket(self.ip, self.port)
        clientList.append(self.client)
        # self.closeSingle.connect(self.client.dealDisconnected)

    def deal_run_single(self, str):
        if str == "find_network":
            pass
        elif str == "RF_ON":
            print("射频开电")
        elif str == "RF_OFF":
            print("射频关电")
        else:
            pass

    # def handle_close(self):
    #     print("bbbbbbbbbbbbbb")
    #     self.closeSingle.emit()
    #     self.client.close()

    # 断开连接
    def dealDisconnected(self):
        while self.client.state() > 0:
            print("断开连接")
            self.client.disconnectFromHost()
            self.client.close()
            self.client.deleteLater()
        else:
            print(self.client.state())
