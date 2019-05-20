

import numpy as np
import networkx as nx
import ndlib.models.ModelConfig as mc
import ndlib.models.opinions.AlgorithmicBiasModel as ab



class opinionFromationModel:
    def __init__(self,graph,seed):
        self.graph = graph.todense()
        self.seed = seed



    def calculateDiffernceCen(self):
        # find indegrees and outdegrees
        self.outdegree = [np.sum(row) for row in self.graph]
        self.indegree = [np.sum(row) for row in np.transpose(self.graph)]
        # find difference of these two
        self.differnece = np.array(self.outdegree) - np.array(self.indegree)

    def makeDegrootTruthMatrix(self):
        # find indegrees and outdegrees
        self.calculateDiffernceCen()
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

    def findingNeighbors(self):
        inNeighbors = {}
        numOfNodes = np.shape(self.graph)[0]
        for i in range(0,numOfNodes):
            inNeighbors[i] = np.nonzero(self.graph[:,i])[0]
        return inNeighbors

    def makeProposedTruthMatrix(self):
        # find indegrees and outdegrees
        self.calculateDiffernceCen()
        # to make them all positive
        centrality = self.differnece - np.min(self.differnece)
        # find in neighbors
        inNeighbors = self.findingNeighbors()
        # build D matrix
        D = np.zeros(np.shape(self.graph))
        numOfNodes = np.shape(self.graph)[0]
        for i in range(0,numOfNodes):
            sigma = np.sum(centrality[inNeighbors[i]])
            D[i,i] = centrality[i]/(sigma + centrality[i])
        W = np.zeros(np.shape(self.graph))
        for i in range(0, numOfNodes):
            sigma = np.sum(centrality[inNeighbors[i]])
            for j in range(0, numOfNodes):
                W[i,j] = centrality[j]/(sigma + centrality[i])

        D = (np.divide(D.T, D.sum(axis=1))).T
        D[np.isnan(D)] = 0

        W = (np.divide(W.T, W.sum(axis=1))).T
        W[np.isnan(W)] = 0

        return (W,D)




    def setSeed(self,seed):
        self.seed = seed

    # ------------- degroot model -------------
    def degroot(self):
        self.makeDegrootTruthMatrix()
        opinions = np.zeros(np.shape(self.graph)[0])
        opinions[self.seed] = 1
        epsilon = 0.1
        trend = [0,0.1]

        while np.abs(trend[len(trend) - 1] - trend[len(trend) - 2]) >= epsilon:
            opinions = np.matmul(self.DegrootTruth,opinions)
            trend.append(np.sum(opinions))
        trend.pop(0)
        trend.pop(0)
        return trend
        # print("degroot")


    # ------------- proposed model -------------
    def proposedModel(self):
        (W,D) = self.makeProposedTruthMatrix()
        opinions = np.zeros(np.shape(self.graph)[0])
        opinions0 = np.zeros(np.shape(self.graph)[0])
        opinions[self.seed] = 1
        opinions[self.seed] = 1
        epsilon = 0.1
        trend = [0,0.1]

        while np.abs(trend[len(trend) - 1] - trend[len(trend) - 2]) >= epsilon:
            opinions = np.matmul(W,opinions) + np.matmul(D,opinions0)
            trend.append(np.sum(opinions))
        trend.pop(0)
        trend.pop(0)
        return trend


    # ------------- added model -------------
    def addMethod(self):

        nxGraph = nx.DiGraph(self.graph)


        # Model selection
        model = ab.AlgorithmicBiasModel(nxGraph)

        # Model configuration
        config = mc.Configuration()
        config.add_model_parameter("epsilon", 0.32)
        config.add_model_parameter("gamma", 1)

        model.set_initial_status(config)

        for key in model.status:
            if key in self.seed:
                model.status[key] = 1
            else:
                model.status[key] = 0.001

        numOfIters = 100

        trendArr = []

        for i in range(0, numOfIters):
            iterations = model.iteration_bunch(1)
            trends = model.build_trends(iterations)
            di = model.status
            infectedTrend = np.sum(list(map(lambda x: di[x], di)))
            trendArr.append(infectedTrend)

        return trendArr

        print("added method")