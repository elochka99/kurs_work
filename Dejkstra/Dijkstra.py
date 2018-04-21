class Dijkstra:
    """docstring for Dijkstra"""
    def __init__(self):
        self.INF = 2147483647 / 2
        self.n = 0
        self.m = 0
        self.start = 0
        self.adj = []
        self.weight = []
        self.used = []
        self.dist = []
        self.pred = []

        self.latest = 0
        self.back = {}
        self.data = []

    # array -> [[u, v, value]]
    def readdata(self, n, m, start, array):
        self.latest = 0
        self.back = {}
        self.data = []
        self.n = n
        self.m = m
        self.start = start - 1
        for i in range(n):
            self.adj.append([])
            self.weight.append([])
        self.used = [False] * n
        self.pred = [-1] * n
        self.dist = [self.INF] * n
            
        for i in range(m):
            u = int(array[i][0]) - 1
            v = int(array[i][1]) - 1
            w = float(array[i][2])
            self.adj[u].append(v)
            self.weight[u].append(w)
        self.__algo()

    def __algo(self):
        self.dist[self.start] = 0
        for k in range(self.n):
            v = -1
            distV = self.INF
            for i in range(self.n):
                if self.used[i] is False and distV > self.dist[i]:
                    v = i
                    distV = self.dist[i]
            for i in range(len(self.adj[v])):
                u = self.adj[v][i]
                weightU = self.weight[v][i]
                if self.dist[v] + weightU < self.dist[u]:
                    self.dist[u] = self.dist[v] + weightU
                    self.pred[u] = v
            self.used[v] = True

    def __printway(self, v):
        if v == -1:
            return 
        self.__printway(self.pred[v])
        self.back[self.latest].append(v + 1)
        #print(v + 1, end=" ")

    def printdata(self):
        for v in range(self.n):
            if self.dist[v] == self.INF:
                self.data.append(-1)
                #print("-1", end=" ")
            else:
                self.data.append(self.dist[v])
                #print(self.dist[v], end=" ")
        #print()
        for v in range(self.n):
            self.latest = v + 1
            self.back[v + 1] = []
            #print("%d: " % (v + 1), end=" ")
            if self.dist[v] != self.INF:
                self.__printway(v)
            #print()
        return {'bytes': self.data, 'path': self.back}

#Dijkstra = Dijkstra()
"""Dijkstra.readdata(7, 11, 1, [
        [1, 2, 1],
        [1, 3, 7],
        [2, 4, 4],
        [2, 5, 2],
        [3, 2, 4],
        [3, 5, 5],
        [4, 5, 3],
        [5, 3, 3],
        [5, 4, 10],
        [6, 7, 3],
        [7, 6, 4]
])"""
#Dijkstra.readdata(2, 2, 1, [[1, 2, 3], [2,1,3]])
#print(Dijkstra.printdata())
#Dijkstras = Dijkstra()
