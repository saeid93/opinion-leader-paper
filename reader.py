import numpy as np
from scipy import sparse


def read(datasetName, numOfNodes):
    with open(datasetName) as f:
            data = f.read()
    
    data = data.split("\n")
    data.pop()
    data = list(map(lambda x:x.split(),data))
    data = np.array(data,dtype=float)
    fromCol = data[:,0].astype(int)
    toCol = data[:, 1].astype(int)
    weightCol = data[:, 2]
    data = sparse.csr_matrix((weightCol, (fromCol, toCol)), (numOfNodes, numOfNodes))
    return data
