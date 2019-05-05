
import numpy as np
from scipy import sparse


class reader:
    def __init__(self, datasetName, numOfNodes):
        self.datasetName = datasetName
        self.numOfNodes = numOfNodes

    # reading from the file
    def reader(self):
        with open(self.datasetName) as f:
            data = f.read()
        return self.toScipy(data)

    # converting to scipy matrix
    def toScipy(self,data):
        data = data.split("\n")
        data.pop()
        data = list(map(lambda x:x.split(),data))
        data = np.array(data,dtype=float)
        fromCol = data[:,0].astype(int)
        toCol = data[:, 1].astype(int)
        weightCol = data[:, 2]
        data = sparse.csr_matrix((weightCol, (fromCol, toCol)), (self.numOfNodes,self.numOfNodes))
        return data
    # def toAdjMatrix(self):








