import threading
from core import DanMuJiCore
from HeadlessMainWindow import HeadlessMainWindow
from PySide6.QtWidgets import QApplication, QStyledItemDelegate, QStyle
from PySide6.QtGui import QStandardItemModel, QStandardItem, QTextDocument
from PySide6.QtCore import QRect, QSize
from queue import Queue
from config import CONFIG

from PySide6.QtCore import Signal, QObject


class DanMuSignal(QObject):
    DanMuUpdate = Signal(str)


class DanMuModel(QStyledItemDelegate):
    def __init__(self, *args):
        super().__init__(*args)
        self.doc = QTextDocument()

    def paint(self, painter, option, index):
        painter.save()
        self.initStyleOption(option, index)
        self.doc.setHtml(option.text)
        option.text = ""
        option.widget.style().drawControl(QStyle.CE_ItemViewItem, option, painter)
        painter.translate(option.rect.left(), option.rect.top())
        self.doc.drawContents(painter)
        painter.restore()

    def sizeHint(self, option, index):
        return QSize(self.doc.idealWidth(), self.doc.size().height())


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
        self._thread = threading.Thread(target=self.getDanMu, daemon=True)
        self._thread.start()
        self.app.exec()

    def getDanMu(self):
        while self._fresh:
            danmu = self.danmu_pipe.get()
            if danmu["code"] <= 2:
                data = danmu["data"]
                if danmu["code"] == 2:
                    html = ""
                    if data.get("medal"):
                        html += f"<font style='background-color:#008080;color:#f5f5dc;'>{data['medal']}</font> "
                    html += f"<font style='color:#0ebeff;'>{data['nickname']}：</font>"
                    html += f"<font style='color:#2fb6c3;'>{data['text']}</font>"
                else:
                    html = f"<font style='color:#97d948;'>{data['info']}</font>"
                self.danmu_signal.DanMuUpdate.emit(html)

    def uiInitialize(self):
        self.danmu_signal = DanMuSignal()
        self.danmu_signal.DanMuUpdate.connect(self.showDanMu)
        self.window.ui.DanMuSendButton.clicked.connect(self.sendDanMu)
        self.window.ui.DanMuListView.setItemDelegate(DanMuModel())
        self.window.ui.DanMuListView.setModel(self.danmu_model)

        def onClose(event):
            self.window.hide()
            self._fresh = False
            self._thread.join()
            self.core.stop()

        self.window.closeEvent = onClose

    def showDanMu(self, danmu):
        item = QStandardItem(danmu)
        self.danmu_model.insertRow(0, item)
        cnt = self.danmu_model.rowCount()
        if cnt == 50:
            self.danmu_model.removeRow(49)

    def sendDanMu(self):
        message = self.window.ui.DanMuLineEdit.text()
        self.core.send_danmu(message)
        self.window.ui.DanMuLineEdit.setText("")
