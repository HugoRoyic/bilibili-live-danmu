from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6 import QtCore

QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)

class DanMuJi():
    def __init__(self):
        self.app = QApplication()
        qfile = QFile("danmuji.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()

        self.ui = QUiLoader().load(qfile)

    def exec(self):
        self.ui.show()
        self.app.exec()


if __name__ == "__main__":
    
    d = DanMuJi()
    d.exec()
