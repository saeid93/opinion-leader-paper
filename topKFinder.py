import numpy as np


class topKFinder:
    def __init__(self,graph,k,numOfNodes):
        self.graph = graph
        self.k = k
        self.numOfNodes = numOfNodes
        self.inNeighbors = {}
        self.indegree = []
        self.outdegree = []

    def findingNeighbors(self):
        for i in range(0,self.numOfNodes):
            self.inNeighbors[i] = np.nonzero(self.graph[:,i])[0]


    def initialVals(self):
        self.indegree = [np.sum(row) for row in self.graph]
        self.outdegree = [np.sum(row) for row in np.transpose(self.graph)]
        print(self.indegree)
        print(self.outdegree)




    def topKAlg(self):
        self.findingNeighbors()
        self.initialVals()