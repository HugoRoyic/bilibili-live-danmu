from PySide6.QtWidgets import QMainWindow, QSizeGrip
from PySide6 import QtCore

from ui_danmuji import Ui_MainWindow

# QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)

NORMAL = 0
MAXIMIZED = 1

class HeadlessMainWindow(QMainWindow):
    SHOW_STATE = NORMAL
    def __init__(self):
        super().__init__()       
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
        def moveWindow(event):
            if self.SHOW_STATE == MAXIMIZED:
                self.maximizeRestore()
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.TitleBarFrame.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def uiInitialize(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.TitleBarFrame.mouseDoubleClickEvent = self.maximizeRestore
        self.ui.MaximizeButton.clicked.connect(self.maximizeRestore)
        self.ui.MinimizeButton.clicked.connect(self.showMinimized)
        self.ui.CloseButton.clicked.connect(self.close)
        self.sizegrip = QSizeGrip(self.ui.GripFrame)
        # self.sizegrip.setStyleSheet("bottom: 0px;right:0px;")

    def maximizeRestore(self, event=None):
        if not self.SHOW_STATE:
            self.showMaximized()
            self.SHOW_STATE = MAXIMIZED
            self.ui.MainWindowFrame.setStyleSheet("border-radius: 0px;")
        else:
            self.showNormal()
            self.SHOW_STATE = NORMAL
            self.ui.MainWindowFrame.setStyleSheet("border-radius: 10px;")


if __name__ == "__main__":    
    pass
