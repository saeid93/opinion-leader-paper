from reader import reader
from topKFinder import topKFinder

def main():
    numOfNodes = 6541
    # if index is from 1
    numOfNodes = numOfNodes + 1
    seedSize = 100
    read = reader('Datasets/advogato.txt', numOfNodes)
    data = read.reader()

    topK = topKFinder(data,seedSize,numOfNodes)
    topK.topKAlg()


if __name__== '__main__':
    main()