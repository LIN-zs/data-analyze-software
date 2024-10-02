# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab.ui'
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
                               QLineEdit, QSizePolicy, QSpacerItem, QVBoxLayout,
                               QWidget, QPushButton, QFileDialog)

class Ui_Feature_Extraction(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(710, 704)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_29 = QLabel(Form)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_32.addWidget(self.label_29)

        self.lineEdit_26 = QLabel(Form)
        self.horizontalLayout_32.addWidget(self.lineEdit_26)



        self.verticalLayout.addLayout(self.horizontalLayout_32)

        self.btn= QPushButton(Form)
        self.btn.setText("选择文件")
        self.horizontalLayout_32.addWidget(self.btn)
        self.btn.clicked.connect(self.getcsv)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setWordWrap(False)

        self.horizontalLayout.addWidget(self.label_2)

        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.verticalLayout_4.addWidget(self.comboBox_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi
    def getcsv(self):
        fileName, fileType = QFileDialog().getOpenFileName(None,'选择储存csv文件路径',"", "All Files (*)")
        self.lineEdit_26.setText(fileName)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u8def\u5f84", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u9884\u5904\u7406\u65b9\u6cd5", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"No", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"MSC", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"Normal", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"1ST", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Form", u"SNV", None))

        self.label.setText(QCoreApplication.translate("Form", u"\u7279\u5f81\u63d0\u53d6\u7b97\u6cd5", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"No", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Form", u"CARS", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Form", u"VIP", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Form", u"iPLS", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("Form", u"PCA", None))

    # retranslateUi

