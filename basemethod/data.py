import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.model_selection import StratifiedShuffleSplit, KFold
from basemethod.FeatureExtrac import CARS,iPLS,VIP
import matplotlib.pyplot as plt
from collections import OrderedDict
from pylab import mpl
from sklearn import preprocessing

def ks(x, y, test_size=0.2):
    """
    :param x: shape (n_samples, n_features)
    :param y: shape (n_sample, )
    :param test_size: the ratio of test_size (float)
    :return: spec_train: (n_samples, n_features)
             spec_test: (n_samples, n_features)
             target_train: (n_sample, )
             target_test: (n_sample, )
    """
    M = x.shape[0]
    y=np.array(y).reshape(-1,)
    N = round((1 - test_size) * M)
    samples = np.arange(M)

    D = np.zeros((M, M))

    for i in range((M - 1)):
        xa = x[i, :]
        for j in range((i + 1), M):
            xb = x[j, :]
            D[i, j] = np.linalg.norm(xa - xb)

    maxD = np.max(D, axis=0)
    index_row = np.argmax(D, axis=0)
    index_column = np.argmax(maxD)

    m = np.zeros(N)
    m[0] = np.array(index_row[index_column])
    m[1] = np.array(index_column)
    m = m.astype(int)
    dminmax = np.zeros(N)
    dminmax[1] = D[m[0], m[1]]

    for i in range(2, N):
        pool = np.delete(samples, m[:i])
        dmin = np.zeros((M - i))
        for j in range((M - i)):
            indexa = pool[j]
            d = np.zeros(i)
            for k in range(i):
                indexb = m[k]
                if indexa < indexb:
                    d[k] = D[indexa, indexb]
                else:
                    d[k] = D[indexb, indexa]
            dmin[j] = np.min(d)
        dminmax[i] = np.max(dmin)
        index = np.argmax(dmin)
        m[i] = pool[index]

    m_complement = np.delete(np.arange(x.shape[0]), m)

    spec_train = x[m, :]
    target_train = y[m]
    spec_test = x[m_complement, :]
    target_test = y[m_complement]
    return spec_train, spec_test, target_train, target_test
def sk(x,y,test_size=0.2):

    split = StratifiedShuffleSplit(n_splits=1, test_size=test_size, random_state=42)
    for train_index, test_index in split.split(x, y):
        train_data = x[list(train_index), :]
        train_label = np.array([y[i] for i in train_index]).reshape(-1, 1)
        test_data = x[list(test_index), :]
        test_label = np.array([y[i] for i in test_index]).reshape(-1, 1)
    return train_data, test_data, train_label.reshape(-1, ), test_label.reshape(-1, )
def cv(totaldata, totallabel,Kfold=5):
    cv = KFold(n_splits=Kfold, shuffle=True, random_state=42)
    train_data = []
    train_label = []
    test_data = []
    test_label = []
    for train_index, test_index in cv.split(totaldata, totallabel):
        train_data.append(totaldata[list(train_index), :])
        train_label.append([totallabel[i] for i in train_index])
        test_data.append(totaldata[list(test_index), :])
        test_label.append([totallabel[i] for i in test_index])
    return train_data, test_data, train_label, test_label
def trans_label(index):
    labels=[]
    for i in index:
        labels.append()
    return labels

class originaldata():
    def __init__(self,path=r'C:\Users\16609\Desktop\光谱融合LIBS数据\classcsv\NIRS.csv'):
        self.data=pd.read_csv(path,index_col=0)
        self.label=[]
        for i in self.data.index:
            if i =='黑土':
                self.label.append(78.348)
            elif i=='赤红壤':
                self.label.append(11.59)
            elif i=='黄土':
                self.label.append(19.096)
            elif i=='褐土':
                self.label.append(27.627)
            elif i=='水稻土':
                self.label.append(29.454)
            elif i=='紫色土':
                self.label.append(9.777)
            elif i=='红壤土':
                self.label.append(37.56)
            else:
                self.label.append(float(i.split('ppm')[0]))
                #self.label.append(float(i))
        self.dataformodel=self.data.values
    def getlabel(self):
        return self.label
    def preprocess(self,name='snv'):
        if name=='snv' or name =='SNV':
            mean = np.mean(self.dataformodel, axis=1, keepdims=True)
            std = np.std(self.dataformodel, axis=1, keepdims=True)
            # 对每个样本进行标准化
            snv_data = (self.dataformodel - mean) / std
            self.dataformodel=snv_data
        elif name=='msc'or name =='MSC':
            ref_spectrum = np.mean(self.dataformodel, axis=0)
            corrected_data = np.zeros_like(self.dataformodel)
            for i in range(self.dataformodel.shape[0]):
                # 对每个样本进行最小二乘线性回归
                fit = np.polyfit(ref_spectrum, self.dataformodel[i, :], 1)
                # 应用校正
                corrected_data[i, :] = (self.dataformodel[i, :] - fit[1]) / fit[0]
            self.dataformodel=corrected_data
        elif name=='1st'or name =='1ST':
            a=self.data.columns
            x=[ float(i) for i in self.data.columns.values]
            dx = np.diff(x)
            # 注意这里，我们用dx[0]来近似所有波长间的差值，这是一个简化假设，通常光谱波长间隔是均匀的
            derivative_spectra = np.diff(self.dataformodel) / dx[0]
            # x坐标为原始x坐标的中点
            #x_mid_points = (x[:-1] + x[1:]) / 2
            self.dataformodel=derivative_spectra
        elif name =='Normal':
            minmax=preprocessing.MinMaxScaler()
            self.dataformodel=minmax.fit_transform(self.dataformodel)

        else:
            pass
    def SelectWavenumber(self,wavenumber):
        if wavenumber[0]==None or wavenumber[1]==None:
            pass
        else:
            ssss=self.data.columns.values.astype(np.float64)
            ss=np.where(ssss<=wavenumber[0])
            sss=np.where(ssss>=wavenumber[1])
            select=np.intersect1d(ss[0],sss[0])
            self.dataformodel=self.dataformodel[:,select]
    def FeatureExtract(self,name,highpara=[]):
        if name =='CARS':
            cars=CARS(self.dataformodel,self.label,highpara[0],highpara[1],cv=highpara[2])
            self.dataformodel,self.label,select=cars.extract()
        elif name=='VIP':
            vip=VIP(self.dataformodel,self.label,int(highpara[0]))
            self.dataformodel,self.label,select=vip.extract(highpara[1])
        elif name=='iPLS':
            ipls=iPLS(self.dataformodel,self.label,highpara[0],highpara[1])
            self.dataformodel, self.label=ipls.extract(highpara[2])
        elif name=='PCA':
            pca=PCA(n_components=highpara[0])
            self.dataformodel=pca.fit_transform(self.dataformodel)
            self.datapca=pd.DataFrame(self.dataformodel,index=self.label)
        else:
            pass
    def plot(self):
        mpl.rcParams["font.sans-serif"] = ["SimHei"]
        fig = plt.figure()
        data = self.data.T
        index = data.columns.values
        index = np.unique(index)
        colors = ['black', 'bisque', 'lightgreen', 'r', 'y', 'c', 'blue', 'pink', 'wheat','plum','slategrey']
        i = 0
        xlabel = data.index.values
        xlabel = [float(i) for i in xlabel]
        xlabels = np.linspace(xlabel[0], xlabel[-1], 5)
        for name in index:
            y = data[name].values
            plt.plot(xlabel, y, color=colors[i], label=name)
            i += 1
        plt.xticks(xlabels)
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = OrderedDict(zip(labels, handles))
        plt.legend(by_label.values(), by_label.keys())
        return fig
    def plotpca(self):
        mpl.rcParams["font.sans-serif"] = ["SimHei"]
        data = self.data.T
        index = data.columns.values
        index = np.unique(index)
        colors = ['black', 'bisque', 'lightgreen', 'r', 'y', 'c', 'blue', 'pink', 'wheat','plum','slategrey']
        i = 0
        xlabel = data.index.values
        xlabel = [float(i) for i in xlabel]
        xlabels = np.linspace(xlabel[0], xlabel[-1], 5)
        for name in index:
            y = data[name].values
            plt.scatter(y[0],y[1], color=colors[i], label=name)
            i += 1
        plt.xticks(xlabels)
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = OrderedDict(zip(labels, handles))
        plt.legend(by_label.values(), by_label.keys())
        plt.show()
        pass

    def getttdata(self,test_size=0.3):
        totaldata=self.dataformodel
        totallabel=self.label
        return sk(totaldata,totallabel,test_size=test_size)
    def getcvdata(self,Kfold=5):
        totaldata=self.dataformodel
        totallabel=self.label
        return cv(totaldata,totallabel,Kfold)
    def gettotaldata(self):
        return self.dataformodel,np.array(self.label)
    def getksdata(self,test_size):
        return ks(self.dataformodel,self.label,test_size)
    def getelsedata(self,testlabel):
        totallabel=list(set(self.label))
        trainlabel=list(set(totallabel)-set(testlabel))
        indexs=[]

        labels=np.array(self.label)
        for i in testlabel:
            index=np.where(labels==float(i))
            indexs.append(index)
        selected=np.concatenate(indexs,axis=1)
        test_data=self.dataformodel[selected,:].squeeze(0)
        s=selected.tolist()[0]
        test_label=[self.label[i] for i in s ]
        indexs=[]
        labels=np.array(self.label)
        for i in trainlabel:
            index=np.where(labels==float(i))
            indexs.append(index)
        selected=np.concatenate(indexs,axis=1)
        train_data=self.dataformodel[selected,:].squeeze(0)
        s=selected.tolist()[0]
        train_label=[self.label[i] for i in s ]
        return train_data, test_data, np.array(train_label).reshape(-1,), np.array(test_label).reshape(-1,)










