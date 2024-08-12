#encoding=utf-8
import matplotlib
matplotlib.use('Qt5Agg')
from basemethod.data import *
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
        datas.append(data)
    data=DataFusion(datas)
    return data
def plot_data(csvname):
    data=originaldata(csvname)
    fig=data.plot()
    return fig
def plt_results(true_label,predict_labels):
    fig=plt.figure()
    plt.scatter(true_label,predict_labels,color='r')
    return fig
def cal_lowmid_results(dic):
    if dic['rf_state']:
        model = RandomForestRegressor(int(dic['rf_number']))
    elif dic['svr_state']:
        model = sklearn.svm.SVR(epsilon=dic['svr_g'], C=dic['svr_c'], kernel=dic['svr_k'])
    elif dic['plsr_state']:
        model = PLSRegression(n_components=dic['plsr_nc'])
def get_all_information_highdatafusion(ui):
    csvname=ui.lineEdit_csvname.text()
    firstst_state=ui.checkBox_1st.isChecked()
    normale_state=ui.checkBox_normal.isChecked()
    msc_state=ui.checkBox_msc.isChecked()
    snv_state=ui.checkBox_snv.isChecked()

    cars_state=ui.checkBox_cars.isChecked()
    cars_cv=ui.lineEdit_carscv.text()
    cars_iteration=ui.lineEdit_carsiteration.text()
    cars_nv=ui.lineEdit_carsnv.text()

    ipls_state=ui.checkBox_ipls.isChecked()
    ipls_internum=ui.lineEdit_iplsinternum.text()
    ipls_number=ui.lineEdit_iplsnumber.text()
    ipls_size=ui.lineEdit_iplssize.text()

    vip_state=ui.checkBox_vip.isChecked()
    vip_number=ui.lineEdit_vipnumber.text()

    first_Kfold=ui.lineEdit.text()



    rf_state=ui.checkBox_rf.isChecked()
    rf_number=ui.lineEdit_rfnumber.text()

    svr_state=ui.checkBox_svr.isChecked()
    svr_c=ui.lineEdit_svrc.text()
    svr_g=ui.lineEdit_svrg.text()
    svr_k=ui.lineEdit_svrk.text()

    plsr_state=ui.checkBox_plsr.isChecked()
    plsr_nc=ui.lineEdit_plsrnc.text()


    rf_state=ui.checkBox_rf.isChecked()
    rf_number_3=ui.lineEdit_rfnumber_3.text()

    svr_state=ui.checkBox_svr.isChecked()
    svr_c_3=ui.lineEdit_svrc_3.text()
    svr_g_3=ui.lineEdit_svrg_3.text()
    svr_k_3=ui.lineEdit_svrk_3.text()


    plsr_state=ui.checkBox_plsr.isChecked()
    plsr_nc_3=ui.lineEdit_plsrnc_3.text()

    ttspilt=ui.comboBox_traintestspilt.currentText()
    ttspilt_size=ui.lineEdit_traintestspilt.text()

    dic={
        'first_kfold':first_Kfold,
        'ttspilt':ttspilt,
        'ttspilt_size':ttspilt_size,
        'csvname':csvname,
        'firstst_state': firstst_state,
        'normal_state':normale_state,
        'msc_state':msc_state,
        'snv_state':snv_state,
        'cars_state':cars_state,
        'cars_cv':cars_cv,
        'cars_iteration':cars_iteration,
        'cars_nv':cars_nv,
        'ipls_state':ipls_state,
        'ipls_internum':ipls_internum,
        'ipls_number':ipls_number,
        'ipls_size':ipls_size,
        'vip_state':vip_state,
        'vip_number':vip_number,
        'rf_state':rf_state,
        'rf_number':rf_number,
        'svr_state':svr_state,
        'svr_c':svr_c,
        'svr_g':svr_g,
        'svr_k': svr_k,
        'plsr_state':plsr_state,
        'plsr_nc':plsr_nc,
        'rf_number_3': rf_number_3,
        'svr_c_3': svr_c_3,
        'svr_g_3': svr_g_3,
        'svr_k_3': svr_k_3
        , 'plsr_nc_3': plsr_nc_3,

    }
    return dic
def cal_evalluton_highdatafusion(dic):
    data = originaldata(dic['csvname'])
    if dic['msc_state']:
        data.preprocess('msc')
    if dic['snv_state']:
        data.preprocess('snv')
    if dic['normal_state']:
        data.preprocess('normal')
    if dic['firstst_state']:
        data.preprocess('1st')

    if dic['cars_state']:
        data.FeatureExtract('CARS', [int(dic['cars_iteration']), int(dic['cars_nv']), int(dic['cars_cv'])])
    if dic['ipls_state']:
        data.FeatureExtract('iPLS', [float(dic['ipls_size']), int(dic['ipls_number']), int(dic['ipls_internum'])])
    if dic['vip_state']:
        data.FeatureExtract('VIP', [int(dic['vip_number'])])
    model1=RandomForestRegressor(int(dic['rf_number']))
    model2= sklearn.svm.SVR(epsilon=float(dic['svr_g']), C=float(dic['svr_c']), kernel=dic['svr_k'])
    model3= PLSRegression(n_components=int(dic['plsr_nc']))

    if dic['rf_state']:
        model = RandomForestRegressor(int(dic['rf_number_3']))
    elif dic['svr_state']:

        model = sklearn.svm.SVR(epsilon=float(dic['svr_g_3']), C=float(dic['svr_c_3']), kernel=dic['svr_k_3'])
    elif dic['plsr_state']:
        model = PLSRegression(n_components=int(dic['plsr_nc_3']))
    else:
        print('fail')
    if dic['ttspilt'] == '随机划分':
        train_data, test_data, train_label, test_label = data.getttdata(dic['ttspilt_size'])
    elif dic['ttspilt'] == 'KS划分':
        train_data, test_data, train_label, test_label = data.getksdata(dic['ttspilt_size'])
    elif dic['ttspilt'] == '他验证':
        train_data, test_data, train_label, test_label = data.getelsedata([33.2,78.2,128.2])
    elif dic['ttspilt'] == '交叉验证':
        train_data, test_data, train_label, test_label = data.getcvdata(dic['ttspilt_size'])
    modelev = ME()
    calibration_labels, predict_labels, calibration_r2, predict_r2, calibration_mse, predict_mse, calibration_rpd, predict_rpd,test_label = modelev.highfusion(
     [model1,model2,model3],model,int(dic['first_kfold']),data,datatesttype=dic['ttspilt'],para=dic['ttspilt_size'])
    fig=data.plot()
    fig1=pltresults(test_label,predict_labels[0])
    return calibration_labels, predict_labels, calibration_r2, predict_r2, calibration_mse, predict_mse, calibration_rpd, predict_rpd,fig,fig1


def cal_evalluton_highdatafusion_new(csvname,premethodname,feature_method,diclist,featurehara,first_Kfold,spilt_type,spilt_information,secondregressiondic):
    data = originaldata(csvname)
    data.preprocess(premethodname)
    data.FeatureExtract(feature_method,featurehara)


    models=[]

    if spilt_type == '随机划分':
        train_data, test_data, train_label, test_label = data.getttdata(spilt_information)
    elif spilt_type == 'KS划分':
        train_data, test_data, train_label, test_label = data.getksdata(spilt_information)
    elif spilt_type == '他验证':
        train_data, test_data, train_label, test_label = data.getelsedata(spilt_information)
    elif spilt_type == '交叉验证':
        train_data, test_data, train_label, test_label = data.getcvdata(spilt_information)

    for modelhara in diclist:
        if modelhara['rf_state']:
            model = RandomForestRegressor(modelhara['rf_number'])
        elif modelhara['svr_state']:
            if modelhara['svr_pso']:
                model = optimize_svm(train_data, train_label, test_data, test_label)

            else:
                model = sklearn.svm.SVR(epsilon=modelhara['svr_g'], C=modelhara['svr_c'], kernel=modelhara['svr_k'])
        elif modelhara['plsr_state']:
            model = PLSRegression(n_components=modelhara['plsr_nc'])
        else:
            pass
        models.append(model)

    if secondregressiondic['rf_state']:
        model = RandomForestRegressor(secondregressiondic['rf_number'])
    elif secondregressiondic['svr_state']:
        if secondregressiondic['svr_pso']:
            model = optimize_svm(train_data, train_label, test_data, test_label)
        else:
            model = sklearn.svm.SVR(epsilon=secondregressiondic['svr_g'], C=secondregressiondic['svr_c'], kernel=secondregressiondic['svr_k'])
    elif secondregressiondic['plsr_state']:
        model = PLSRegression(n_components=secondregressiondic['plsr_nc'])
    else:
        print('fail')






    modelev = ME()
    calibration_labels, predict_labels, calibration_r2, predict_r2, calibration_mse, predict_mse, calibration_rpd, predict_rpd,test_label = modelev.highfusion(
     models,model,first_Kfold,data,datatesttype=spilt_type,para=spilt_information)
    fig=data.plot()
    fig1=pltresults(test_label,predict_labels[0])
    return calibration_labels, predict_labels, calibration_r2, predict_r2, calibration_mse, predict_mse, calibration_rpd, predict_rpd,fig,fig1