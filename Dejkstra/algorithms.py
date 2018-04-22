import sys, os
sys.path.append(os.path.abspath('../'))
from el_core.SingleTon import SingleTon

@SingleTon
class Dijkstra:
    """
    Dijkstra's algorithm (English Dijkstra's algorithm) is an 
    algorithm on graphs, invented by the Dutch scientist Edsger 
    Dijkstra in 1959. Finds the shortest paths from one of 
    the vertices of the graph to all the others. The algorithm 
    works only for graphs without edges of negative weight. 
    The algorithm is widely used in programming and technology, 
    for example, it uses the routing protocols OSPF and IS-IS.
    """
    def __init__(self):
        """
        Crate a object of Dijkstra algorithm, use pattern Singleton. 
        From this initialisation, create a local variable
        """
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

    @property
    def algorithm(self):
        """
        This method returns data after entering them into the class, 
        and executing the algorithm
        """
        for v in range(self.n):
            if self.dist[v] == self.INF:
                self.data.append(-1)
            else:
                self.data.append(self.dist[v])

        for v in range(self.n):
            self.latest = v + 1
            self.back[v + 1] = []
            if self.dist[v] != self.INF:
                self.__printway(v)
        returns = {'bytes': self.data, 'path': self.back}
        self.__unset()
        return returns

    @algorithm.setter
    def algorithm(self, data):
        """
        This method set the data to created variables and
        start Dijkstra algorithm from search path
        """
        n = data['n']
        m = data['m']
        start = data['start']
        array = data['array']
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
        """
        This a private base algorithm method from
        search path
        """
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
        """
        Private method, search path from data
        """
        if v == -1:
            return 
        self.__printway(self.pred[v])
        self.back[self.latest].append(v + 1)

    def __unset(self):
        """
        Unset baset variable
        """
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


# A*


class SquareGrid:
    """
    This class is responsible for the data grid for the 
    algorithm and the old one
    """
    def __init__(self, width, height):
        """
        Creates local variables that will be used in the 
        process of running the algorithm
        """
        self.width = width
        self.height = height
        self.walls = []
    
    def in_bounds(self, id):
        """
        The method checks if data is within the specified 
        limits
        """
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height
    
    def passable(self, id):
        """
        Checks whether the given data is in a grid of walls
        """
        return id not in self.walls
    
    def neighbors(self, id):
        """
        This method looks for the nearest neighbors of the 
        given data
        """
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)


class GridWithWeights(SquareGrid):
    """
    This class is responsible for the weight of the grid 
    and its elements
    """
    def __init__(self, width, height):
        """
        Initializes the creation, appeals to the parent 
        class to create the necessary variables and 
        creates its own
        """
        super().__init__(width, height)
        self.weights = {}
    
    def cost(self, from_node, to_node):
        """
        Returns the amount by the given data from the grid
        """
        return self.weights.get(to_node, 1)

class PriorityQueue:
    """
    This class is responsible for the priority queue
    """
    def __init__(self):
        """
        The method initializes the queue
        """
        self.elements = []
    
    def empty(self):
        """
        The method checks whether the queue is empty
        """
        return len(self.elements) == 0
    
    def put(self, item, priority):
        """
        The method enters the data in the queue
        """
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        """
        The method extracts data from the queue
        """
        return heapq.heappop(self.elements)[1]


class Astar(object):
    """
    Search A * (pronounced "A star" or "A star", 
    from English A star) - in computer science and 
    mathematics, the search algorithm for the 
    first best match on the graph that finds the 
    route with the lowest cost from one vertex 
    (initial) to the other (target, final).
    """
    @staticmethod
    def Search(graph, start, goal):
        """
        The method initializes the search and returns the data
        came from and cost so far.
        Input data the: graph - GridWithWeights()
        start - typle() (start point)
        goal - typle() (end point)
        """
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0
        
        while not frontier.empty():
            current = frontier.get()
            if current == goal:
                break
            for next in graph.neighbors(current):
                new_cost = cost_so_far[current] + graph.cost(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + heuristic(goal, next)
                    frontier.put(next, priority)
                    came_from[next] = current
        
        return came_from, cost_so_far

class Draw(object):
    """
    The class is responsible for returning the data 
    in the appropriate format, numeric (amount when 
    passing each path) and the arrow, how to go better
    """
    def tile(graph, id, style, width):
        """
        This method is responsible for determining 
        the tile at this point
        """
        r = "."
        if 'number' in style and id in style['number']: r = "%d" % style['number'][id]
        if 'point_to' in style and style['point_to'].get(id, None) is not None:
            (x1, y1) = id
            (x2, y2) = style['point_to'][id]
            if x2 == x1 + 1: r = "→"
            if x2 == x1 - 1: r = "←"
            if y2 == y1 + 1: r = "↓"
            if y2 == y1 - 1: r = "↑"
        if 'start' in style and id == style['start']: r = "A"
        if 'goal' in style and id == style['goal']: r = "Z"
        if 'path' in style and id in style['path']: r = "@"
        if id in graph.walls: r = "#" * width
        return r

    def draw_grid(graph, width=2, **style):
        array = []
        for y in range(graph.height):
            tarray = []
            for x in range(graph.width):
                tarray.append("{}{}".format(' ' * width, self.draw_tile(graph, (x, y), style, width)))
            array.append(tarray)
        return array