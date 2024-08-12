import numpy as np
from sklearn.cross_decomposition import PLSRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score, StratifiedShuffleSplit


class CARS:
    def __init__(self, X, y, iteration=50, n_comps=500, cv=10):
        self.iteration = iteration
        self.cv = cv
        self.n_comps = n_comps
        self.prob = 0.8
        self.X = X
        self.y = np.array(y)
        self.N, self.D = X.shape
        a = np.power((self.D/2), (1/(iteration-1)))
        k = (np.log(self.D/2))/(iteration-1)
        self.r = [round(a*np.exp(-(k*i))*self.D) for i in range(1, iteration+1)]

    def extract(self):
        weights = np.ones(self.D)/self.D
        RMSECV = []
        idWs = []
        idW = np.arange(self.D)
        for i in range(self.iteration):
            idCal = np.random.choice(np.arange(self.N),
                                     size=int(self.prob*self.N),
                                     replace=False)
            idW = np.random.choice(idW, self.r[i], p=weights, replace=True)
            idW = np.array(list(set(idW)))
            idWs.append(idW)
            X = self.X[idCal.reshape(-1, 1), idW]
            Y = self.y[idCal]
            comp = self.n_comps if len(idW) > self.n_comps else len(idW)
            pls = PLSRegression(comp)
            pls.fit(X, Y)
            absolute = pls.coef_.__abs__().reshape(-1)
            weights = absolute / sum(absolute)
            MSE = -cross_val_score(pls, X, Y, cv=self.cv, scoring="neg_mean_squared_error")
            RMSE = sum(MSE**(1/2))/self.cv
            RMSECV.append(RMSE)
        W = idWs[np.argmin(RMSECV)]
        return self.X[:,W],self.y,W

class VIP:
    def __init__(self,X,y,comp):
        self.X = X
        self.y = y
        self.n_comps=comp
    def extract(self,selectnum):
        #weights = np.ones(self.D) / self.D
        comp = self.n_comps
        pls = PLSRegression(comp)
        model=pls.fit(self.X, self.y)
        t = model.x_scores_
        w = model.x_weights_
        q = model.y_loadings_
        p, h = w.shape
        vips = np.zeros((p,))  # np.zeros()表示初始化0向量
        s = np.diag(np.matmul(np.matmul(np.matmul(t.T, t), q.T), q)).reshape(h, -1)
        # np.matmul(a,b)表示两个矩阵相乘;np.diag()输出矩阵中对角线上的元素，若矩阵是一维数组则输出一个以一维数组为对角线的矩阵
        total_s = np.sum(s)
        for i in range(p):
            weight = np.array([(w[i, j] / np.linalg.norm(w[:, j])) ** 2 for j in range(h)])
            # np.linarg.norm()表示求范数：矩阵整体元素平方和开根号，不保留矩阵二维特性
            vips[i] = np.sqrt(p * (np.matmul(s.T, weight)) / total_s)
            # s.T表示矩阵的转置
        W=np.where(np.argsort(vips)<=selectnum)[0]
        return self.X[:,W],self.y,W
class iPLS():
    def __init__(self, totaldata,totallabel,test_size,interval_num):
        split = StratifiedShuffleSplit(n_splits=1, test_size=test_size, random_state=42)
        for train_index, test_index in split.split(totaldata, totallabel):
            x_train=totaldata[list(train_index), :]
            y_train=np.array([totallabel[i] for i in train_index]).reshape(-1,1)
            x_test=totaldata[list(test_index), :]
            y_test=np.array([totallabel[i] for i in test_index]).reshape(-1,1)
        self.y_train=y_train
        self.y_test=y_test
        self.interval_num=interval_num
        feature_num = x_train.shape[1]
        x_train_block = {}
        x_test_black = {}
        remaining = feature_num % interval_num  # 用于检查是否能等分
        # （一）特征数量能够等分的情况
        if not remaining:
            interval_size = feature_num / interval_num  # 子区间波点数量
            for i in range(1, interval_num + 1):
                # （1）取对应子区间的光谱数据
                feature_start, feature_end = int((i - 1) * interval_size), int(i * interval_size)
                x_train_block[str(i)] = x_train[:, feature_start:feature_end]
                x_test_black[str(i)] = x_test[:, feature_start:feature_end]
        # （二）特征数量不能等分的情况(将多余波点等分到后面的几个区间里)
        else:
            separation = interval_num - remaining  # 前几个区间
            intervalsize1 = feature_num // interval_num
            intervalsize2 = feature_num // interval_num + 1

            # （2）前几个子区间(以separation为界)
            for i in range(1, separation + 1):
                feature_start, feature_end = int((i - 1) * intervalsize1), int(i * intervalsize1)
                x_train_block[str(i)] = x_train[:, feature_start:feature_end]
                x_test_black[str(i)] = x_test[:, feature_start:feature_end]

            # （3）后几个子区间(以separation为界)
            for i in range(separation + 1, interval_num + 1):
                feature_s = int((i - separation - 1) * intervalsize2) + feature_end
                feature_e = int((i - separation) * intervalsize2) + feature_end
                x_train_block[str(i)] = x_train[:, feature_s:feature_e]
                x_test_black[str(i)] = x_test[:, feature_s:feature_e]
        self.x_train_block=x_train_block
        self.x_test_black=x_test_black

    def extract(self,Selectnum):
        mse = []
        for i in range(1,  self.interval_num + 1):
            print("当前区间:", i)
            x_train_interval, x_test_interval = self.x_train_block[str(i)], self.x_test_black[str(i)]
            current_fn = x_train_interval.shape[1]
            if current_fn >= 100:
                ncom_upper = 100
            elif current_fn >= 50:
                ncom_upper = current_fn - 10
            else:
                ncom_upper = current_fn - 5
            ncomp = np.arange(5, ncom_upper)

            error = []
            for nc in ncomp:
                print("迭代当前主成分数量:", nc)
                pls = PLSRegression(n_components=nc,
                                    scale=True,
                                    max_iter=500,
                                    tol=1e-06,
                                    copy=True)
                pls.fit(x_train_interval, self.y_train.reshape(-1, 1))
                y_test_pred = pls.predict(x_test_interval)
                mse_temp = mean_squared_error(self.y_test, y_test_pred.ravel())
                error.append(mse_temp)
            mse.append(np.min(error))

        selcetval=np.where(np.argsort(mse)<=Selectnum-1)
        x_trains=[]
        x_tests=[]
        for i in selcetval[0]:
            x_train_interval, x_test_interval = self.x_train_block[str(i+1)], self.x_test_black[str(i+1)]
            x_trains.append(x_train_interval)
            x_tests.append(x_test_interval)
        x_train=np.concatenate(x_trains,1)
        x_test=np.concatenate(x_tests,axis=1)
        X=np.concatenate([x_train,x_test],axis=0)
        y=np.concatenate([self.y_train,self.y_test],axis=0)
        return X,y


