
from reader import reader
from topKFinder import topKFinder
from otherTopK import otherTopK
from opinionFormationModel import opinionFromationModel
from IMMethods import IMMethods
import numpy as np
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
    # seedSize = 100
    seedSize = 1
    # dataset data
    numOfNodes = 6541
    # numOfNodes = 4
    numOfNodes = numOfNodes + 1 # if index is from 1
    dataset = "advogato"
    # dataset = 'test'
    read = reader("Datasets/" + dataset + ".txt", numOfNodes)
    data = read.reader()
    # ----------top-k nodes finder----------

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

        # influence maximization based methods
        IM = IMMethods(dataset, seedSize)
        IM.runIM()


    # ----------compute opinion formation modes trends----------

    elif option == 2:


        def opinionFromation(method,seed):
            opForm = opinionFromationModel(data, seed)
            trendDegroot = opForm.degroot()
            write2file("trends/" + dataset + "/degroot/" + method + ".csv", trendDegroot)
            print("Degroot of " + method + " is done")
            trendProposedModel = opForm.proposedModel()
            write2file("trends/" + dataset + "/proposedModel/" + method + ".csv", trendProposedModel)
            print("Proposed Opinion formation of " + method + " is done")
            trendAddMethod = opForm.addMethod()
            write2file("trends/" + dataset + "/addMethod/" + method + ".csv", trendAddMethod)
            print("Added Opinion formation of " + method + " is done")

        # read previously computed seeds from the hdd
        PropSeed = np.loadtxt("topKNodes/" + dataset + "/proposedMethod.csv",dtype=int)
        BetCenSeed = np.loadtxt("topKNodes/" + dataset + "/betweeness.csv",dtype=int)
        ClosCenSeed = np.loadtxt("topKNodes/" + dataset + "/closeness.csv",dtype=int)
        EigenCenSeed = np.loadtxt("topKNodes/" + dataset + "/eigenvector.csv",dtype=int)
        PageRankCenSeed = np.loadtxt("topKNodes/" + dataset + "/pagerank.csv",dtype=int)
        StaticGreedySeed = np.loadtxt("topKNodes/" + dataset + "/StaticGreedy.csv",dtype=int)
        IMRankSeed = np.loadtxt("topKNodes/" + dataset + "/IMRank.csv",dtype=int)


        opinionFromation("proposedMethod",PropSeed)
        opinionFromation("betweeness", BetCenSeed)
        opinionFromation("closeness", ClosCenSeed)
        opinionFromation("eigenvector", EigenCenSeed)
        opinionFromation("pagerank", PageRankCenSeed)
        opinionFromation("StaticGreedy", StaticGreedySeed)
        opinionFromation("IMRank", IMRankSeed)


    # program runtime estimation
    end = time.time()
    print((end - start)/60)

if __name__== '__main__':
    main()