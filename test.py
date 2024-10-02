import pandas as pd
import numpy as np

data=pd.read_csv(r'C:\Users\16609\Desktop\LIBS.csv',header=None,).values
np.set_printoptions(precision=4)
train_data=data[:141,:-2]
train_label=data[:141,-1].reshape(-1,1)
test_data=data[141:,:-2]
test_label=data[141:,-1].reshape(-1,1)

from sklearn.preprocessing import MinMaxScaler

scaler_input=MinMaxScaler(feature_range=(0,1))
P_train_normalized = scaler_input.fit_transform(train_data)
P_test_normalized = scaler_input.transform(test_data)

scaler_output = MinMaxScaler(feature_range=(0, 1))
T_train_normalized = scaler_output.fit_transform(train_label)
T_test_normalized = scaler_output.transform(test_label)


from sklearn.svm import SVR
svr = SVR(kernel='rbf', C=0.381, gamma= 0.1,epsilon=0.01)
svr.fit(P_train_normalized, T_train_normalized)
predict=svr.predict(P_test_normalized).reshape(-1,1)
predict= scaler_output.inverse_transform(predict)

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
print(r2_score(predict,test_label))
