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
        print(self.inNeighbors[5])

    def initialVals(self):



    def topKAlg(self):
        self.findingNeighbors()
        self.initialVals()