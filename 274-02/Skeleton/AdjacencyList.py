"""An implementation of the adjacency list representation of a graph"""
import numpy
import DLList
import SLLQueue
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack
import ArrayQueue


class AdjacencyList(Graph):
    def __init__(self, n: int):
        self.n = n
        self.adj = np.zeros(n, object)
        for i in range(self.n):
            self.adj[i] = ArrayList.ArrayList()

    def add_edge(self, i: int, j: int):
        self.adj[i].append(j)

    def remove_edge(self, i: int, j: int):
        for k in range(len(self.adj[i]) - 1):
            if self.adj[i].get(k) == j:
                self.adj[i].remove(k)
                return

    def has_edge(self, i: int, j: int) -> bool:
        for k in range(self.adj[i]):
            if k == j:
                return True
        return False

    def out_edges(self, i) -> List:
        return self.adj[i]

    def in_edges(self, i) -> List:
        out = ArrayStack.ArrayStack()
        for j in range(self.n - 1):
            if self.has_edge(j, i):
                out.push(j)
        return out

    def new_boolean_array(self, n):
        return numpy.zeros(n, numpy.bool_)

    def bfs(self, r: int):
        seen = self.new_boolean_array(self.n)
        q = SLLQueue.SLLQueue()
        q.add(r)
        seen[r] = True
        while q.size() > 0:
            i = q.remove()
            for j in self.out_edges(i):
                if seen[j] == False:
                    q.add(j)
                    seen[j] = True

    def dfs(self, r: int):
        c = self.new_boolean_array(self.n)
        s = ArrayStack.ArrayStack()
        s.push(r)
        c[r] = True
        while s.size() > 0:
            i = s.pop()
            print(i)
            for j in self.out_edges(i):
                if not c[j]:
                    c[j] = True
                    s.push(j)

    def distance(self, r: int, dest: int):
        c = self.new_boolean_array(self.n)
        p = numpy.zeros(self.n)
        s = ArrayStack.ArrayStack()
        s.push(r)
        p[r] = 0
        while s.size() > 0:
            i = s.pop()
            if c[i] == False:
                c[i] = True
                neighbors = self.out_edges(i)
                for j in neighbors:
                    if c[j] == False:
                        s.push(j)
                        p[j] = p[i] + 1
                        if j == dest:
                            return p[j]


    def size(self) -> int:
        return self.n

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s


'''
g = AdjacencyList(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(1, 4)
g.add_edge(4, 5)

g.dfs(0)
'''
