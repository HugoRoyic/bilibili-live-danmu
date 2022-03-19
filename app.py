import threading
from core import DanMuJiCore
from HeadlessMainWindow import HeadlessMainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QStandardItemModel, QStandardItem
from queue import Queue
from config import CONFIG


class DanMuJiApp:
    def __init__(self):
        self.app = QApplication()
        self.window = HeadlessMainWindow()
        self.core = DanMuJiCore(CONFIG)
        self.window.uiInitialize()
        self.danmu_model = QStandardItemModel()
        self.danmu_pipe = Queue()
        self.uiInitialize()

    def exec(self):
        self.core.start(self.danmu_pipe)
        self.window.show()
        self._fresh = True
        self._thread = threading.Thread(target=self.fresh, daemon=True)
        self._thread.start()
        self.app.exec()

    def fresh(self):
        while self._fresh:
            danmu = self.danmu_pipe.get()
            item = QStandardItem(str(danmu))
            self.danmu_model.insertRow(0, item)
            cnt = self.danmu_model.rowCount()
            if cnt == 50:
                self.danmu_model.removeRow(49)
                

    def uiInitialize(self):
        self.window.ui.DanMuSendButton.clicked.connect(self.sendDanMu)
        self.window.ui.DanMuListView.setModel(self.danmu_model)

        def onClose(event):
            self.window.hide()
            self._fresh = False
            self._thread.join()
            self.core.stop()

        self.window.closeEvent = onClose

    def sendDanMu(self):
        message = self.window.ui.DanMuLineEdit.text()
        self.core.send_danmu(message)
        self.window.ui.DanMuLineEdit.setText("")