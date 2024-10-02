#encoding=utf-8
import sys
import matplotlib
matplotlib.use('Qt5Agg')
from ui.ui_main import Ui_Main
from ui.ui_low_or_mid_analysis import Ui_Low_Or_Mid_Analysis
from inituiandmethod.init_ui import *
import sklearn.svm
from inituiandmethod.init_method import *
from basemethod.ModelEvaluation import *
from ui.ui_high_data_fusion import Ui_High_Data_Fusion
from basemethod.PSO_SVR import *
from basemethod.GA import *
from basemethod.GWO import *
from ui.ui_unit_data import *
import os
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QFileDialog
class ui_unit_data(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Unit_Data()
        self.ui.setupUi(self)
        btn=self.ui.pushButton
        btn.clicked.connect(self.unit_data)
        self.btngetcsv=self.ui.btn
        self.btngetcsv.clicked.connect(self.getcsv)
        self.ui.btnallcsv.clicked.connect(self.getccsv)
        self.ui.returnbutton.clicked.connect(self.retrunmain)
    def retrunmain(self):
        self.window3 =ui_main()
        self.window3.show()
        self.close()
    def getcsv(self):
        csvname=QFileDialog().getExistingDirectory(self,'选择储存csv文件路径',"", "All Files (*)")
        self.ui.csvname.setText(csvname)
        self.csvnametocsave=csvname
    def getccsv(self):
        csvname=QFileDialog.getExistingDirectory(self,'选择csv文件路径','./',)
        self.ui.labelall.setText(csvname)
        self.csvname=csvname
    def unit_data(self):

        path=self.csvname
        path_to_save = self.csvnametocsave
        alldata = {}
        for labelname in os.listdir(path):
            NIRSdata = []
            for csvname in os.listdir(path + os.sep + labelname):
                data = pd.read_csv(path + os.sep + labelname + '\\' + csvname, header=None).values
                NIRSdata.append(data[:, 1].reshape(-1, 1))
            sampledata = np.concatenate(NIRSdata, axis=1)
            sampledata = np.concatenate([data[:, 0].reshape(-1, 1), sampledata], axis=1)
            totaldata = pd.DataFrame(sampledata)
            alldata[labelname] = totaldata

        dataframes = []
        for labelname, data in alldata.items():
            s = data.values
            specdata = data.values[:, 1:].T
            wavenumber = data.values[:, 0].tolist()
            label = [labelname] * specdata.shape[0]

            dataframe = pd.DataFrame(data=specdata, index=label, columns=wavenumber)
            dataframes.append(dataframe)
        dataframe = pd.concat(dataframes, axis=0)
        dataframe.to_csv(path_to_save + os.sep + 'total_data.csv', encoding='utf_8_sig')

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
        self.returnbtn=self.ui.menureturn
        button_action = QAction('&return', self)
        button_action.triggered.connect(self.returnmain)

        self.returnbtn.addAction(button_action)
        self.btn1.clicked.connect(self.analy)
        self.cmbx.currentIndexChanged.connect(self.handleSelectionChange)
        self.checkbox.clicked.connect(self.plt)
        self.btn.clicked.connect(self.addtab)

    def handleSelectionChange(self):
        method = self.ui.comboBox.currentText()
        layout = self.ui.verticalLayout_4
        for i in range(layout.layout().count()):
            layout.layout().itemAt(i).widget().deleteLater()
        if method =='RF':
            layout.addWidget(Ui_Rf())
        elif method =='SVR':
            self.uisvr=Ui_Svr_new()
            layout.addWidget(self.uisvr)
        elif method=='PLSR':
            layout.addWidget(Ui_Plsr())
        else :
            layout.addWidget(Ui_Rf())
    def returnmain(self):
        self.window3 =ui_main()
        self.window3.show()
        self.close()
    def addtab(self):
        global i
        self.ui.tabWidget.addTab(Ui_Feature_Extraction(),'data'+str(i))
        i+=1


    def analy(self):
        tab_num=self.ui.tabWidget.count()
        diclist=[]
        for tab_id in range(tab_num):
            current_tab_widget=self.ui.tabWidget.widget(tab_id)
            csvname=current_tab_widget.ui.lineEdit_26.text()
            premethod=current_tab_widget.ui.comboBox.currentText()
            featuremethod=current_tab_widget.ui.comboBox_2.currentText()
            hara=get_feature_extraction_hara(featuremethod,current_tab_widget.ui.verticalLayout_2)
            dic={
                'csvname':csvname,
                'featuremethod':featuremethod,
                'premethod':premethod,
                'hara':hara
            }
            diclist.append(dic)
        regressionmethod=self.ui.comboBox.currentText()
        regressiondic=get_regression_hara(regressionmethod,self.ui.verticalLayout_4)
        data = cal_fusion_data(diclist)
        spilttype = self.ui.comboBox_2.currentText()
        spiltinformation=self.ui.lineEdit.text()

        train_data, test_data, train_label, test_label=get_dataset(spilttype,spiltinformation,data)
#C:\Users\16609\Desktop\research\Pb 定标\LIBS.csv
#C:\Users\16609\Desktop\光谱融合近红外数据\total_data.csv
        #33.2,78.2,128.2

        if regressiondic['rf_state']:
            model = RandomForestRegressor(regressiondic['rf_number'])
        elif regressiondic['svr_state']:
            optimizedic = self.uisvr.get_optimization_hara()
            if optimizedic['pso_state']:
                model=optimize_svm(train_data, train_label, test_data, test_label,dic=optimizedic)
                self.results.appendPlainText('PSO优化后的gamma：' + str(model.gamma))
                self.results.appendPlainText('PSO优化后的C：' + str(model.C))
            elif optimizedic['ga_state']:
                model=ga_optimize_svr(train_data, train_label, test_data, test_label,optimizationdic=optimizedic)
                self.results.appendPlainText('GA优化后的gamma：' + str(model.gamma))
                self.results.appendPlainText('GA优化后的C：' + str(model.C))
            elif optimizedic['gwo_state']:
                model=gwo_optimize(train_data, test_data, train_label, test_label,optimizationdic=optimizedic)
                self.results.appendPlainText('GWO优化后的gamma：' + str(model.gamma))
                self.results.appendPlainText('GWO优化后的C：' + str(model.C))
            else:
                model = sklearn.svm.SVR(gamma=regressiondic['svr_g'], C=regressiondic['svr_c'], kernel=regressiondic['svr_k'])
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
        self.results.appendPlainText('预测集RMSE：' + str(predict_mse[0]))
        self.results.appendPlainText('训练集RPD：' + str(calibration_rpd[0]))
        self.results.appendPlainText('预测集RPD：' + str(predict_rpd[0]))
        self.results.appendPlainText('                  ')
        self.plot_results(test_label,predict_labels,train_label,calibration_labels)
    def plot_tabdata(self):
        """
        绘制单独tab页的数据光谱图
        :return: None
        """
        #self.checkbox.setChecked(False)
        tadid=self.ui.tabWidget.currentIndex()

        if type(tadid) != int:
            pass
        else:
            csvname=self.ui.tabWidget.widget(tadid).ui.lineEdit_26.text()
            if csvname =='':
                pass
            else:
                widget_plt = self.ui.widget_results
                if widget_plt.layout()==None:
                    pass
                else:
                    widget_plt.layout().deleteLater()
                    item_list = list(range(widget_plt.layout().count()))
                    item_list.reverse()
                    for numss in item_list:
                        item = widget_plt.layout().itemAt(numss)
                        widget_plt.layout().removeItem(item)
                        

                fig=plot_data(csvname=csvname)
                data_fic=MplCanvas(self,fig)
                toolbar = NavigationToolbar(data_fic, self)
                layout=QVBoxLayout()
                layout.addWidget(toolbar)
                layout.addWidget(data_fic)
                widget_plt.setLayout(layout)
    def plt(self):
        self.plot_tabdata()
    def plot_results(self,true_label,predict_labels,train_label,predict_label):
        """
        这个函数主要用于绘制计算结果的图
        输入函数
        true_label：数据集测试集的真实值
        predict_labels：数据集测试集的预测值
        train_label：数据集训练集的真实值
        predict_label：数据集训练集的预测值
        """
        fig=plt_results(true_label,predict_labels,train_label,predict_label)

        widget_plt = self.ui.widget_plt

        # widget_plt.QVBoxLayout().deleteLater()
        data_fic = MplCanvas(self, fig)
        toolbar = NavigationToolbar(data_fic, self)
        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(data_fic)
        widget_plt.setLayout(layout)
class ui_high_new(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_High_Data_Fusion()
        self.ui.setupUi(self)

        self.feature_extract_cbox=self.ui.comboBox_3
        self.btn=self.ui.pushButton
        self.cmbx=self.ui.comboBox_3
        self.results = self.ui.plainTextEdit

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
        elif method =='SVR':
            self.uisvr=Ui_Svr_new()
            layout.addWidget( self.uisvr)
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
        featurehara=get_feature_extraction_hara(self.ui.verticalLayout_3,feature_method)



        tab_num = self.ui.tabWidget.count()
        diclist = []
        optimizedics=[]
        for tab_id in range(tab_num):
            current_tab_widget=self.ui.tabWidget.widget(tab_id)
            first_method=current_tab_widget.ui.comboBox.currentText()
            firstdic=get_regression_hara(first_method,current_tab_widget.ui.verticalLayout_2)
            if firstdic['svr_state']:
                optimizedic = get_optimization_hara(firstdic['svr_pso'],current_tab_widget.ui.verticalLayout_2.layout().itemAt(0).wid.ui.horizontalLayout_5)
                optimizedics.append(optimizedic)
            else:
                optimizedics.append([])

            diclist.append(firstdic)


        regressionmethod = self.ui.comboBox_4.currentText()
        secondregressiondic=get_regression_hara(regressionmethod,self.ui.verticalLayout_4)

        data = originaldata(csvname)
        data.preprocess(premethod)
        data.FeatureExtract(feature_method, featurehara)

        train_data, test_data, train_label, test_label=get_dataset(spilt_type,spilt_information,data)
        models=[]

        for i in range(len(diclist)):
            modelhara=diclist[i]

            if modelhara['rf_state']:
                model = RandomForestRegressor(modelhara['rf_number'])
            elif modelhara['svr_state']:
                optimizedic=optimizedics[i]
                if optimizedic['pso_state']:
                    model = optimize_svm(train_data, train_label, test_data, test_label, dic=optimizedic)
                    self.results.appendPlainText('PSO优化后的gamma：' + str(model.gamma))
                    self.results.appendPlainText('PSO优化后的C：' + str(model.C))
                elif optimizedic['ga_state']:
                    model = ga_optimize_svr(train_data, train_label, test_data, test_label, optimizationdic=optimizedic)
                    self.results.appendPlainText('GA优化后的gamma：' + str(model.gamma))
                    self.results.appendPlainText('GA优化后的C：' + str(model.C))
                elif optimizedic['gwo_state']:
                    model = gwo_optimize(train_data, test_data, train_label, test_label, optimizationdic=optimizedic)
                    self.results.appendPlainText('GWO优化后的gamma：' + str(model.gamma))
                    self.results.appendPlainText('GWO优化后的C：' + str(model.C))
                else:
                    model = sklearn.svm.SVR(gamma=modelhara['svr_g'], C=modelhara['svr_c'],
                                            kernel=modelhara['svr_k'])
            elif modelhara['plsr_state']:
                model = PLSRegression(n_components=modelhara['plsr_nc'])
            else:
                print('未选择定量模型')
            models.append(model)
        if secondregressiondic['rf_state']:
            model = RandomForestRegressor(secondregressiondic['rf_number'])
        elif secondregressiondic['svr_state']:
            optimizedic = get_optimization_hara(secondregressiondic['svr_pso'],self.ui.verticalLayout_4.layout().itemAt(0).wid.ui.horizontalLayout_5 )
            if optimizedic['pso_state']:
                model = optimize_svm(train_data, train_label, test_data, test_label, dic=optimizedic)
                self.results.appendPlainText('PSO优化后的gamma：' + str(model.gamma))
                self.results.appendPlainText('PSO优化后的C：' + str(model.C))
            elif secondregressiondic['ga_state']:
                model = ga_optimize_svr(train_data, train_label, test_data, test_label, optimizationdic=optimizedic)
                self.results.appendPlainText('GA优化后的gamma：' + str(model.gamma))
                self.results.appendPlainText('GA优化后的C：' + str(model.C))
            elif secondregressiondic['gwo_state']:
                model = gwo_optimize(train_data, test_data, train_label, test_label, optimizationdic=optimizedic)
                self.results.appendPlainText('GWO优化后的gamma：' + str(model.gamma))
                self.results.appendPlainText('GWO优化后的C：' + str(model.C))
            else:
                model = sklearn.svm.SVR(gamma=modelhara['svr_g'], C=modelhara['svr_c'],
                                        kernel=modelhara['svr_k'])
        elif secondregressiondic['plsr_state']:
            model = PLSRegression(n_components=modelhara['plsr_nc'])
        else:
            print('未选择定量模型')



        modelev = ME()
        calibration_labels, predict_labels, calibration_r2, predict_r2, calibration_mse, predict_mse, calibration_rpd, predict_rpd, test_label = modelev.highfusion(
            models, model, first_Kfold, data, datatesttype=spilt_type, para=spilt_information)
        fig = data.plot()
        fig1 = pltresults(test_label, predict_labels[0], train_label, calibration_labels)


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
        self.ui.plainTextEdit.appendPlainText('预测集RMSE：' + str(predict_mse[0]))
        self.ui.plainTextEdit.appendPlainText('训练集RPD：' + str(calibration_rpd[0]))
        self.ui.plainTextEdit.appendPlainText('预测集RPD：' + str(predict_rpd[0]))
        self.ui.plainTextEdit.appendPlainText('                  ')



class ui_main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =  Ui_Main()
        self.ui.setupUi(self)
        button1=self.ui.pushButton
        button1.clicked.connect(self.open_new_window1)
        button2 = self.ui.pushButton_2
        button2.clicked.connect(self.open_new_window2)
        button3=self.ui.pushButton_3
        button3.clicked.connect(self.open_new_window3)

    def open_new_window1(self):
        self.window3 =ui_unit_data()
        self.window3.show()
        self.close()
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