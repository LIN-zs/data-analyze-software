import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

#������
path=r'C:\Users\16609\Desktop\PP'
label = os.listdir(path)
index_row=[]
for k in range(20):
    ss='PP0.0%'
    s1=label[k][:3]
    s2=label[k][3:]
    label[k]=s1+ss+s2
for i in range(len(label)):
   if i%20==0:
       index_row.append(label[i])
   else:
       index_row.append(index_row[-1])
Y1=[]
for i in range(len(index_row)):
    temp=str(index_row[i])
    temp1=eval(temp[5:8])
    Y1.append(temp1)

#����
all_data=[]
path=r'C:\Users\16609\Desktop\PP'

fi_li=os.listdir(path)
for file in fi_li:
    fi_pa=os.path.join(path,file)
    all_data.append(pd.read_csv(fi_pa,names=['����','ǿ��']))
X1=[]
for every in all_data:
    temp=every['ǿ��']
    X1.append(temp)

#������
index_column=all_data[0]['����']

results_dict ={'R? Prediction':[],'MSE Prediction':[]}
for m in range(len(all_data)):
    X=[]
    for k in range(len(X1[m])):
        temp=X1[m]
        X.append(temp[k])
    Y=[]
    Y.append(Y1[m])
    Y=Y*1557



    X_train, X_test, Y_train, Y_test = train_test_split(X, Y1, test_size=0.3, random_state=42)
    X_train=np.array(X_train)
    X_train=X_train.reshape(-1,1)
    X_test=np.array(X_test)
    X_test=X_test.reshape(-1,1)


    model = LinearRegression()


    model.fit(X_train,Y_train)


    y_pred = model.predict(X_test)

    r2_test = r2_score(Y_test, y_pred)
    print(r2_test)
    mse_test = mean_squared_error(Y_test, y_pred)


    results_dict['R? Prediction'].append(r2_test)
    results_dict['MSE Prediction'].append(mse_test)



