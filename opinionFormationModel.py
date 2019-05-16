

import numpy as np

class opinionFromationModel:
    def __init__(self,graph,seed):
        self.graph = graph.todense()
        self.seed = seed


    def makeDegrootTruthMatrix(self):
        # find indegrees and outdergrees
        self.outdegree = [np.sum(row) for row in self.graph]
        self.indegree = [np.sum(row) for row in np.transpose(self.graph)]
        # find difference of these two
        self.differnece = np.array(self.outdegree) - np.array(self.indegree)
        # to make them all positive
        self.centrality = self.differnece - np.min(self.differnece)
        # templeate of the truth matrix
        self.DegrootTruth = np.zeros(np.shape(self.graph))
        # populate truth matrix with centralities
        numOfNodes = np.shape(self.graph)[0]
        for i in range(0,numOfNodes):
            for j in range(0,numOfNodes):
                if self.graph[i,j] != 0:
                    self.DegrootTruth[i,j] = self.centrality[i]

        self.DegrootTruth = (np.divide(self.DegrootTruth.T,self.DegrootTruth.sum(axis=1))).T
        self.DegrootTruth[np.isnan(self.DegrootTruth)] = 0



    def setSeed(self,seed):
        self.seed = seed

    def degroot(self):
        self.makeDegrootTruthMatrix()
        opinions = np.zeros(np.shape(self.graph)[0])
        opinions[self.seed] = 1
        epsilon = 0.1
        trend = [0,0.1]

        while np.abs(trend[len(trend) - 1] - trend[len(trend) - 2]) >= epsilon:
            opinions = np.matmul(self.DegrootTruth,opinions)
            trend = trend + [np.sum(opinions)]
        return trend
        # print("degroot")

    def proposedModel(self):
        print("proposed")

    def addMethod(self):
        print("added method")