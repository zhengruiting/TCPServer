from PyQt5.QtCore import QObject, pyqtSignal

mystr = None

class myhh(object):
    msgS = pyqtSignal
    def __init__(self):
        super(myhh, self).__init__()
        self.msgS.connnect(lambda :print("mmmmmmmmmmmm"))

if __name__ == '__main__':
    pass

