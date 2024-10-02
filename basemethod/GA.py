#encoding=utf-8
import random
import copy
import numpy as np
from sklearn import metrics
from sklearn.svm import SVR
import matplotlib.pyplot as plt



def fitness_function(params, X, y, xt, yt):
    C,gamma = params
    svm_model = SVR(kernel='rbf', gamma=gamma, C=C)
    svm_model.fit(X, y)
    y_pred = svm_model.predict(xt)
    mse = np.mean((yt - y_pred) ** 2)
    r2=metrics.r2_score(yt,y_pred)
    return r2

class GAIndividual:
    '''
    individual of genetic algorithm
    '''

    def __init__(self, vardim, bound,train_data, test_data, train_label, test_label):
        '''
        vardim: dimension of variables
        bound: boundaries of variables
        '''
        self.vardim = vardim
        self.bound = bound
        self.fitness = 0.
        self.train_data=train_data
        self.test_data=test_data
        self.train_label=train_label
        self.test_label=test_label

    def generate(self):
        '''
        generate a random chromsome for genetic algorithm
        '''

        len = self.vardim
        rnd = np.random.random(size=len)
        self.chrom = np.zeros(len)
        for i in range(0, len):
            self.chrom[i] = self.bound[0, i] + \
                            (self.bound[1, i] - self.bound[0, i]) * rnd[i]
    def exam_chrom(self):
        for i in range(self.vardim):
            if self.chrom[i]<self.bound[0, i]:
                self.chrom[i]=self.bound[0, i]
            if self.chrom[i]>self.bound[1, i]:
                self.chrom[i]=self.bound[1, i]

    def calculateFitness(self):
        '''
        calculate the fitness of the chromsome
        '''
        self.fitness =  fitness_function(self.chrom,X=self.train_data,y=self.train_label,xt=self.test_data,yt=self.test_label)

class GeneticAlgorithm:
    '''
    The class for genetic algorithm
    '''

    def __init__(self, sizepop, vardim, bound, MAXGEN, params,train_data, test_data, train_label, test_label):
        '''
        sizepop: population sizepop人口规模
        vardim: dimension of variables变量维数
        bound: boundaries of variables变量边界
        MAXGEN: termination condition终止条件
        param: algorithm required parameters, it is a list which is consisting of crossover rate, mutation rate, alpha
        '''
        self.sizepop = int(sizepop)
        self.MAXGEN = int(MAXGEN)
        self.vardim = vardim
        self.bound = bound
        self.population = []
        self.fitness = np.zeros((self.sizepop, 1))
        self.trace = np.zeros((self.MAXGEN, 3))
        self.params = params
        self.train_data=train_data
        self.test_data=test_data
        self.train_label=train_label
        self.test_label=test_label

    def initialize(self):
        '''
        initialize the population
        '''
        for i in range(0, self.sizepop):
            ind = GAIndividual(self.vardim, self.bound,self.train_data,self.test_data,self.train_label,self.test_label)
            ind.generate()
            self.population.append(ind)

    def evaluate(self):

        '''
        evaluation of the population fitnesses
        '''

        for i in range(0, self.sizepop):
            self.population[i].calculateFitness()
            self.fitness[i] = self.population[i].fitness

    def solve(self):
        '''
        evolution process of genetic algorithm
        '''
        self.t = 0
        self.initialize()
        self.evaluate()
        best = np.max(self.fitness)
        bestIndex = np.argmax(self.fitness)
        self.best = copy.deepcopy(self.population[bestIndex])
        self.avefitness = np.mean(self.fitness)
        self.maxfitness = np.max(self.fitness)

        self.trace[self.t, 0] = self.best.fitness
        self.trace[self.t, 1] = self.avefitness
        self.trace[self.t, 2] = self.maxfitness
        print("Generation %d: optimal function value is: %f; average function value is %f;max function value is %f" % (
            self.t, self.trace[self.t, 0], self.trace[self.t, 1], self.trace[self.t, 2]))


        while (self.t < self.MAXGEN - 1):
            self.t += 1
            self.selectionOperation()
            self.crossoverOperation()
            self.mutationOperation()
            self.evaluate()
            best = np.max(self.fitness)
            bestIndex = np.argmax(self.fitness)
            if best > self.best.fitness:
                self.best = copy.deepcopy(self.population[bestIndex])
            self.avefitness = np.mean(self.fitness)
            self.maxfitness = np.max(self.fitness)

            self.trace[self.t, 0] = self.best.fitness
            self.trace[self.t, 1] = self.avefitness
            self.trace[self.t, 2] = self.maxfitness
            print(
                "Generation %d: optimal function value is: %f; average function value is %f;max function value is %f" % (
                    self.t, self.trace[self.t, 0], self.trace[self.t, 1], self.trace[self.t, 2]))

        print("Optimal function value is: %f; " %
              self.trace[self.t, 0])
        print("Optimal solution is:")
        print(self.best.chrom)
        return  SVR(kernel='rbf', gamma=self.best.chrom[1], C=self.best.chrom[0])
       # self.printResult()

    def selectionOperation(self):
        '''
        selection operation for Genetic Algorithm
        '''

        newpop = []

        totalFitness = np.sum(self.fitness)

        accuFitness = np.zeros((self.sizepop, 1))



        sum1 = 0.

        for i in range(0, self.sizepop):

            accuFitness[i] = sum1 + self.fitness[i] / totalFitness
            sum1 = accuFitness[i]

        for i in range(0, self.sizepop):
            r = random.random()
            idx = 0
            for j in range(0, self.sizepop - 1):
                if j == 0 and r < accuFitness[j]:
                    idx = 0
                    break
                elif r >= accuFitness[j] and r < accuFitness[j + 1]:
                    idx = j + 1
                    break
            newpop.append(self.population[idx])

        self.population = newpop

    def crossoverOperation(self):
        '''
        crossover operation for genetic algorithm
        '''
        newpop = []
        for i in range(0, self.sizepop, 2):
            idx1 = random.randint(0, self.sizepop - 1)
            idx2 = random.randint(0, self.sizepop - 1)
            while idx2 == idx1:
                idx2 = random.randint(0, self.sizepop - 1)
            newpop.append(copy.deepcopy(self.population[idx1]))
            newpop.append(copy.deepcopy(self.population[idx2]))
            r = random.random()

            if r < self.params[0]:
                crossPos = random.randint(1, self.vardim - 1)
                for j in range(crossPos, self.vardim):
                    newpop[i].chrom[j] = newpop[i].chrom[j] * self.params[2] + (1 - self.params[2]) * newpop[i + 1].chrom[j]
                    newpop[i].exam_chrom()


                    newpop[i + 1].chrom[j] = newpop[i + 1].chrom[j] * self.params[2] + \
                                             (1 - self.params[2]) * newpop[i].chrom[j]
                    newpop[i+1].exam_chrom()
        self.population = newpop

    def mutationOperation(self):
        '''
        mutation operation for genetic algorithm
        '''
        newpop = []
        for i in range(0, self.sizepop):
            newpop.append(copy.deepcopy(self.population[i]))
            r = random.random()
            if r < self.params[1]:
                mutatePos = random.randint(0, self.vardim - 1)
                theta = random.random()
                if theta > 0.5:
                    newpop[i].chrom[mutatePos] = newpop[i].chrom[
                                                     mutatePos] - (
                                                             newpop[i].chrom[mutatePos] - self.bound[0, mutatePos]) * (
                                                             1 - random.random() ** (1 - self.t / self.MAXGEN))
                    newpop[i].exam_chrom()
                else:
                    newpop[i].chrom[mutatePos] = newpop[i].chrom[
                                                     mutatePos] + (
                                                             self.bound[1, mutatePos] - newpop[i].chrom[mutatePos]) * (
                                                             1 - random.random() ** (1 - self.t / self.MAXGEN))
                    newpop[i].exam_chrom()
        self.population = newpop

    def printResult(self):
        '''
        plot the result of the genetic algorithm
        '''
        x = np.arange(0, self.MAXGEN)
        y1 = self.trace[:, 0]
        y2 = self.trace[:, 1]
        y3 = self.trace[:, 2]
        # plt.plot(x, y1, 'r', label='optimal value')
        plt.plot(x, y2, 'g', label='average value')
        plt.plot(x, y3, 'b', label='max value')
        fig = plt.gcf()
        fig.set_size_inches(18.5, 10.5)
        plt.xlabel("GENS")
        plt.ylabel("R2")
        plt.title("GA")
        plt.legend()
        plt.show()



def ga_optimize_svr(train_data, train_label, test_data, test_label,optimizationdic={}):


    bound = np.array([[optimizationdic['c_low'],  optimizationdic['g_low']], [optimizationdic['c_high'], optimizationdic['g_high'] ]])

    ga = GeneticAlgorithm(sizepop=optimizationdic['sizepop'], vardim=2, bound=bound, MAXGEN=optimizationdic['maxgen'], params=[optimizationdic['crossrate'], optimizationdic['mutationrate'],optimizationdic['alpha'] ],train_data=train_data, train_label=train_label, test_data=test_data, test_label=test_label)
    svrmodel=ga.solve()
    return svrmodel
