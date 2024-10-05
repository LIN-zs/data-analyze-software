#encoding=utf-8
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('Qt5Agg')
from basemethod.FusionData import *
from sklearn.ensemble import RandomForestRegressor
from sklearn.cross_decomposition import PLSRegression
import sklearn.svm
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar

from basemethod.ModelEvaluation import *
from basemethod.PSO_SVR import *

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None,fig=0):
        fig = fig
        super(MplCanvas, self).__init__(fig)
def pltresults(true_label,predict_labels):
    fig=plt.figure()
    plt.scatter(true_label,predict_labels,color='r')
    return fig

def cal_fusion_data(dic_list):
    datas=[]
    for dic in dic_list:
        data=originaldata(dic['csvname'])
        data.preprocess(dic['premethod'])
        data.FeatureExtract(dic['featuremethod'],dic['hara'])
        data.SelectWavenumber(dic['select_wavenumber'])
        datas.append(data)
    data=DataFusion(datas)
    return data
def plot_data(csvname):
    """
    绘制输入数据的光谱图
    :param csvname: 光谱图的文件路径
    :return: matlab的figure对象
    """
    data=originaldata(csvname)
    fig=data.plot()
    return fig
def plt_results(true_label,predict_labels,train_label,predict_label):
    """
    该函数主要用于绘制数据分析结果的散点图并返回figure对象
    :param true_label: 测试集的真实值
    :param predict_labels: 测试集的预测值
    :param train_label: 训练集的真实值
    :param predict_label: 训练集的预测值
    :return:绘制好的matlab figure对象
    """
    fig=plt.figure()
    plt.scatter(true_label,predict_labels,color='r',marker='o',label='prediction set')
    plt.scatter(train_label,predict_label,color='b',marker='*',label='calibration set')
    plt.legend()
    return fig
def get_select_wavenumber(ui):
    wavenumber_low=ui.layout().itemAt(0).wid.ui.lineEdit_low.text()
    wavenumber_high=ui.layout().itemAt(0).wid.ui.lineEdit_high.text()
    return [wavenumber_low,wavenumber_high]
def get_feature_extraction_hara(featuremethod,layout):
    hara=[]
    if featuremethod == 'VIP':
        vipfeaturelayout = layout.layout().itemAt(0).wid.ui.lineEdit.text()
        vipfeaturelayout2 = layout.layout().itemAt(0).wid.ui.lineEdit_2.text()
        hara.append(vipfeaturelayout)
        hara.append(int(vipfeaturelayout2))
    elif featuremethod == 'CARS':
        carsit = layout.layout().itemAt(0).wid.ui.lineEdit.text()
        carscv = layout.layout().itemAt(0).wid.ui.lineEdit_2.text()
        carsnc = layout.layout().itemAt(0).wid.ui.lineEdit_3.text()
        hara.append(int(carsit))
        hara.append(int(carsnc))
        hara.append(int(carscv))
    elif featuremethod == 'iPLS':
        iplssize = layout.layout().itemAt(0).wid.ui.lineEdit.text()
        iplsnum = layout.layout().itemAt(0).wid.ui.lineEdit_2.text()
        iplsselectnum =layout.layout().itemAt(0).wid.ui.lineEdit_3.text()
        hara.append(float(iplssize))
        hara.append(int(iplsnum))
        hara.append(int(iplsselectnum))
    elif featuremethod == 'PCA':
        pcanc = layout.layout().itemAt(0).wid.ui.lineEdit.text()
        hara.append(int(pcanc))
    else:
        pass
    return hara
def get_regression_hara(regressionmethod,layout):
    regressiondic = {
        'rf_state': False,
        'svr_state': False,
        'plsr_state': False,
    }
    if regressionmethod == 'RF':
        rfnc = layout.layout().itemAt(0).wid.ui.lineEdit.text()
        regressiondic['rf_number'] = int(rfnc)
        regressiondic['rf_state'] = True
    elif regressionmethod == 'SVR':
        svrc = layout.layout().itemAt(0).wid.ui.lineEdit.text()
        svrg = layout.layout().itemAt(0).wid.ui.lineEdit_2.text()
        svrk = layout.layout().itemAt(0).wid.ui.lineEdit_3.text()
        svrpso = layout.layout().itemAt(0).wid.ui.comboBox.currentText()
        regressiondic['svr_c'] = float(svrc)
        regressiondic['svr_g'] = float(svrg)
        regressiondic['svr_k'] = svrk
        regressiondic['svr_pso'] = svrpso
        regressiondic['svr_state'] = True
    elif regressionmethod == 'PLSR':
        plsrnc = layout.layout().itemAt(0).wid.ui.lineEdit.text()
        regressiondic['plsr_state'] = True
        regressiondic['plsr_nc'] = int(plsrnc)

    return regressiondic
def get_optimization_hara(optimization_algorithms,layout):
    optimizationdic = {
        'pso_state': False,
        'ga_state': False,
        'gwo_state': False,
    }
    if optimization_algorithms =='PSO':
        optimizationdic['pso_state']=True
        c1=layout.layout().itemAt(0).wid.ui.lineEdit.text()
        c2=layout.layout().itemAt(0).wid.ui.lineEdit_5.text()
        w=layout.layout().itemAt(0).wid.ui.lineEdit_2.text()
        c_low=layout.layout().itemAt(0).wid.ui.lineEdit_8.text()
        c_high=layout.layout().itemAt(0).wid.ui.lineEdit_4.text()
        g_low=layout.layout().itemAt(0).wid.ui.lineEdit_7.text()
        g_high=layout.layout().itemAt(0).wid.ui.lineEdit_3.text()
        optimizationdic['c1']=float(c1)
        optimizationdic['c2'] = float(c2)
        optimizationdic['w'] = float(w)
        optimizationdic['c_low'] = float(c_low)
        optimizationdic['c_high'] = float(c_high)
        optimizationdic['g_low'] = float(g_low)
        optimizationdic['g_high'] = float(g_high)

    elif optimization_algorithms =='GWO':
        optimizationdic['gwo_state']=True
        iteration=layout.layout().itemAt(0).wid.ui.lineEdit.text()

        sizepop=layout.layout().itemAt(0).wid.ui.lineEdit_2.text()
        c_low=layout.layout().itemAt(0).wid.ui.lineEdit_8.text()
        c_high=layout.layout().itemAt(0).wid.ui.lineEdit_4.text()
        g_low=layout.layout().itemAt(0).wid.ui.lineEdit_7.text()
        g_high=layout.layout().itemAt(0).wid.ui.lineEdit_3.text()

        optimizationdic['iteration'] = float(iteration)
        optimizationdic['size_pop'] = float(sizepop)
        optimizationdic['c_low'] = float(c_low)
        optimizationdic['c_high'] = float(c_high)
        optimizationdic['g_low'] = float(g_low)
        optimizationdic['g_high'] = float(g_high)

    elif optimization_algorithms =='GA':
        optimizationdic['ga_state']=True
        maxgen=layout.layout().itemAt(0).wid.ui.lineEdit.text()
        crossrate=layout.layout().itemAt(0).wid.ui.lineEdit_10.text()
        sizepop=layout.layout().itemAt(0).wid.ui.lineEdit_2.text()
        c_low=layout.layout().itemAt(0).wid.ui.lineEdit_8.text()
        c_high=layout.layout().itemAt(0).wid.ui.lineEdit_4.text()
        g_low=layout.layout().itemAt(0).wid.ui.lineEdit_7.text()
        g_high=layout.layout().itemAt(0).wid.ui.lineEdit_3.text()
        mutationrate=layout.layout().itemAt(0).wid.ui.lineEdit_9.text()
        alpha=layout.layout().itemAt(0).wid.ui.lineEdit_5.text()
        optimizationdic['maxgen']=float(maxgen)
        optimizationdic['crossrate'] = float(crossrate)
        optimizationdic['sizepop'] = float(sizepop)
        optimizationdic['c_low'] = float(c_low)
        optimizationdic['c_high'] = float(c_high)
        optimizationdic['g_low'] = float(g_low)
        optimizationdic['g_high'] = float(g_high)
        optimizationdic['mutationrate'] = float(mutationrate)
        optimizationdic['alpha'] = float(alpha)
    else:
        pass
    return optimizationdic
def get_dataset(spilttype,spiltinformation,data):
    if spilttype == '随机划分':
        train_data, test_data, train_label, test_label = data.getttdata(float(spiltinformation))
    elif spilttype == 'KS划分':
        train_data, test_data, train_label, test_label = data.getksdata(float(spiltinformation))
    elif spilttype == '他验证':
        spiltinformation = spiltinformation.split(',')
        spiltinformation = [float(label) for label in spiltinformation]
        train_data, test_data, train_label, test_label = data.getelsedata(spiltinformation)
    elif spilttype == '交叉验证':
        train_data, test_data, train_label, test_label = data.getcvdata(int(spiltinformation))
    return train_data, test_data, train_label, test_label






