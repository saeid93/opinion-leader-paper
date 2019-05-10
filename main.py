
from reader import reader
from topKFinder import topKFinder
from otherTopK import otherTopK

def main():
    alpha = 0.5
    numOfNodes = 6541
    # if index is from 1
    numOfNodes = numOfNodes + 1
    seedSize = 100
    read = reader('Datasets/advogato.txt', numOfNodes)
    data = read.reader()
    # topK = topKFinder(data,seedSize,numOfNodes,alpha)
    # topKNodes = topK.topKAlg()
    # print(topKNodes)

    oTopK = otherTopK(data,seedSize)
    oTopK.findTopKSeeds()

if __name__== '__main__':
    main()