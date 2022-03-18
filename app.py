from socketserver import ThreadingMixIn
from core import DanMuJiCore
from HeadlessMainWindow import HeadlessMainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QStandardItemModel, QStandardItem
import threading
import queue
from config import CONFIG


class DanMuJiApp:
    def __init__(self):
        self.app = QApplication()
        self.window = HeadlessMainWindow()
        self.core = DanMuJiCore(CONFIG)
        self.window.uiInitialize()
        self.danmu_model = QStandardItemModel()
        self.bind()

    def exec(self):
        self.core.start()
        self.window.show()
        self._fresh = True
        self._thread = threading.Thread(target=self.fresh, daemon=True)
        self._thread.start()
        self.app.exec()

    def fresh(self):
        while self._fresh:
            if not self.core.pipe.empty():
                danmu = self.core.pipe.get()
                item = QStandardItem(str(danmu))
                self.danmu_model.appendRow(item)

    def bind(self):
        self.window.ui.DanMuListView.setModel(self.danmu_model)
