from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import numpy as np
from basemethod.data import *
from scipy.stats import pearsonr
def cal(model,train_data, test_data, train_label, test_label,type='s',Kfold=None):
    calibration_labels = []
    predict_labels = []
    calibration_r2 = []
    predict_r2 = []
    calibration_mse = []
    predict_mse = []
    calibration_rpd = []
    predict_rpd = []
    calibration_label=[]
    predict_label=[]
    if  type == 'cv':
        for i in range( Kfold):
            model.fit(train_data[i], train_label[i])
            calibration_label.append(model.predict(train_data[i]))
            predict_label.append(model.predict(test_data[i]))
            calibration_r2.append(r2_score(train_label[i], calibration_label[i]))
            predict_r2.append(r2_score(test_label[i], predict_label[i]))
            calibration_mse.append(mean_squared_error(train_label[i], calibration_label[i]))
            predict_mse.append(mean_squared_error(test_label[i], predict_label[i]))
            calibration_labels.append(calibration_label[i])
            predict_labels.append(predict_label[i])
            calibration_rpd.append(np.std(train_label) / calibration_mse)
            predict_rpd.append(np.std(test_label) / predict_mse)
            return calibration_labels, predict_labels, calibration_r2, predict_r2, calibration_mse, predict_mse, calibration_rpd, predict_rpd
    else:
        model.fit(train_data, train_label)
        calibration_label = model.predict(train_data)
        predict_label = model.predict(test_data)
        calibration_r2.append(r2_score(train_label, calibration_label))
        predict_r2.append(r2_score(test_label, predict_label))
        calibration_mse.append(mean_squared_error(train_label, calibration_label))
        predict_mse.append(mean_squared_error(test_label, predict_label))
        calibration_labels.append(calibration_label)
        predict_labels.append(predict_label)
        calibration_rpd.append(np.std(train_label) / calibration_mse)
        predict_rpd.append(np.std(test_label) / predict_mse)
        # print(np.corrcoef(train_label, y=calibration_label))
        # print(np.corrcoef(test_label, y=predict_label))
        return calibration_labels, predict_labels, calibration_r2, predict_r2, calibration_mse, predict_mse, calibration_rpd, predict_rpd,test_label


class ME:
    def __init__(self):
        pass
    def caleva(self,model,train_data, test_data, train_label, test_label,type='s'):
        self.model=model
        return cal(model,train_data,test_data,train_label,test_label,type=type)
    def highfusion(self,models,highmodel,Kfold,data,datatesttype,para):
        train_data, test_data, train_label, test_label =data.getcvdata(Kfold)
        highdata=[]
        modellabel=[]
        for i in range(Kfold):
            modeldata=[]
            for model in models:
                model.fit(train_data[i],train_label[i])
                modeldata.append(model.predict(test_data[i]).reshape(-1,1))
            modellabel.append(test_label[i])
            highdata.append(np.concatenate(modeldata,axis=1))
        highdata=np.concatenate(highdata,axis=0)
        highlabel=np.concatenate(modellabel)
        if datatesttype== '随机划分':
            train_data, test_data, train_label, test_label = data.getttdata(para)
        elif datatesttype== 'KS划分':
            train_data, test_data, train_label, test_label = data.getksdata(para)
        elif datatesttype == '他验证':
            train_data, test_data, train_label, test_label = data.getelsedata(para)
        elif datatesttype == '交叉验证':
            train_data, test_data, train_label, test_label = data.getcvdata(para)
        return cal(highmodel,train_data, test_data, train_label, test_label)