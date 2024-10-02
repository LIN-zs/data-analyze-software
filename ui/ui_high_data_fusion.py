# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_high_data_fusion.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_High_Data_Fusion(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_3.addWidget(self.lineEdit_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_3.addWidget(self.comboBox)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_3.addWidget(self.lineEdit_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_4.addWidget(self.comboBox_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.comboBox_3 = QComboBox(self.centralwidget)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_6.addWidget(self.comboBox_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.horizontalLayout_6.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_7.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_8.addWidget(self.label_6)

        self.comboBox_4 = QComboBox(self.centralwidget)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.horizontalLayout_8.addWidget(self.comboBox_4)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.horizontalLayout_8.addLayout(self.verticalLayout_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_2.addWidget(self.plainTextEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_plt = QWidget(self.centralwidget)
        self.widget_plt.setObjectName(u"widget_plt")

        self.verticalLayout.addWidget(self.widget_plt)

        self.widget_results = QWidget(self.centralwidget)
        self.widget_results.setObjectName(u"widget_results")

        self.verticalLayout.addWidget(self.widget_results)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u8def\u5f84", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e00\u5c42Kfold", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e8c\u5c42\u6570\u636e\u5212\u5206", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u968f\u673a\u5212\u5206", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"KS\u5212\u5206", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u4ed6\u9a8c\u8bc1", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u4ea4\u53c9\u9a8c\u8bc1", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u9884\u5904\u7406\u65b9\u6cd5", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"SNV", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"MSC", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"1ST", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Normal", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u7279\u5f81\u63d0\u53d6\u7b97\u6cd5", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"PCA", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"VIP", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"CARS", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"iPLS", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u589e\u52a0\u7b2c\u4e00\u5c42\u7b97\u6cd5", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e8c\u5c42\u7b97\u6cd5", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"RF", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"PLSR", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"SVR", None))

        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5206\u6790", None))
    # retranslateUi

