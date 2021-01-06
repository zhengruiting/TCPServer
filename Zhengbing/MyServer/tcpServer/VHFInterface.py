import sys

from Zhengbing.MyServer import dealmm
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow
from Zhengbing.MyServer.mySource import interface
from  Zhengbing.MyServer.MyQTcpServer.MyQTcpServer import MyQTcpServer
# address_server = [("192.168.1.105",8888),("127.0.0.1",8888)]
address_server = [("127.0.0.1",8888)]
serverList=[]
class HostClientWidget(QMainWindow):
    msgSingle = pyqtSignal(str)
    def __init__(self):
        super(HostClientWidget, self).__init__()
        self.my_qtcpserver=None
        # 调用QtDesigner生成的界面有两种方式
        # 1.将生成的ui文件转为py文件
        self.ui = interface.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda :self.msgSingle.emit(self.ui.lineEdit.text()))
        # self.ui.pushButton.clicked.connect(self.mm)
        for ip,port in address_server:
            self.my_qtcpserver = MyQTcpServer(ip,port)
            self.msgSingle.connect(self.my_qtcpserver.handle_msgSingle)
            serverList.append(self.my_qtcpserver)
        address_server.clear()

    def mm(self):
        msg = self.ui.lineEdit.text()
        self.msgSingle.emit(msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = HostClientWidget()
    widget.show()
    sys.exit(app.exec_())


