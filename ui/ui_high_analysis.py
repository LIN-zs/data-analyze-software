# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'high_fusion.ui
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_High_Analysis(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(921, 1159)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_18 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_12.addWidget(self.label_12)

        self.lineEdit_csvname = QLineEdit(self.centralwidget)
        self.lineEdit_csvname.setObjectName(u"lineEdit_csvname")

        self.horizontalLayout_12.addWidget(self.lineEdit_csvname)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_13.addWidget(self.label_19)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_13.addWidget(self.lineEdit)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_13.addWidget(self.label_13)

        self.comboBox_traintestspilt = QComboBox(self.centralwidget)
        self.comboBox_traintestspilt.addItem("")
        self.comboBox_traintestspilt.addItem("")
        self.comboBox_traintestspilt.addItem("")
        self.comboBox_traintestspilt.addItem("")
        self.comboBox_traintestspilt.setObjectName(u"comboBox_traintestspilt")

        self.horizontalLayout_13.addWidget(self.comboBox_traintestspilt)

        self.lineEdit_traintestspilt = QLineEdit(self.centralwidget)
        self.lineEdit_traintestspilt.setObjectName(u"lineEdit_traintestspilt")

        self.horizontalLayout_13.addWidget(self.lineEdit_traintestspilt)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)


        self.verticalLayout_12.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox_normal = QCheckBox(self.centralwidget)
        self.checkBox_normal.setObjectName(u"checkBox_normal")

        self.horizontalLayout.addWidget(self.checkBox_normal)

        self.checkBox_msc = QCheckBox(self.centralwidget)
        self.checkBox_msc.setObjectName(u"checkBox_msc")

        self.horizontalLayout.addWidget(self.checkBox_msc)

        self.checkBox_1st = QCheckBox(self.centralwidget)
        self.checkBox_1st.setObjectName(u"checkBox_1st")

        self.horizontalLayout.addWidget(self.checkBox_1st)

        self.checkBox_snv = QCheckBox(self.centralwidget)
        self.checkBox_snv.setObjectName(u"checkBox_snv")

        self.horizontalLayout.addWidget(self.checkBox_snv)


        self.verticalLayout_12.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_12.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.checkBox_cars = QCheckBox(self.centralwidget)
        self.checkBox_cars.setObjectName(u"checkBox_cars")

        self.verticalLayout_4.addWidget(self.checkBox_cars)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lineEdit_carsiteration = QLineEdit(self.centralwidget)
        self.lineEdit_carsiteration.setObjectName(u"lineEdit_carsiteration")

        self.horizontalLayout_5.addWidget(self.lineEdit_carsiteration)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_carsnv = QLineEdit(self.centralwidget)
        self.lineEdit_carsnv.setObjectName(u"lineEdit_carsnv")

        self.horizontalLayout_4.addWidget(self.lineEdit_carsnv)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_carscv = QLineEdit(self.centralwidget)
        self.lineEdit_carscv.setObjectName(u"lineEdit_carscv")

        self.horizontalLayout_3.addWidget(self.lineEdit_carscv)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.checkBox_ipls = QCheckBox(self.centralwidget)
        self.checkBox_ipls.setObjectName(u"checkBox_ipls")

        self.verticalLayout_6.addWidget(self.checkBox_ipls)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.lineEdit_iplssize = QLineEdit(self.centralwidget)
        self.lineEdit_iplssize.setObjectName(u"lineEdit_iplssize")

        self.horizontalLayout_9.addWidget(self.lineEdit_iplssize)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.lineEdit_iplsinternum = QLineEdit(self.centralwidget)
        self.lineEdit_iplsinternum.setObjectName(u"lineEdit_iplsinternum")

        self.horizontalLayout_10.addWidget(self.lineEdit_iplsinternum)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_11.addWidget(self.label_11)

        self.lineEdit_iplsnumber = QLineEdit(self.centralwidget)
        self.lineEdit_iplsnumber.setObjectName(u"lineEdit_iplsnumber")

        self.horizontalLayout_11.addWidget(self.lineEdit_iplsnumber)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.checkBox_vip = QCheckBox(self.centralwidget)
        self.checkBox_vip.setObjectName(u"checkBox_vip")

        self.verticalLayout_5.addWidget(self.checkBox_vip)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.lineEdit_vipnumber = QLineEdit(self.centralwidget)
        self.lineEdit_vipnumber.setObjectName(u"lineEdit_vipnumber")

        self.horizontalLayout_6.addWidget(self.lineEdit_vipnumber)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)


        self.verticalLayout_12.addLayout(self.horizontalLayout_2)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_12.addWidget(self.label_7)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_29 = QLabel(self.centralwidget)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_7.addWidget(self.label_29)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.lineEdit_rfnumber = QLineEdit(self.centralwidget)
        self.lineEdit_rfnumber.setObjectName(u"lineEdit_rfnumber")

        self.horizontalLayout_8.addWidget(self.lineEdit_rfnumber)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_7.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_30 = QLabel(self.centralwidget)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_8.addWidget(self.label_30)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_14.addWidget(self.label_14)

        self.lineEdit_svrg = QLineEdit(self.centralwidget)
        self.lineEdit_svrg.setObjectName(u"lineEdit_svrg")

        self.horizontalLayout_14.addWidget(self.lineEdit_svrg)


        self.verticalLayout_8.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_15.addWidget(self.label_15)

        self.lineEdit_svrc = QLineEdit(self.centralwidget)
        self.lineEdit_svrc.setObjectName(u"lineEdit_svrc")

        self.horizontalLayout_15.addWidget(self.lineEdit_svrc)


        self.verticalLayout_8.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_16.addWidget(self.label_16)

        self.lineEdit_svrk = QLineEdit(self.centralwidget)
        self.lineEdit_svrk.setObjectName(u"lineEdit_svrk")

        self.horizontalLayout_16.addWidget(self.lineEdit_svrk)


        self.verticalLayout_8.addLayout(self.horizontalLayout_16)


        self.horizontalLayout_7.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_31 = QLabel(self.centralwidget)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_9.addWidget(self.label_31)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_17.addWidget(self.label_17)

        self.lineEdit_plsrnc = QLineEdit(self.centralwidget)
        self.lineEdit_plsrnc.setObjectName(u"lineEdit_plsrnc")

        self.horizontalLayout_17.addWidget(self.lineEdit_plsrnc)


        self.verticalLayout_9.addLayout(self.horizontalLayout_17)


        self.horizontalLayout_7.addLayout(self.verticalLayout_9)


        self.verticalLayout_12.addLayout(self.horizontalLayout_7)

        self.label_28 = QLabel(self.centralwidget)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_12.addWidget(self.label_28)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.checkBox_rf = QCheckBox(self.centralwidget)
        self.checkBox_rf.setObjectName(u"checkBox_rf")

        self.verticalLayout_14.addWidget(self.checkBox_rf)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_26.addWidget(self.label_18)

        self.lineEdit_rfnumber_3 = QLineEdit(self.centralwidget)
        self.lineEdit_rfnumber_3.setObjectName(u"lineEdit_rfnumber_3")

        self.horizontalLayout_26.addWidget(self.lineEdit_rfnumber_3)


        self.verticalLayout_14.addLayout(self.horizontalLayout_26)


        self.horizontalLayout_25.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.checkBox_svr = QCheckBox(self.centralwidget)
        self.checkBox_svr.setObjectName(u"checkBox_svr")

        self.verticalLayout_15.addWidget(self.checkBox_svr)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_24 = QLabel(self.centralwidget)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_27.addWidget(self.label_24)

        self.lineEdit_svrg_3 = QLineEdit(self.centralwidget)
        self.lineEdit_svrg_3.setObjectName(u"lineEdit_svrg_3")

        self.horizontalLayout_27.addWidget(self.lineEdit_svrg_3)


        self.verticalLayout_15.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_28.addWidget(self.label_25)

        self.lineEdit_svrc_3 = QLineEdit(self.centralwidget)
        self.lineEdit_svrc_3.setObjectName(u"lineEdit_svrc_3")

        self.horizontalLayout_28.addWidget(self.lineEdit_svrc_3)


        self.verticalLayout_15.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_26 = QLabel(self.centralwidget)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_29.addWidget(self.label_26)

        self.lineEdit_svrk_3 = QLineEdit(self.centralwidget)
        self.lineEdit_svrk_3.setObjectName(u"lineEdit_svrk_3")

        self.horizontalLayout_29.addWidget(self.lineEdit_svrk_3)


        self.verticalLayout_15.addLayout(self.horizontalLayout_29)


        self.horizontalLayout_25.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.checkBox_plsr = QCheckBox(self.centralwidget)
        self.checkBox_plsr.setObjectName(u"checkBox_plsr")

        self.verticalLayout_16.addWidget(self.checkBox_plsr)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_27 = QLabel(self.centralwidget)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_30.addWidget(self.label_27)

        self.lineEdit_plsrnc_3 = QLineEdit(self.centralwidget)
        self.lineEdit_plsrnc_3.setObjectName(u"lineEdit_plsrnc_3")

        self.horizontalLayout_30.addWidget(self.lineEdit_plsrnc_3)


        self.verticalLayout_16.addLayout(self.horizontalLayout_30)


        self.horizontalLayout_25.addLayout(self.verticalLayout_16)


        self.verticalLayout_12.addLayout(self.horizontalLayout_25)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_12.addWidget(self.pushButton)

        self.plainTextEdit_results = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_results.setObjectName(u"plainTextEdit_results")

        self.verticalLayout_12.addWidget(self.plainTextEdit_results)


        self.horizontalLayout_18.addLayout(self.verticalLayout_12)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.widget_plt = QWidget(self.centralwidget)
        self.widget_plt.setObjectName(u"widget_plt")

        self.verticalLayout_25.addWidget(self.widget_plt)

        self.widget_results = QWidget(self.centralwidget)
        self.widget_results.setObjectName(u"widget_results")

        self.verticalLayout_25.addWidget(self.widget_results)


        self.horizontalLayout_18.addLayout(self.verticalLayout_25)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 921, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u8def\u5f84", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e00\u5c42Kfold", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e8c\u5c42\u6570\u636e\u5212\u5206", None))
        self.comboBox_traintestspilt.setItemText(0, QCoreApplication.translate("MainWindow", u"\u968f\u673a\u5212\u5206", None))
        self.comboBox_traintestspilt.setItemText(1, QCoreApplication.translate("MainWindow", u"KS\u5212\u5206", None))
        self.comboBox_traintestspilt.setItemText(2, QCoreApplication.translate("MainWindow", u"\u4ea4\u53c9\u9a8c\u8bc1", None))
        self.comboBox_traintestspilt.setItemText(3, QCoreApplication.translate("MainWindow", u"\u4ed6\u9a8c\u8bc1", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u9884\u5904\u7406\u65b9\u6cd5", None))
        self.checkBox_normal.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.checkBox_msc.setText(QCoreApplication.translate("MainWindow", u"MSC", None))
        self.checkBox_1st.setText(QCoreApplication.translate("MainWindow", u"1ST", None))
        self.checkBox_snv.setText(QCoreApplication.translate("MainWindow", u"SNV", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u7279\u5f81\u63d0\u53d6\u65b9\u6cd5", None))
        self.checkBox_cars.setText(QCoreApplication.translate("MainWindow", u"CARS", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u8fed\u4ee3\u6b21\u6570", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u6210\u5206\u6570", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u4ea4\u53c9\u9a8c\u8bc1\u6b21\u6570", None))
        self.checkBox_ipls.setText(QCoreApplication.translate("MainWindow", u"IPLS", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u5212\u5206\u6bd4\u4f8b", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u533a\u95f4\u6570", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u53d6\u533a\u95f4\u6570\u91cf", None))
        self.checkBox_vip.setText(QCoreApplication.translate("MainWindow", u"VIP", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u53d6\u7279\u5f81\u6570\u91cf", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e00\u5c42\u5b9a\u91cf\u7b97\u6cd5", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"RF", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u6811\u7684\u6570\u91cf", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"SVR", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"g", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"c", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u6838\u51fd\u6570", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"PLSR", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u6210\u5206\u6570\u91cf", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e8c\u5c42\u5b9a\u91cf\u7b97\u6cd5", None))
        self.checkBox_rf.setText(QCoreApplication.translate("MainWindow", u"RF", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u6811\u7684\u6570\u91cf", None))
        self.checkBox_svr.setText(QCoreApplication.translate("MainWindow", u"SVR", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"g", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"c", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u6838\u51fd\u6570", None))
        self.checkBox_plsr.setText(QCoreApplication.translate("MainWindow", u"PLSR", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u6210\u5206\u6570\u91cf", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4", None))
    # retranslateUi

