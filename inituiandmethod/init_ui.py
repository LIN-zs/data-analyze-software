from ui import cars,ipls,plsr,rf,svr,vip,ui_feature_extraction,ui_first_method_select
from PySide6.QtWidgets import  QWidget

class Ui_Cars(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=cars.Cars()
        self.ui.setupUi(self)
class Ui_Vip(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=vip.Vip()
        self.ui.setupUi(self)
class Ui_ipls(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=ipls.ipls()
        self.ui.setupUi(self)
class Ui_Plsr(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=plsr.Plsr()
        self.ui.setupUi(self)
class Ui_Rf(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=rf.Rf()
        self.ui.setupUi(self)
class Ui_Svr(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=svr.Svr()
        self.ui.setupUi(self)


class Ui_Feature_Extraction(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=ui_feature_extraction.Ui_Feature_Extraction()
        self.ui.setupUi(self)
        self.ui.comboBox_2.currentIndexChanged.connect(self.handleSelectionChange)
    def handleSelectionChange(self):
        cbox=self.ui.comboBox_2
        method = cbox.currentText()
        layout = self.ui.verticalLayout_2
        s=layout.layout()
        for i in range(s.count()):
            s.itemAt(i).widget().deleteLater()
        if method =='VIP':
            layout.addWidget(Ui_Vip())
        elif method =='CARS':
            layout.addWidget(Ui_Cars())
            pass
        elif method=='iPLS':
            layout.addWidget(Ui_ipls())
            pass
        else :
            pass
class Ui_First_Method_Select(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=ui_first_method_select.Ui_First_Method_Select()
        self.ui.setupUi(self)

        self.ui.comboBox.currentIndexChanged.connect(self.handleSelectionChange)
    def handleSelectionChange(self):
        cbox=self.ui.comboBox
        method = cbox.currentText()
        layout = self.ui.verticalLayout_2
        s=layout.layout()
        for i in range(s.count()):
            s.itemAt(i).widget().deleteLater()
        if method =='RF':
            layout.addWidget(Ui_Rf())
        elif method =='PSO-SVR':
            layout.addWidget(Ui_Svr())
            pass
        elif method=='PLSR':
            layout.addWidget(Ui_Plsr())
            pass
        else :
            pass