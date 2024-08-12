import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit, KFold
from basemethod.data import *
def checkequal(list):
    for i in range(len(list)):
        if list[i] != list[0]:
            return False
    return True
class DataFusion:
    def __init__(self,datalist=[]):
        self.datas=[]
        self.labels=[]
        if checkequal(self.labels):
            pass
        else:
            raise Exception("the label is not equal")
        for data in datalist:
            specdata,label=data.gettotaldata()
            self.datas.append(specdata)
            self.labels.append(label)
            self.label=label
        if len(self.datas)==1:
            self.dataformodel=self.datas[0]
        else:
            self.dataformodel = np.concatenate(self.datas, axis=1)
    def getttdata(self,test_size=0.3):
        totaldata=self.dataformodel
        totallabel=self.label
        split = StratifiedShuffleSplit(n_splits=1, test_size=test_size, random_state=42)
        for train_index, test_index in split.split(totaldata, totallabel):
            train_data=totaldata[list(train_index), :]
            train_label=np.array([totallabel[i] for i in train_index]).reshape(-1,1)
            test_data=totaldata[list(test_index), :]
            test_label=np.array([totallabel[i] for i in test_index]).reshape(-1,1)
        return train_data, test_data, train_label, test_label
    def getcvdata(self,Kfold=5):
        totaldata=self.dataformodel
        totallabel=self.label
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
    def gettotaldata(self):
        return self.dataformodel,self.label
    def getksdata(self,test_size):
        return ks(self.dataformodel,self.label,test_size)
    def getelsedata(self,testlabel):
        totallabel=list(set(self.label.tolist()))
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