#encoding=utf-8
import numpy as np

class GWO:
    def __init__(self, fitness_func, dim, lb, ub, N, Max_iter):
        self.fitness_func = fitness_func  # 适应度函数
        self.dim = dim  # 变量维度
        self.lb = [int(a) for a in lb]  # 变量下限
        self.ub = [int(a) for a in ub]  # 变量上限
        self.N =int( N ) # 狼群数量
        self.Max_iter = int(Max_iter)  # 最大迭代次数

    def optimize(self):
        # 初始化狼群位置
        X = np.random.uniform(self.lb, self.ub, (self.N, self.dim))
        alpha_pos = np.zeros(self.dim)
        beta_pos = np.zeros(self.dim)
        delta_pos = np.zeros(self.dim)
        alpha_fit = float('-inf')
        beta_fit = float('-inf')
        delta_fit = float('-inf')

        # 迭代优化
        for t in range(self.Max_iter):
            for i in range(self.N):
                # 计算适应度
                fitness = self.fitness_func(X[i])
                if fitness > alpha_fit:
                    alpha_fit = fitness
                    alpha_pos = X[i].copy()
                elif fitness > beta_fit:
                    beta_fit = fitness
                    beta_pos = X[i].copy()
                elif fitness > delta_fit:
                    delta_fit = fitness
                    delta_pos = X[i].copy()

            # 更新狼群位置
            a = 2 - 2 * t / self.Max_iter
            for i in range(self.N):
                r1 = np.random.rand(self.dim)
                r2 = np.random.rand(self.dim)
                A = 2 * a * r1 - a
                C = 2 * r2
                D_alpha = np.abs(C * alpha_pos - X[i])
                X1 = alpha_pos - A * D_alpha
                r1 = np.random.rand(self.dim)
                r2 = np.random.rand(self.dim)
                A = 2 * a * r1 - a
                C = 2 * r2
                D_beta = np.abs(C * beta_pos - X[i])
                X2 = beta_pos - A * D_beta
                r1 = np.random.rand(self.dim)
                r2 = np.random.rand(self.dim)
                A = 2 * a * r1 - a
                C = 2 * r2
                D_delta = np.abs(C * delta_pos - X[i])
                X3 = delta_pos - A * D_delta
                X[i] = (X1 + X2 + X3) / 3

        # 记录最佳位置
        self.best_pos = alpha_pos

import numpy as np
from sklearn.svm import SVR


# 训练数据
def gwo_optimize(train_data, test_data, train_label, test_label,optimizationdic={}):



    N = optimizationdic['size_pop']
    Max_iter = optimizationdic['iteration']  # 最大迭代次数

    svm = SVR(kernel='rbf', C=1, gamma=0.1)

    def fitness_func(position):
        # 防止valueError
        if position[1] <= 0:
            position[1] = optimizationdic['g_low']
        if position[0] <= 0:
            position[0] =  optimizationdic['c_low']
        if position[1]>=optimizationdic['g_high']:
            position[1] = optimizationdic['g_high']
        if position[0]>=optimizationdic['c_high']:
            position[0] = optimizationdic['c_high']

        svm.set_params(C=position[0], gamma=position[1])
        svm.fit(train_data, train_label)
        y_pred = svm.predict(test_data)
        mse = np.mean((test_label - y_pred) ** 2)
        fitness = 1 / (mse + 1e-6)
        return fitness

    gwo = GWO(fitness_func, 2, lb=[optimizationdic['c_low'], optimizationdic['g_low']], ub=[optimizationdic['c_high'] , optimizationdic['g_high']], N=N, Max_iter=Max_iter)
    gwo.optimize()
    svm.set_params(C=gwo.best_pos[0], gamma=gwo.best_pos[1])
    return svm





