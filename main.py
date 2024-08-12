#encoding=utf-8
import sys
import matplotlib
matplotlib.use('Qt5Agg')
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from ui.ui_main import Ui_Main
from ui.ui_low_or_mid_analysis import Ui_Low_Or_Mid_Analysis
from inituiandmethod.init_ui import *
import sklearn.svm
from inituiandmethod.init_method import *
from basemethod.ModelEvaluation import *
from ui.ui_high_analysis import Ui_High_Analysis
from ui.ui_high_data_fusion import Ui_High_Data_Fusion
from basemethod.PSO_SVR import *


class ui_low_or_mid_analysis(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =  Ui_Low_Or_Mid_Analysis()
        self.ui.setupUi(self)

        self.btn=self.ui.pushButton_2
        self.btn1=self.ui.pushButton
        self.cmbx=self.ui.comboBox
        self.checkbox=self.ui.checkBox

        self.results = self.ui.plainTextEdit
        self.btn1.clicked.connect(self.analy)
        self.cmbx.currentIndexChanged.connect(self.handleSelectionChange)
        self.checkbox.checkStateChanged.connect(self.plt)
        self.btn.clicked.connect(self.addtab)
        self.ui.tabWidget.currentChanged.connect(self.plot_tabdata)
    def handleSelectionChange(self):
        method = self.ui.comboBox.currentText()
        layout = self.ui.verticalLayout_4
        for i in range(layout.layout().count()):
            layout.layout().itemAt(i).widget().deleteLater()
        if method =='RF':
            layout.addWidget(Ui_Rf())
        elif method =='PSO-SVR':
            layout.addWidget(Ui_Svr())
        elif method=='PLSR':
            layout.addWidget(Ui_Plsr())
        else :
            layout.addWidget(Ui_Rf())
    def addtab(self):
        global i
        self.ui.tabWidget.addTab(Ui_Feature_Extraction(),'data'+str(i))
        i+=1
    def analy(self):
        tab_num=self.ui.tabWidget.count()
        diclist=[]
        for tab_id in range(tab_num):
            hara=[]
            current_tab_widget=self.ui.tabWidget.widget(tab_id)
            csvname=current_tab_widget.ui.lineEdit_26.text()
            premethod=current_tab_widget.ui.comboBox.currentText()
            featuremethod=current_tab_widget.ui.comboBox_2.currentText()
            if featuremethod == 'VIP':
                vipfeaturelayout =current_tab_widget.ui.verticalLayout_2.layout().itemAt(0).wid.ui.lineEdit.text()
                vipfeaturelayout2 = current_tab_widget.ui.verticalLayout_2.layout().itemAt(0).wid.ui.lineEdit_2.text()
                hara.append(vipfeaturelayout)
                hara.append(int(vipfeaturelayout2))
            elif featuremethod == 'CARS':
                carsit = current_tab_widget.ui.verticalLayout_2.layout().itemAt(0).wid.ui.lineEdit.text()
                carscv = current_tab_widget.ui.verticalLayout_2.layout().itemAt(0).wid.ui.lineEdit_2.text()
                carsnc = current_tab_widget.ui.verticalLayout_2.layout().itemAt(0).wid.ui.lineEdit_3.text()
                hara.append(int(carsit))
                hara.append(int(carsnc))
                hara.append(int(carscv))
            elif featuremethod=='iPLS':
                iplssize = self.ui.tabWidget.widget(tab_id).ui.verticalLayout_2.layout().itemAt(0).wid.ui.lineEdit.text()
                iplsnum = self.ui.tabWidget.widget(tab_id).ui.verticalLayout_2.layout().itemAt(0).wid.ui.lineEdit_2.text()
                iplsselectnum = self.ui.tabWidget.widget(tab_id).ui.verticalLayout_2.layout().itemAt(0).wid.ui.lineEdit_3.text()
                hara.append(float(iplssize))
                hara.append(int(iplsnum))
                hara.append(int(iplsselectnum))
            else:
                pass
            dic={
                'csvname':csvname,
                'featuremethod':featuremethod,
                'premethod':premethod,
                'hara':hara
            }
            diclist.append(dic)
        regressiondic={
        'rf_state':False,
        'svr_state':False,
        'plsr_state':False,
        }
        regressionmethod=self.ui.comboBox.currentText()
        if regressionmethod =='RF':
            rfnc=self.ui.verticalLayout_4.layout().itemAt(0).wid.ui.lineEdit.text()
            regressiondic['rf_number']=int(rfnc)
            regressiondic['rf_state']=True
        elif regressionmethod =='PSO-SVR':
            svrc = self.ui.verticalLayout_4.layout().itemAt(0).wid.ui.lineEdit.text()
            svrg = self.ui.verticalLayout_4.layout().itemAt(0).wid.ui.lineEdit_2.text()
            svrk = self.ui.verticalLayout_4.layout().itemAt(0).wid.ui.lineEdit_3.text()
            svrpso = self.ui.verticalLayout_4.layout().itemAt(0).wid.ui.checkBox.isChecked()
            regressiondic['svr_c']=float(svrc)
            regressiondic['svr_g'] =float(svrg)
            regressiondic['svr_k'] =svrk
            regressiondic['svr_pso'] =svrpso
            regressiondic['svr_state'] = True
        elif regressionmethod=='PLSR':
            plsrnc=self.ui.verticalLayout_4.layout().itemAt(0).wid.ui.lineEdit.text()
            regressiondic['plsr_state']=True
            regressiondic['plsr_nc']=int(plsrnc)
        data = cal_fusion_data(diclist)

        spilttype = self.ui.comboBox_2.currentText()
        spiltinformation=self.ui.lineEdit.text()

        if spilttype == '随机划分':
            train_data, test_data, train_label, test_label = data.getttdata(float(spiltinformation))
        elif spilttype == 'KS划分':
            train_data, test_data, train_label, test_label = data.getksdata(float(spiltinformation))
        elif spilttype == '他验证':
            spiltinformation=spiltinformation.split(',')
            spiltinformation=[ float(label) for label in spiltinformation]
            train_data, test_data, train_label, test_label = data.getelsedata(spiltinformation)
        elif spilttype == '交叉验证':
            train_data, test_data, train_label, test_label = data.getcvdata(int(spiltinformation))

        if regressiondic['rf_state']:
            model = RandomForestRegressor(regressiondic['rf_number'])
        elif regressiondic['svr_state']:
            if regressiondic['svr_state']:
                model=optimize_svm(train_data, train_label, test_data, test_label)
            else:
                model = sklearn.svm.SVR(epsilon=regressiondic['svr_g'], C=regressiondic['svr_c'], kernel=regressiondic['svr_k'])
        elif regressiondic['plsr_state']:
            model = PLSRegression(n_components=regressiondic['plsr_nc'])
        else:
            print('未选择定量模型')




        modelev = ME()
        calibration_labels, predict_labels, calibration_r2, predict_r2, calibration_mse, predict_mse, calibration_rpd, predict_rpd,test_label = modelev.caleva(
                model, train_data, test_data, train_label, test_label)
        self.results.appendPlainText('训练集R2：'+str(calibration_r2[0]))
        self.results.appendPlainText('预测集R2：' + str(predict_r2[0]))
        self.results.appendPlainText('训练集RMSE：' + str(calibration_mse[0]))
        self.results.appendPlainText('预测集R2：' + str(predict_mse[0]))
        self.results.appendPlainText('训练集RPD：' + str(calibration_rpd[0]))
        self.results.appendPlainText('预测集RPD：' + str(predict_rpd[0]))
        self.results.appendPlainText('                  ')
        self.plot_results(test_label,predict_labels)

    def plot_tabdata(self):
        self.checkbox.setChecked(False)
        tadid=self.ui.tabWidget.currentIndex()
        print(tadid)
        if type(tadid) != int:
            pass
        else:
            csvname=self.ui.tabWidget.widget(tadid).ui.lineEdit_26.text()
            if csvname =='':
                pass
            else:
                fig=plot_data(csvname=self.ui.tabWidget.widget(tadid).ui.lineEdit_26.text())
                widget_plt = self.ui.widget_results
                data_fic=MplCanvas(self,fig)
                toolbar = NavigationToolbar(data_fic, self)
                layout=QVBoxLayout()
                layout.addWidget(toolbar)
                layout.addWidget(data_fic)
                widget_plt.setLayout(layout)
    def plt(self):
        if self.checkbox.isChecked():
            self.plot_tabdata()
        else:
            pass
    def plot_results(self,ture_labels,predict_labels):
        fig=plt_results(ture_labels,predict_labels)
        widget_plt = self.ui.widget_plt
        data_fic = MplCanvas(self, fig)
        toolbar = NavigationToolbar(data_fic, self)
        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(data_fic)
        widget_plt.setLayout(layout)
        pass




class ui_high_new(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_High_Data_Fusion()
        self.ui.setupUi(self)

        self.feature_extract_cbox=self.ui.comboBox_3
        self.btn=self.ui.pushButton
        self.cmbx=self.ui.comboBox_3

        self.cmbx.currentIndexChanged.connect(self.handleSelectionChange)
        self.ui.comboBox_4.currentIndexChanged.connect(self.handleSelectionChange2)
        self.btn.clicked.connect(self.addtab)

        self.ui.pushButton_2.clicked.connect(self.analy)
    def handleSelectionChange2(self):
        method = self.ui.comboBox_4.currentText()
        layout = self.ui.verticalLayout_4
        for i in range(layout.layout().count()):
            layout.layout().itemAt(i).widget().deleteLater()
        if method =='RF':
            layout.addWidget(Ui_Rf())
        elif method =='PSO-SVR':
            layout.addWidget(Ui_Svr())
        elif method=='PLSR':
            layout.addWidget(Ui_Plsr())
        else :
            layout.addWidget(Ui_Rf())
    def handleSelectionChange(self):
        method = self.ui.comboBox_3.currentText()
        layout = self.ui.verticalLayout_3
        for i in range(layout.layout().count()):
            layout.layout().itemAt(i).widget().deleteLater()
        if method =='iPLS':
            layout.addWidget(Ui_ipls())
        elif method =='CARS':
            layout.addWidget(Ui_Cars())
        elif method=='VIP':
            layout.addWidget(Ui_Vip())
        else :
            pass
    def addtab(self):
        global ii
        self.ui.tabWidget.addTab(Ui_First_Method_Select(),'算法'+str(ii))
        ii+=1
    def analy(self):
        csvname=self.ui.lineEdit.text()
        first_Kfold=int(self.ui.lineEdit_2.text())
        spilt_information=self.ui.lineEdit_3.text()
        spilt_type=self.ui.comboBox.currentText()
        premethod=self.ui.comboBox_2.currentText()

        feature_method=self.ui.comboBox_3.currentText()
        featurehara=[]
        if feature_method == 'VIP':
            vipnumber=self.ui.verticalLayout_3.layout().itemAt(0).wid.ui.lineEdit.text()
            vipselectnum=self.ui.verticalLayout_3.layout().itemAt(0).wid.ui.lineEdit_2.text()
            featurehara.append(int(vipnumber))
            featurehara.append(int(vipselectnum))
        elif feature_method =='CARS':
            carsit=self.ui.verticalLayout_3.layout().itemAt(0).wid.ui.lineEdit.text()
            carscv=self.ui.verticalLayout_3.layout().itemAt(0).wid.ui.lineEdit_2.text()
            carsnc=self.ui.verticalLayout_3.layout().itemAt(0).wid.ui.lineEdit_3.text()
            featurehara.append(int(carsit))
            featurehara.append(int(carsnc))
            featurehara.append(int(carscv))
        elif feature_method=='iPLS':
            iplssize = self.ui.verticalLayout_3.layout().itemAt(0).wid.ui.lineEdit.text()
            iplsnum = self.ui.verticalLayout_3.layout().itemAt(0).wid.ui.lineEdit_2.text()
            iplsselectnum = self.ui.verticalLayout_3.layout().itemAt(0).wid.ui.lineEdit_3.text()
            featurehara.append(float(iplssize))
            featurehara.append(int(iplsnum))
            featurehara.append(int(iplsselectnum))
        else:
            pass

        tab_num = self.ui.tabWidget.count()
        diclist = []
        for tab_id in range(tab_num):
            hara=[]
            firstdic={}
            current_tab_widget=self.ui.tabWidget.widget(tab_id)
            first_method=current_tab_widget.ui.comboBox.currentText()
            firstdic={'rf_state':False,
                      'svr_state':False,
                      'plsr_state':False,}
            if first_method =='RF':
                rfnc = current_tab_widget.ui.verticalLayout_2.layout().itemAt(0).wid.ui.lineEdit.text()
                firstdic['rf_number'] = int(rfnc)
                firstdic['rf_state'] = True
            elif first_method == 'PSO-SVR':
                svrc = current_tab_widget.ui.verticalLayout_2.layout().itemAt(0).wid.ui.lineEdit.text()
                svrg = current_tab_widget.ui.verticalLayout_2.layout().itemAt(0).wid.ui.lineEdit_2.text()
                svrk = current_tab_widget.ui.verticalLayout_2.layout().itemAt(0).wid.ui.lineEdit_3.text()
                svrpso = current_tab_widget.ui.verticalLayout_2.layout().itemAt(0).wid.ui.checkBox.isChecked()
                firstdic['svr_c'] = float(svrc)
                firstdic['svr_g'] = float(svrg)
                firstdic['svr_k'] = svrk
                firstdic['svr_pso'] = svrpso
                firstdic['svr_state'] = True
            elif first_method == 'PLSR':
                plsrnc = current_tab_widget.ui.verticalLayout_2.layout().itemAt(0).wid.ui.lineEdit.text()
                firstdic['plsr_state'] = True
                firstdic['plsr_nc'] = int(plsrnc)
            else:
                pass
            diclist.append(firstdic)

        secondregressiondic = {
            'rf_state': False,
            'svr_state': False,
            'plsr_state': False,
        }
        regressionmethod = self.ui.comboBox_4.currentText()
        if regressionmethod == 'RF':
            rfnc = self.ui.verticalLayout_4.layout().itemAt(0).wid.ui.lineEdit.text()
            secondregressiondic['rf_number'] = int(rfnc)
            secondregressiondic['rf_state'] = True
        elif regressionmethod == 'PSO-SVR':
            svrc = self.ui.verticalLayout_4.layout().itemAt(0).wid.ui.lineEdit.text()
            svrg = self.ui.verticalLayout_4.layout().itemAt(0).wid.ui.lineEdit_2.text()
            svrk = self.ui.verticalLayout_4.layout().itemAt(0).wid.ui.lineEdit_3.text()
            svrpso = self.ui.verticalLayout_4.layout().itemAt(0).wid.ui.checkBox.isChecked()
            secondregressiondic['svr_c'] = float(svrc)
            secondregressiondic['svr_g'] = float(svrg)
            secondregressiondic['svr_k'] = svrk
            secondregressiondic['svr_pso'] = svrpso
            secondregressiondic['svr_state'] = True
        elif regressionmethod == 'PLSR':
            plsrnc = self.ui.verticalLayout_4.layout().itemAt(0).wid.ui.lineEdit.text()
            secondregressiondic['plsr_state'] = True
            secondregressiondic['plsr_nc'] = int(plsrnc)
        calibration_labels, predict_labels, calibration_r2, predict_r2, calibration_mse, predict_mse, calibration_rpd, predict_rpd, fig, fig1= cal_evalluton_highdatafusion_new(csvname=csvname,premethodname=premethod,feature_method=feature_method,diclist=diclist,featurehara=featurehara,first_Kfold=first_Kfold,spilt_type=spilt_type,spilt_information=spilt_information,secondregressiondic=secondregressiondic)






        widget = self.ui.widget_plt
        sc=MplCanvas(self,fig)
        toolbar = NavigationToolbar( sc,self)
        layout=QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)
        widget.setLayout(layout)


        widget1 = self.ui.widget_results
        sc1=MplCanvas(self,fig1)
        toolbar = NavigationToolbar(sc1, self)
        layout=QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc1)
        widget1.setLayout(layout)

        self.ui.plainTextEdit.appendPlainText('训练集R2：'+str(calibration_r2[0]))
        self.ui.plainTextEdit.appendPlainText('预测集R2：' + str(predict_r2[0]))
        self.ui.plainTextEdit.appendPlainText('训练集RMSE：' + str(calibration_mse[0]))
        self.ui.plainTextEdit.appendPlainText('预测集R2：' + str(predict_mse[0]))
        self.ui.plainTextEdit.appendPlainText('训练集RPD：' + str(calibration_rpd[0]))
        self.ui.plainTextEdit.appendPlainText('预测集RPD：' + str(predict_rpd[0]))
        self.ui.plainTextEdit.appendPlainText('                  ')



class ui_main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =  Ui_Main()
        self.ui.setupUi(self)
        button2 = self.ui.pushButton_2
        button2.clicked.connect(self.open_new_window2)
        button3=self.ui.pushButton_3
        button3.clicked.connect(self.open_new_window3)
    def open_new_window2(self):
        self.window3 =ui_low_or_mid_analysis()
        self.window3.show()
        self.close()
    def open_new_window3(self):
        self.window3 =ui_high_new()
        self.window3.show()
        self.close()



if __name__ == "__main__":
    i=0
    ii=0
    app = QApplication(sys.argv)
    window =ui_main()
    window.show()
    sys.exit(app.exec_())