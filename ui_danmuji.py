# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'danmujibXbNUb.ui'
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
"	background-color: #1b1b1b;\n"
"}\n"
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
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.TitleBarFrame = QFrame(self.MainWindowFrame)
        self.TitleBarFrame.setObjectName(u"TitleBarFrame")
        self.TitleBarFrame.setMinimumSize(QSize(0, 30))
        self.TitleBarFrame.setMaximumSize(QSize(16777215, 30))
        self.TitleBarFrame.setFrameShape(QFrame.NoFrame)
        self.TitleBarFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.TitleBarFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 6, 0, 0)
        self.TitleTextFrame = QFrame(self.TitleBarFrame)
        self.TitleTextFrame.setObjectName(u"TitleTextFrame")
        self.TitleTextFrame.setFrameShape(QFrame.StyledPanel)
        self.TitleTextFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.TitleTextFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(6, 0, 0, 0)
        self.TitleLabel = QLabel(self.TitleTextFrame)
        self.TitleLabel.setObjectName(u"TitleLabel")
        font1 = QFont()
        font1.setPointSize(10)
        self.TitleLabel.setFont(font1)
        self.TitleLabel.setStyleSheet(u"color: #a8b2b6;")

        self.horizontalLayout_3.addWidget(self.TitleLabel)


        self.horizontalLayout.addWidget(self.TitleTextFrame)

        self.TitleButtonFrame = QFrame(self.TitleBarFrame)
        self.TitleButtonFrame.setObjectName(u"TitleButtonFrame")
        self.TitleButtonFrame.setMaximumSize(QSize(90, 16777215))
        self.TitleButtonFrame.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 9px;\n"
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
        self.MinimizeButton.setMinimumSize(QSize(18, 18))
        self.MinimizeButton.setMaximumSize(QSize(18, 18))

        self.horizontalLayout_2.addWidget(self.MinimizeButton)

        self.MaximizeButton = QPushButton(self.TitleButtonFrame)
        self.MaximizeButton.setObjectName(u"MaximizeButton")
        self.MaximizeButton.setMinimumSize(QSize(18, 18))
        self.MaximizeButton.setMaximumSize(QSize(18, 18))

        self.horizontalLayout_2.addWidget(self.MaximizeButton)

        self.CloseButton = QPushButton(self.TitleButtonFrame)
        self.CloseButton.setObjectName(u"CloseButton")
        self.CloseButton.setMinimumSize(QSize(18, 18))
        self.CloseButton.setMaximumSize(QSize(18, 18))

        self.horizontalLayout_2.addWidget(self.CloseButton)

        self.MaximizeButton.raise_()
        self.MinimizeButton.raise_()
        self.CloseButton.raise_()

        self.horizontalLayout.addWidget(self.TitleButtonFrame)


        self.verticalLayout_2.addWidget(self.TitleBarFrame)

        self.ContentFrame = QFrame(self.MainWindowFrame)
        self.ContentFrame.setObjectName(u"ContentFrame")
        self.ContentFrame.setStyleSheet(u"border-radius: 0px;")
        self.ContentFrame.setFrameShape(QFrame.NoFrame)
        self.ContentFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.ContentFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, 0, 6, 0)
        self.TopFrame = QFrame(self.ContentFrame)
        self.TopFrame.setObjectName(u"TopFrame")
        self.TopFrame.setStyleSheet(u"")
        self.TopFrame.setFrameShape(QFrame.StyledPanel)
        self.TopFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.TopFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.DanMuFrame = QFrame(self.TopFrame)
        self.DanMuFrame.setObjectName(u"DanMuFrame")
        font2 = QFont()
        font2.setPointSize(9)
        self.DanMuFrame.setFont(font2)
        self.DanMuFrame.setStyleSheet(u"")
        self.DanMuFrame.setFrameShape(QFrame.StyledPanel)
        self.DanMuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.DanMuFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.DanMuListView = QListView(self.DanMuFrame)
        self.DanMuListView.setObjectName(u"DanMuListView")
        font3 = QFont()
        font3.setPointSize(11)
        self.DanMuListView.setFont(font3)
        self.DanMuListView.setLayoutDirection(Qt.LeftToRight)
        self.DanMuListView.setStyleSheet(u"QListView::item::hover {\n"
"	background-color: #262626;\n"
"}")
        self.DanMuListView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.DanMuListView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.DanMuListView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.DanMuListView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.DanMuListView.setDragEnabled(False)
        self.DanMuListView.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.DanMuListView.setDefaultDropAction(Qt.IgnoreAction)
        self.DanMuListView.setAlternatingRowColors(False)
        self.DanMuListView.setSelectionMode(QAbstractItemView.NoSelection)
        self.DanMuListView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.DanMuListView.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.DanMuListView.setMovement(QListView.Static)
        self.DanMuListView.setFlow(QListView.TopToBottom)
        self.DanMuListView.setProperty("isWrapping", False)
        self.DanMuListView.setLayoutMode(QListView.SinglePass)
        self.DanMuListView.setViewMode(QListView.ListMode)
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
        self.AudienceFrame.setStyleSheet(u"")
        self.AudienceFrame.setFrameShape(QFrame.StyledPanel)
        self.AudienceFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.AudienceFrame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.WatchedFrame = QFrame(self.AudienceFrame)
        self.WatchedFrame.setObjectName(u"WatchedFrame")
        self.WatchedFrame.setMinimumSize(QSize(0, 21))
        self.WatchedFrame.setMaximumSize(QSize(16777215, 21))
        self.WatchedFrame.setStyleSheet(u"QLabel{\n"
"	color: #0ebeff;\n"
"}")
        self.WatchedFrame.setFrameShape(QFrame.StyledPanel)
        self.WatchedFrame.setFrameShadow(QFrame.Raised)
        self.WatchedFrame.setLineWidth(0)
        self.horizontalLayout_7 = QHBoxLayout(self.WatchedFrame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(9, 3, 9, 3)
        self.WatchedNumLabel = QLabel(self.WatchedFrame)
        self.WatchedNumLabel.setObjectName(u"WatchedNumLabel")
        self.WatchedNumLabel.setLineWidth(0)
        self.WatchedNumLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.WatchedNumLabel)

        self.WatchedTextLabel = QLabel(self.WatchedFrame)
        self.WatchedTextLabel.setObjectName(u"WatchedTextLabel")
        self.WatchedTextLabel.setLineWidth(0)
        self.WatchedTextLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.WatchedTextLabel)


        self.verticalLayout_5.addWidget(self.WatchedFrame)

        self.PopularityFrame = QFrame(self.AudienceFrame)
        self.PopularityFrame.setObjectName(u"PopularityFrame")
        self.PopularityFrame.setMinimumSize(QSize(0, 21))
        self.PopularityFrame.setMaximumSize(QSize(16777215, 21))
        self.PopularityFrame.setFrameShape(QFrame.StyledPanel)
        self.PopularityFrame.setFrameShadow(QFrame.Raised)
        self.PopularityFrame.setLineWidth(0)
        self.horizontalLayout_8 = QHBoxLayout(self.PopularityFrame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 3, -1, 3)
        self.PopularityLabel = QLabel(self.PopularityFrame)
        self.PopularityLabel.setObjectName(u"PopularityLabel")
        self.PopularityLabel.setStyleSheet(u"color: #2fb45a;")
        self.PopularityLabel.setLineWidth(0)
        self.PopularityLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.PopularityLabel)


        self.verticalLayout_5.addWidget(self.PopularityFrame)

        self.AudienceListView = QListView(self.AudienceFrame)
        self.AudienceListView.setObjectName(u"AudienceListView")
        self.AudienceListView.setMovement(QListView.Free)

        self.verticalLayout_5.addWidget(self.AudienceListView)


        self.horizontalLayout_4.addWidget(self.AudienceFrame)

        self.QueueFrame = QFrame(self.TopFrame)
        self.QueueFrame.setObjectName(u"QueueFrame")
        self.QueueFrame.setStyleSheet(u"")
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
        self.BottomFrame.setStyleSheet(u"")
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

        self.verticalLayout_3.setStretch(0, 3)
        self.verticalLayout_3.setStretch(1, 2)

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
        self.WatchedNumLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.WatchedTextLabel.setText(QCoreApplication.translate("MainWindow", u"0\u4eba\u770b\u8fc7", None))
        self.PopularityLabel.setText(QCoreApplication.translate("MainWindow", u"0\u4eba\u6c14", None))
        self.StatusLabel.setText("")
    # retranslateUi

