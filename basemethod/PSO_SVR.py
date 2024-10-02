# coding=utf-8
import numpy as np
from sklearn.svm import SVR
from matplotlib import pyplot as plt
from pyswarm import pso as ps


# 优化函数
def optimize_svm(train_data, train_label, test_data, test_label, n_particles=100, n_iterations=50,dic={}):
    def fitness_function(x, train_data, test_data, train_label, test_label):
        gamma, C = x
        svm_model = SVR(kernel='rbf', gamma=gamma, C=C)
        svm_model.fit(train_data, train_label)
        y_pred = svm_model.predict(test_data)
        mse = np.mean((test_label - y_pred) ** 2)
        return mse

    def con1(x, train_data, test_data, train_label, test_label):
        x1 = x[0]
        return x1

    def con2(x, train_data, test_data, train_label, test_label):

        x2 = x[1]
        return x2

    lb = [dic['c_low'], dic['g_low']]
    ub = [dic['c_high'], dic['g_high']]
    train_label=train_label.reshape(-1,)
    test_label=test_label.reshape(-1,)

    xopt, fopt = ps(fitness_function, lb, ub, f_ieqcons=None, ieqcons=[con1, con2],
                     args=(train_data, test_data, train_label, test_label), kwargs={},
                     swarmsize=100, omega=dic['w'], phip= dic['c2'], phig= dic['c1'], maxiter=50, minstep=1e-8,
                     minfunc=1e-8, debug=False)

    svm_model = SVR(kernel='rbf', gamma=xopt[1], C=xopt[0])


    return svm_model
