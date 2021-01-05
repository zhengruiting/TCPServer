import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal, QObject, QThread
from Zhengbing.tcp.TcpServerObject import MyTcpServer

from Zhengbing.DealLogic.Logic import FindNetwork
from Zhengbing.VHF_PY.VHF import Ui_MainWindow
from Zhengbing.mythread.MyClinetThreadObject import MyClientThread

# 窗体宽高
widgetWidth = 500
widgetHeight = 500
IP = "0.0.0.0"
PORT = 8888
# 服务器绑定的地址
# server_address = [("127.0.0.1", 8888)]

# 客户端连接主机的地址
# client_to_server = [("127.0.0.1", 8889), ("127.0.0.1", 8888)]
client_to_server = [("127.0.0.1", 8889)]
# client_to_server = [("192.168.1.110", 8888)]
tcpserverList = []

clientList = []


# 主控电脑的客户端
class HostClientWidget(QMainWindow):
    runing_single = pyqtSignal(str)  # 自定义信号---运行菜单项里面的动作触发信号
    closeSingle = pyqtSignal()  # 自定义信号---关闭时触发
    myclientSingle = pyqtSignal()  # 自定义信号---客户端连接时触发开始线程信号

    def __init__(self):
        super(HostClientWidget, self).__init__()
        # 调用QtDesigner生成的界面有两种方式
        # 1.将生成的ui文件转为py文件
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #初始化
        self.my_init()

    def my_init(self):
        # 开始运行菜单里面只有搜索网络可用
        self.ui.action_2.setEnabled(True)
        self.ui.action_12.setEnabled(False)
        self.ui.action_13.setEnabled(False)
        self.handle_client()


        # 运行菜单不同动作触发不同信号，通过传入的字符串来判断是哪个项被单击了
        # self.ui.action_2.triggered.connect(self.find_network)
        # self.ui.action_12.triggered.connect(lambda: self.runing_single.emit("RF_ON"))
        # self.ui.action_13.triggered.connect(lambda: self.runing_single.emit("RF_OFF"))


    # # 点击菜单里面的搜索网络，客户端主动连接服务器，
    # def find_network(self):
    #     self.handle_client()
    #     # self.runing_single.emit("find_network")
    # # 主控电脑客户机----用继承Qobject的方式来实现多线程
    def handle_client(self):
        for ip, port in client_to_server:
            # 有几个服务器，那么客户端连接时就创建几个线程
            # 1.实例化自定义的客户端线程
            self.myclientthread = MyClientThread(ip, port)
            # 2、创建一个线程用来处理所有客户端线程
            self.clientthread = QThread(self)

            # 将线程保存，避免这个函数循环结束销毁变量
            clientList.append((self.myclientthread, self.clientthread))
            # 3.移动客户端到子线程
            self.myclientthread.moveToThread(self.clientthread)
            # 连接触发客户端子线程的信号和曹
            self.myclientSingle.connect(self.myclientthread.handle_client)
            self.clientthread.finished.connect(self.clientthread.deleteLater)

            # 当客户机软件点击右上角×时，触发信号执行函数，释放客户端套接字资源
            self.closeSingle.connect(self.myclientthread.dealDisconnected)
            #
            # # 运行菜单对应动作触发的信号连接到响应的槽函数
            # self.runing_single.connect(self.myclientthread.deal_run_single)
            #
            self.clientthread.start()  # 启动线程但没有开始线程
            self.myclientSingle.emit()





    def closeEvent(self, event):
        self.closeSingle.emit()
        # for a,b in clientList:
        #     if b.isRunning():
        #         b.deleteLater()
        #     else:
        #         pass
        event.accept()


# class MyWidget(QMainWindow):
#     runing_single = pyqtSignal(str)  # 自定义信号---运行菜单项里面的动作触发信号
#     closeSingle = pyqtSignal()  # 自定义信号---关闭时触发
#     myclientSingle = pyqtSignal()  # 自定义信号---客户端连接时触发开始线程信号
#
#     def __init__(self):
#         super(MyWidget, self).__init__()
#         # 调用QtDesigner生成的界面有两种方式
#         # 1.将生成的ui文件转为py文件
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#         # 2.直接加载ui文件----这种方式重写close方法好像没效果
#         # self.ui = uic.loadUi("./Zhengbing/VHF/VHF.ui")
#         self.my_init()
#
#     def my_init(self):
#         # 开始运行菜单里面只有搜索网络可用
#         self.ui.action_2.setEnabled(True)
#         self.ui.action_12.setEnabled(False)
#         self.ui.action_13.setEnabled(False)
#         # 运行菜单不同动作触发不同信号，通过传入得字符串来判断是哪个项被单击了
#         self.ui.action_2.triggered.connect(self.find_network)
#         self.ui.action_12.triggered.connect(lambda: self.runing_single.emit("RF_ON"))
#         self.ui.action_13.triggered.connect(lambda: self.runing_single.emit("RF_OFF"))
#         # self.handle_client()
#
#     # 点击菜单里面的搜索网络，客户端主动连接服务器，
#     def find_network(self):
#         self.handle_client()
#         self.runing_single.emit("find_network")
#         self.ui.action_12.setEnabled(True)
#         self.ui.action_13.setEnabled(True)
#
#     # 主控电脑客户机
#     def handle_client(self):
#         for ip, port in client_to_server:
#             # 有几个服务器，那么客户端连接时就创建几个线程
#             # 1.实例化客户端
#             myclientthread = MyClientThread(ip, port)
#             # 2、创建一个线程用来处理所有客户端线程
#             clientthread = QThread(self)
#             clientList.append((myclientthread, clientthread))
#             # 3.移动客户端到子线程
#             myclientthread.moveToThread(clientthread)
#             # 连接触发客户端子线程的信号和曹
#             self.myclientSingle.connect(myclientthread.handle_client)
#             # 当客户机软件点击右上角×时，触发信号执行函数，释放客户端套接字资源
#             self.closeSingle.connect(myclientthread.handle_close)
#
#             # 运行菜单对应动作触发的信号连接到响应的槽函数
#             self.runing_single.connect(myclientthread.deal_run_single)
#
#             clientthread.start()  # 启动线程但没有开始线程
#             self.myclientSingle.emit()
#
#     # 服务机
#     def handle_server(self):
#         for ip, port in server_address:
#             # 这里必须要用self,不然类执行完tcpserver就释放了内存，导致客户端无法连接
#             self.tcpserver = MyTcpServer(ip, port)
#
#     def __del__(self):
#         print("主程序退出，释放内存-----del")
#
#     def closeEvent(self, event):
#         self.closeSingle.emit()
#         event.accept()
#
#     #     self.findnetwork()
#     #
#     # #处理菜单中搜索网络动作
#     # def findnetwork(self):
#     #     self.find_network = FindNetwork(IP,PORT)
#     #     self.ui.action_2.triggered.connect(self.find_network.startServer)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = HostClientWidget()
    # widget.ui.show()
    widget.show()
    sys.exit(app.exec_())
