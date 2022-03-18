from PySide6.QtWidgets import QApplication

from HeadlessMainWindow import HeadlessMainWindow

if __name__ == "__main__":
    app = QApplication()
    window = HeadlessMainWindow()
    window.uiInitialize()
    window.show()
    app.exec()