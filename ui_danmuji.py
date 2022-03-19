# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'danmujizKWGVU.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListView, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(917, 709)
        font = QFont()
        font.setFamilies([u"Sarasa Fixed SC"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QFrame {\n"
"	border: 0px;\n"
"	background-color: #191919;\n"
"}\n"
"\n"
"\n"
"")
        self.MainWindowWidget = QWidget(MainWindow)
        self.MainWindowWidget.setObjectName(u"MainWindowWidget")
        self.MainWindowWidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.MainWindowWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.MainWindowFrame = QFrame(self.MainWindowWidget)
        self.MainWindowFrame.setObjectName(u"MainWindowFrame")
        self.MainWindowFrame.setAutoFillBackground(False)
        self.MainWindowFrame.setStyleSheet(u"border-radius: 10px;\n"
"")
        self.MainWindowFrame.setFrameShape(QFrame.NoFrame)
        self.MainWindowFrame.setFrameShadow(QFrame.Raised)
        self.MainWindowFrame.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.MainWindowFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 0)
        self.TitleBarFrame = QFrame(self.MainWindowFrame)
        self.TitleBarFrame.setObjectName(u"TitleBarFrame")
        self.TitleBarFrame.setMinimumSize(QSize(0, 25))
        self.TitleBarFrame.setMaximumSize(QSize(16777215, 25))
        self.TitleBarFrame.setFrameShape(QFrame.NoFrame)
        self.TitleBarFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.TitleBarFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.TitleTextFrame = QFrame(self.TitleBarFrame)
        self.TitleTextFrame.setObjectName(u"TitleTextFrame")
        self.TitleTextFrame.setFrameShape(QFrame.StyledPanel)
        self.TitleTextFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.TitleTextFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 0, 0, 0)
        self.TitleLabel = QLabel(self.TitleTextFrame)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setStyleSheet(u"color: #a8b2b6;")

        self.horizontalLayout_3.addWidget(self.TitleLabel)


        self.horizontalLayout.addWidget(self.TitleTextFrame)

        self.TitleButtonFrame = QFrame(self.TitleBarFrame)
        self.TitleButtonFrame.setObjectName(u"TitleButtonFrame")
        self.TitleButtonFrame.setMaximumSize(QSize(100, 16777215))
        self.TitleButtonFrame.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	background-color: #333333;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #666666;\n"
"}")
        self.TitleButtonFrame.setFrameShape(QFrame.NoFrame)
        self.TitleButtonFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.TitleButtonFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.MinimizeButton = QPushButton(self.TitleButtonFrame)
        self.MinimizeButton.setObjectName(u"MinimizeButton")
        self.MinimizeButton.setMinimumSize(QSize(16, 16))
        self.MinimizeButton.setMaximumSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.MinimizeButton)

        self.MaximizeButton = QPushButton(self.TitleButtonFrame)
        self.MaximizeButton.setObjectName(u"MaximizeButton")
        self.MaximizeButton.setMinimumSize(QSize(16, 16))
        self.MaximizeButton.setMaximumSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.MaximizeButton)

        self.CloseButton = QPushButton(self.TitleButtonFrame)
        self.CloseButton.setObjectName(u"CloseButton")
        self.CloseButton.setMinimumSize(QSize(16, 16))
        self.CloseButton.setMaximumSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.CloseButton)

        self.MaximizeButton.raise_()
        self.MinimizeButton.raise_()
        self.CloseButton.raise_()

        self.horizontalLayout.addWidget(self.TitleButtonFrame)


        self.verticalLayout_2.addWidget(self.TitleBarFrame)

        self.ContentFrame = QFrame(self.MainWindowFrame)
        self.ContentFrame.setObjectName(u"ContentFrame")
        self.ContentFrame.setStyleSheet(u"border-radius: 0px;")
        self.ContentFrame.setFrameShape(QFrame.StyledPanel)
        self.ContentFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.ContentFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.TopFrame = QFrame(self.ContentFrame)
        self.TopFrame.setObjectName(u"TopFrame")
        self.TopFrame.setFrameShape(QFrame.StyledPanel)
        self.TopFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.TopFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.DanMuFrame = QFrame(self.TopFrame)
        self.DanMuFrame.setObjectName(u"DanMuFrame")
        self.DanMuFrame.setFrameShape(QFrame.StyledPanel)
        self.DanMuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.DanMuFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.DanMuListView = QListView(self.DanMuFrame)
        self.DanMuListView.setObjectName(u"DanMuListView")
        self.DanMuListView.setLayoutDirection(Qt.LeftToRight)
        self.DanMuListView.setStyleSheet(u"color: white;")
        self.DanMuListView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.DanMuListView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.DanMuListView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.DanMuListView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.DanMuListView.setDragEnabled(True)
        self.DanMuListView.setAlternatingRowColors(False)
        self.DanMuListView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.DanMuListView.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.DanMuListView.setMovement(QListView.Free)
        self.DanMuListView.setProperty("isWrapping", False)
        self.DanMuListView.setLayoutMode(QListView.SinglePass)
        self.DanMuListView.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.DanMuListView)

        self.DanMuEditFrame = QFrame(self.DanMuFrame)
        self.DanMuEditFrame.setObjectName(u"DanMuEditFrame")
        self.DanMuEditFrame.setMinimumSize(QSize(0, 20))
        self.DanMuEditFrame.setMaximumSize(QSize(16777215, 20))
        self.DanMuEditFrame.setFrameShape(QFrame.StyledPanel)
        self.DanMuEditFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.DanMuEditFrame)
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.DanMuLineEdit = QLineEdit(self.DanMuEditFrame)
        self.DanMuLineEdit.setObjectName(u"DanMuLineEdit")
        self.DanMuLineEdit.setMinimumSize(QSize(0, 20))
        self.DanMuLineEdit.setStyleSheet(u"background-color: #333333;\n"
"color: #a2fafa;")

        self.horizontalLayout_6.addWidget(self.DanMuLineEdit)

        self.DanMuSendButton = QPushButton(self.DanMuEditFrame)
        self.DanMuSendButton.setObjectName(u"DanMuSendButton")
        self.DanMuSendButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #2fb6c3;\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	padding: 12px;\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	color: #333333;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #666666;\n"
"}")

        self.horizontalLayout_6.addWidget(self.DanMuSendButton)


        self.verticalLayout_4.addWidget(self.DanMuEditFrame)


        self.horizontalLayout_4.addWidget(self.DanMuFrame)

        self.AudienceFrame = QFrame(self.TopFrame)
        self.AudienceFrame.setObjectName(u"AudienceFrame")
        self.AudienceFrame.setFrameShape(QFrame.StyledPanel)
        self.AudienceFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.AudienceFrame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.AudienceListView = QListView(self.AudienceFrame)
        self.AudienceListView.setObjectName(u"AudienceListView")
        self.AudienceListView.setMovement(QListView.Free)

        self.verticalLayout_5.addWidget(self.AudienceListView)


        self.horizontalLayout_4.addWidget(self.AudienceFrame)

        self.QueueFrame = QFrame(self.TopFrame)
        self.QueueFrame.setObjectName(u"QueueFrame")
        self.QueueFrame.setFrameShape(QFrame.StyledPanel)
        self.QueueFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.QueueFrame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.QueueListView = QListView(self.QueueFrame)
        self.QueueListView.setObjectName(u"QueueListView")

        self.verticalLayout_6.addWidget(self.QueueListView)


        self.horizontalLayout_4.addWidget(self.QueueFrame)

        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 2)
        self.horizontalLayout_4.setStretch(2, 2)
        self.AudienceFrame.raise_()
        self.DanMuFrame.raise_()
        self.QueueFrame.raise_()

        self.verticalLayout_3.addWidget(self.TopFrame)

        self.BottomFrame = QFrame(self.ContentFrame)
        self.BottomFrame.setObjectName(u"BottomFrame")
        self.BottomFrame.setFrameShape(QFrame.StyledPanel)
        self.BottomFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.BottomFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.MedalFrame = QFrame(self.BottomFrame)
        self.MedalFrame.setObjectName(u"MedalFrame")
        self.MedalFrame.setFrameShape(QFrame.StyledPanel)
        self.MedalFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.MedalFrame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.MedalBrowser = QTextBrowser(self.MedalFrame)
        self.MedalBrowser.setObjectName(u"MedalBrowser")

        self.verticalLayout_8.addWidget(self.MedalBrowser)


        self.horizontalLayout_5.addWidget(self.MedalFrame)

        self.HistoryFrame = QFrame(self.BottomFrame)
        self.HistoryFrame.setObjectName(u"HistoryFrame")
        self.HistoryFrame.setFrameShape(QFrame.StyledPanel)
        self.HistoryFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.HistoryFrame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.HistoryTableWidget = QTableWidget(self.HistoryFrame)
        self.HistoryTableWidget.setObjectName(u"HistoryTableWidget")
        self.HistoryTableWidget.setSortingEnabled(True)

        self.verticalLayout_7.addWidget(self.HistoryTableWidget)


        self.horizontalLayout_5.addWidget(self.HistoryFrame)


        self.verticalLayout_3.addWidget(self.BottomFrame)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)

        self.verticalLayout_2.addWidget(self.ContentFrame)

        self.horizontalFrame = QFrame(self.MainWindowFrame)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setMinimumSize(QSize(0, 25))
        self.horizontalFrame.setMaximumSize(QSize(16777215, 25))
        self.BottomLineFrame = QHBoxLayout(self.horizontalFrame)
        self.BottomLineFrame.setSpacing(0)
        self.BottomLineFrame.setObjectName(u"BottomLineFrame")
        self.BottomLineFrame.setContentsMargins(0, 0, 0, 0)
        self.StatusLabel = QLabel(self.horizontalFrame)
        self.StatusLabel.setObjectName(u"StatusLabel")
        self.StatusLabel.setStyleSheet(u"color: #a8b2b6;")

        self.BottomLineFrame.addWidget(self.StatusLabel)

        self.GripFrame = QFrame(self.horizontalFrame)
        self.GripFrame.setObjectName(u"GripFrame")
        self.GripFrame.setMinimumSize(QSize(16, 16))
        self.GripFrame.setMaximumSize(QSize(16, 16))
        self.GripFrame.setFrameShape(QFrame.StyledPanel)
        self.GripFrame.setFrameShadow(QFrame.Raised)

        self.BottomLineFrame.addWidget(self.GripFrame)


        self.verticalLayout_2.addWidget(self.horizontalFrame)


        self.verticalLayout.addWidget(self.MainWindowFrame)

        MainWindow.setCentralWidget(self.MainWindowWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.TitleLabel.setText(QCoreApplication.translate("MainWindow", u"\u5f39\u5e55\u59ec", None))
        self.MinimizeButton.setText("")
        self.MaximizeButton.setText("")
        self.CloseButton.setText("")
        self.DanMuSendButton.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.StatusLabel.setText("")
    # retranslateUi

