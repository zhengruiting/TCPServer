# import sys
# from PyQt4.QtCore import *
# from PyQt4.QtGui import *
# from PyQt4.QtNetwork import *
# from PyQt5.QtCore import QByteArray, QDataStream, QIODevice, Qt
# from PyQt5.QtNetwork import QTcpServer, QHostAddress
# from PyQt5.QtWidgets import QApplication, QPushButton
#
# PORT = 9999
# SIZEOF_UINT32 = 4
#
#
# def SIGNAL(param):
#     pass
#
#
# class ServerDlg(QPushButton):
#
#     def __init__(self, parent=None):
#         super(ServerDlg, self).__init__(
#             "&Close Server", parent)
#         self.setWindowFlags(Qt.WindowStaysOnTopHint)
#
#         self.tcpServer = QTcpServer(self)
#         self.tcpServer.listen(QHostAddress("0.0.0.0"), PORT)
#         self.connect(self.tcpServer, SIGNAL("newConnection()"),
#                      self.addConnection)
#         self.connections = []
#
#         self.connect(self, SIGNAL("clicked()"), self.close)
#         font = self.font()
#         font.setPointSize(24)
#         self.setFont(font)
#         self.setWindowTitle("Server")
#
#     def addConnection(self):
#         clientConnection = self.tcpServer.nextPendingConnection()
#         clientConnection.nextBlockSize = 0
#         self.connections.append(clientConnection)
#
#         self.connect(clientConnection, SIGNAL("readyRead()"),
#                      self.receiveMessage)
#         self.connect(clientConnection, SIGNAL("disconnected()"),
#                      self.removeConnection)
#         self.connect(clientConnection, SIGNAL("error()"),
#                      self.socketError)
#
#     def receiveMessage(self):
#         for s in self.connections:
#             if s.bytesAvailable() > 0:
#                 stream = QDataStream(s)
#                 stream.setVersion(QDataStream.Qt_4_2)
#
#                 if s.nextBlockSize == 0:
#                     if s.bytesAvailable() < SIZEOF_UINT32:
#                         return
#                     s.nextBlockSize = stream.readUInt32()
#                 if s.bytesAvailable() < s.nextBlockSize:
#                     return
#
#                 textFromClient = stream.readQString()
#                 s.nextBlockSize = 0
#                 self.sendMessage(textFromClient,
#                                  s.socketDescriptor())
#                 s.nextBlockSize = 0
#
#     def sendMessage(self, text, socketId):
#         for s in self.connections:
#             if s.socketDescriptor() == socketId:
#                 message = "You> {}".format(text)
#             else:
#                 message = "{}> {}".format(socketId, text)
#             reply = QByteArray()
#             stream = QDataStream(reply, QIODevice.WriteOnly)
#             stream.setVersion(QDataStream.Qt_4_2)
#             stream.writeUInt32(0)
#             stream.writeQString(message)
#             stream.device().seek(0)
#             stream.writeUInt32(reply.size() - SIZEOF_UINT32)
#             s.write(reply)
#
#     def removeConnection(self):
#         pass
#
#     def socketError(self):
#         pass
#
#
# app = QApplication(sys.argv)
# form = ServerDlg()
# form.show()
# form.move(0, 0)
# app.exec_()


#折旧年限


# class Data_test2(object):
#     day=0
#     month=0
#     year=0
#     def __init__(self,year=0,month=0,day=0):
#         self.day=day
#         self.month=month
#         self.year=year
#     @classmethod
#     def get_date(cls,data_as_string):
#
#         #这里第一个参数是cls， 表示调用当前的类名
#
#         year,month,day=map(int,data_as_string.split('-'))
#         date1=cls(year,month,day)     #返回的是一个初始化后的类
#         return date1
#
#     def out_date(self):
#         print("year :",self.year)
#         print("month :",self.month)
#         print("day :",self.day)
#
# r=Data_test2.get_date("2020-1-1")
#
# r.out_date()





# num = int(input("输入一个数字: "))
# if (num % 2) == 0:
#     print("{0} 是偶数".format(num))
# else:
#     print("{0} 是奇数".format(num))

a = int(input("输入第一个数字: "))
b = int(input("输入第二个数字: "))
if a>b:
    print("最大的数:",a)
elif a == b:
    print("相等")
else:
    print("最大的数:",b)
