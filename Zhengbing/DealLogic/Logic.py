from Zhengbing.tcp.TcpServerObject import MyTcpServer
class FindNetwork(object):
    def __init__(self,ip,port):
        self.ip=ip
        self.port =port
    def startServer(self):
        print("开始网络服务")
        self.tcpserver = MyTcpServer(self.ip,self.port)



if __name__ == '__main__':
    pass
