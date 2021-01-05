import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow
from Zhengbing.VHF_PY.VHF import Ui_MainWindow
from Zhengbing.MyClient.ClientThread.MyThread import MyClientThread

# 窗体宽高
widgetWidth = 500
widgetHeight = 500
# client_to_server = [("127.0.0.1", 8889), ("127.0.0.1", 8888)]
client_to_server = [("127.0.0.1", 8889)]
myhostclientList = []


class HostClientWidget(QMainWindow):
    closeSingle = pyqtSignal()
    runing_single = pyqtSignal(str)
    def __init__(self):
        super(HostClientWidget, self).__init__()
        # 调用QtDesigner生成的界面有两种方式
        # 1.将生成的ui文件转为py文件
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 初始化
        self.my_init()

    def my_init(self):
        # 开始运行菜单里面只有搜索网络可用
        self.ui.action_2.setEnabled(True)
        self.ui.action_12.setEnabled(False)
        self.ui.action_13.setEnabled(False)
        # 运行菜单不同动作触发不同信号，通过传入的字符串来判断是哪个项被单击了
        self.ui.action_2.triggered.connect(self.find_network)
        self.ui.action_2.triggered.connect(lambda: self.runing_single.emit("FIND"))
        self.ui.action_12.triggered.connect(lambda: self.runing_single.emit("RF_ON"))
        self.ui.action_13.triggered.connect(lambda: self.runing_single.emit("RF_OFF"))

    # 主控机客户端
    def find_network(self):
        self.handle_host_client()
        self.ui.action_12.setEnabled(True)
        self.ui.action_13.setEnabled(True)
    # 主控电脑客户机----用run来实现多线程
    def handle_host_client(self):
        for ip, port in client_to_server:
            # 创建线程
            self.myhostclient = MyClientThread(ip, port)
            myhostclientList.append(self.myhostclient)
            # 开始线程
            self.myhostclient.start()
            self.runing_single.connect(self.myhostclient.handle_runing_single)
            self.myhostclient.finished.connect(self.myhostclient.deleteLater)
            self.closeSingle.connect(self.myhostclient.winClose)

    def closeEvent(self, CloseEvent):
        self.closeSingle.emit()
        CloseEvent.accept()

    def __del__(self):
        self.myhostclient.deleteLater


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = HostClientWidget()
    widget.show()
    sys.exit(app.exec_())
