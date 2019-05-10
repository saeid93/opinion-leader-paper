import networkx as nx


class otherTopK:
    def __init__(self,graphAdj,k):
        self.graphAdj = graphAdj
        self.k = k

    def findTopKSeeds(self):
        # print(self.graphAdj)
        graph = nx.DiGraph(self.graphAdj)
        print(len(graph.edges.data()))
            # print

        # print
