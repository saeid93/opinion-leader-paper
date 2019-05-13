
from reader import reader
from topKFinder import topKFinder
from otherTopK import otherTopK
import time

def write2file(file,seed):
    f= open(file,"w+")
    for item in seed:
         f.write(str(item) + "\n")
    f.close()


def main():
    start = time.time()
    option = int(input("Enter the right option:\n1. Find top users\n2.Opinion formation test\n"))
    # algorithm parameters
    alpha = 0.5
    seedSize = 100
    # dataset data
    numOfNodes = 6541
    numOfNodes = numOfNodes + 1 # if index is from 1
    dataset = "advogato"
    read = reader("Datasets/" + dataset + ".txt", numOfNodes)
    data = read.reader()

    # top-k nodes finder
    if option == 1:
        # proposed method
        topK = topKFinder(data,seedSize,numOfNodes,alpha)
        topKNodes = topK.topKAlg()
        write2file("topKNodes/" + dataset + "/proposedMethod.csv",topKNodes)
        # centrality-based methods
        oTopK = otherTopK(data, seedSize)
        [BetCenSeed,ClosCenSeed,EigenCenSeed,PageRankCenSeed] = oTopK.findTopKSeeds()
        write2file("topKNodes/" + dataset + "/betweeness.csv", BetCenSeed)
        write2file("topKNodes/" + dataset + "/closeness.csv", ClosCenSeed)
        write2file("topKNodes/" + dataset + "/eigenvector.csv", EigenCenSeed)
        write2file("topKNodes/" + dataset + "/pagerank.csv", PageRankCenSeed)
    # print(topKNodes)
    elif option == 2:
        print("option2")
    end = time.time()
    print((end - start)/60)

if __name__== '__main__':
    main()