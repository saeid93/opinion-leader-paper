import numpy as np

class topKFinder:
    def __init__(self,graph,k,numOfNodes,alpha):
        self.graph = graph
        self.k = k
        self.numOfNodes = numOfNodes
        self.inNeighbors = {}
        self.indegree = []
        self.outdegree = []
        self.alpha = alpha

    def findingNeighbors(self):
        for i in range(0,self.numOfNodes):
            self.inNeighbors[i] = np.nonzero(self.graph[:,i])[0]



    # computing indegree and outdegrees
    def initialVals(self):
        self.outdegree = [np.sum(row) for row in self.graph]
        self.indegree = [np.sum(row) for row in np.transpose(self.graph)]




    def topKAlg(self):
        self.findingNeighbors()
        self.initialVals()

        # initializing the influ0, influ at t, influ at t-1
        influ0 = np.array(self.outdegree) - np.array(self.indegree)
        influT = np.zeros(self.numOfNodes)
        influTM1 = influ0

        # indicator array of the number of present at each iteration
        presentNodes = np.array(list(range(0,self.numOfNodes)))
        t = 0
        while np.shape(presentNodes)[0]>self.k:
            t+=1
            for node in presentNodes:
                neighbors = self.inNeighbors[node]
                sumOfInN = 0
                for neighbor in neighbors:
                    sumOfInN += self.graph[neighbor,node]*influTM1[neighbor]

                # influence update function
                influT[node] = self.alpha * influ0[node] + (1 - self.alpha) * sumOfInN

                # find kth largest max, influ max, influ min at each iteration
                kthInfluMax = influT[np.argsort(influT)[-self.k]]
                influMax = influT.max()
                influMin = influT.min()


            # presentNodes1 = presentNodes
            # print(np.shape(presentNodes))
            presentNodes =  presentNodes[(kthInfluMax - influT[presentNodes]) <= ((2 * (1-self.alpha)**t) * (influMax - influMin))]
            influTM1 = influT

        return presentNodes