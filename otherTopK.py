import networkx as nx
from operator import itemgetter


class otherTopK:
    def __init__(self,graphAdj,k):
        self.graphAdj = graphAdj
        self.k = k

    def findTopKSeeds(self):
        graph = nx.DiGraph(self.graphAdj)

        # Betweenes centrality
        BetCen = nx.betweenness_centrality(graph)
        BetCenSeed = sorted(BetCen.items(), key=itemgetter(1), reverse=True)[:self.k]
        BetCenSeed = list(map(lambda x: x[0], BetCenSeed))
        print("method 2/7 completed")


        # Closeness centrality
        ClosCen = nx.closeness_centrality(graph)
        ClosCenSeed = sorted(ClosCen.items(), key=itemgetter(1), reverse=True)[:self.k]
        ClosCenSeed = list(map(lambda x: x[0], ClosCenSeed))
        print("method 3/7 completed")

        # Eigenvector centrality
        EigenCen = nx.eigenvector_centrality(graph)
        EigenCenSeed = sorted(EigenCen.items(), key=itemgetter(1), reverse=True)[:self.k]
        EigenCenSeed = list(map(lambda x: x[0], EigenCenSeed))
        print("method 4/7 completed")

        # PageRank centrality
        PageRankCen = nx.pagerank(graph)
        PageRankCenSeed = sorted(PageRankCen.items(), key=itemgetter(1), reverse=True)[:self.k]
        PageRankCenSeed = list(map(lambda x: x[0], PageRankCenSeed))
        print("method 5/7 completed")


        return [BetCenSeed,ClosCenSeed,EigenCenSeed,PageRankCenSeed]

        # print
