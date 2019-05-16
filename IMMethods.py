
import subprocess as sb

class IMMethods:

    def __init__(self,dataset,k):
        self.dataset = dataset
        self.k = k

    def runIM(self):

        # static greedy
        R = 100
        sb.run("./StaticGreedy Datasets/" + self.dataset + "-IMReady.txt " + str(R) + " " + str(self.k) + " bsg",shell=True)
        sb.run("tail -n+5 BasicStaticGreedy_R" + str(R) + "_k" + str(self.k) + ".txt > topKNodes/" + self.dataset + "/StaticGreedy.csv",shell=True)
        sb.run("rm BasicStaticGreedy_R" + str(R) + "_k" + str(self.k) + ".txt" , shell=True)

        # IMRank
        L = 1
        iters = 10
        sb.run("./IMrank Datasets/" + self.dataset + "-IMReady.txt " + str(self.k) + " "+ str(L) +" "+ str(iters) + " PageRank" , shell=True)
        sb.run("tail -n+5 IMRank_k" + str(self.k) + "_l" + str(L) + "_LOOP" + str(iters) + "_irPageRank.txt > topKNodes/" + self.dataset + "/IMRank.csv" , shell=True)
        sb.run("rm IMRank_k" + str(self.k) + "_l" + str(L) + "_LOOP" + str(iters) + "_irPageRank.txt",shell=True)

IM = IMMethods("advogato",100)

IM.runIM()