# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'unit_data.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_Unit_Data(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.returnbutton=QPushButton(self.centralwidget)
        self.returnbutton.setObjectName(u"return")

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")




        self.verticalLayout.addWidget(self.returnbutton)
        self.horizontalLayout.addWidget(self.label)

        self.labelall = QLabel(self.centralwidget)
        self.btnallcsv=QPushButton(self.centralwidget)


        self.horizontalLayout.addWidget(self.labelall)
        self.horizontalLayout.addWidget(self.btnallcsv)

        self.verticalLayout.addLayout(self.horizontalLayout)




        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.csvname=QLabel(self.centralwidget)
        self.csvname.setObjectName(u"csvname")
        self.horizontalLayout_2.addWidget(self.csvname)


        self.btn = QPushButton(self.centralwidget)
        self.btn.setObjectName(u"getcsvnae")
        self.horizontalLayout_2.addWidget(self.btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)


    # setupUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.returnbutton.setText(QCoreApplication.translate("MainWindow", u"return", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u6587\u4ef6\u5939", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5b58\u653e\u6570\u636e\u6587\u4ef6\u5939", None))
        self.btn.setText(QCoreApplication.translate("MainWindow", u"选择储存文件路径", None))
        self.btnallcsv.setText(QCoreApplication.translate("MainWindow", u"选择文件路径", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u786e\u5b9a", None))
    # retranslateUi

