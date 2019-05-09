from reader import reader
from topKFinder import topKFinder

def main():
    alpha = 0.2
    numOfNodes = 6541
    # if index is from 1
    numOfNodes = numOfNodes + 1
    seedSize = 100
    read = reader('Datasets/advogato.txt', numOfNodes)
    data = read.reader()

    topK = topKFinder(data,seedSize,numOfNodes,alpha)
    topK.topKAlg()


if __name__== '__main__':
    main()