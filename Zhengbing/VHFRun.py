import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from numpy.distutils.fcompiler import pg

from Zhengbing.VHF_PY.VHF import Ui_MainWindow
from Zhengbing.mythread.MythreadRun import MyThread
class MyWidget(QMainWindow):
    def __init__(self):
        self.ui = uic.loadUi("../VHF2.ui")
        self.ui.splitter_2.setStretchFactor(1, 5)
        self.pw = pg.PlotWidget()
        self.pw.setBackground("r")

        hour = [1,2,3,4]
        mm = [20,40,50,10]
        self.pw.plot(hour,mm)
        self.ui.horizontalLayout_5.addWidget(self.pw)

        self.ui.setStyleSheet("#tab_4 > QLabel:hover{ background:blue }")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    # widget.ui.show()
    widget.ui.setStyleSheet("QLabel { background:gray;color:blue }")
    widget.ui.show()
    sys.exit(app.exec_())









