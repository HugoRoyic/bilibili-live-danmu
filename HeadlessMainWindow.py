from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt


class HeadlessMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        

if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication()
    ui = HeadlessMainWindow()
    ui.show()
    app.exec()
