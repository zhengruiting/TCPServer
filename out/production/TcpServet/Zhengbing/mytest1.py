# import sys
#
# from PyQt5 import uic
# from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow
# import pyqtgraph as pg
#
# class WID(QMainWindow):
#     def __init__(self):
#         self.ui = uic.loadUi("../VHF2.ui")
#         self.pw = pg.PlotWidget()
#         self.pw.setBackground("b")
#
#
#         hour = [1,2,3,4]
#         mm = [20,40,50,10]
#         self.pw.plot(hour,mm)
#         self.ui.horizontalLayout_5.addWidget(self.pw)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     w = WID()
#     w.ui.show()
#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
# from VHFObject import MyWidget
# import multiprocessing
#
# class MyWidget(QMainWindow):
#     def __init__(self):
#         super(MyWidget, self).__init__()
#     def closeEvent(self, event):
#         reply = QMessageBox.question(self,
#                                      '本程序',
#                                      "是否要退出程序？",
#                                      QMessageBox.Yes | QMessageBox.No,
#                                      QMessageBox.No)
#         if reply == QMessageBox.Yes:
#             event.accept()
#         else:
#             event.ignore()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     widget = MyWidget()
#     widget.show()
#     sys.exit(app.exec_())



class person(object):
    def __init__(self):
        pass
    def eat(self,m):
        def dogeat(self,m):
            m = m+1
            print(m)
            return m
        return dogeat

p=person()
p.eat(5)









