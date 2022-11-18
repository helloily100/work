"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import numpy
import copy
import ArrayList
import ArrayStack
import SLLQueue


class AdjacencyMatrix(object):
    def __init__(self, n):
        self.n = n
        self.a = np.zeros([n, n], np.bool_)

    def add_edge(self, i, j):
        self.a[i][j] = True

    def remove_edge(self, i, j):
        self.a[i][j] = False

    def has_edge(self, i, j):
        return self.a[i][j]

    def out_edges(self, i):
        l = ArrayList.ArrayList()
        for j in range(self.n - 1):
            if self.has_edge(i, j):
                l.append(j)
        return l

    def in_edges(self, j):
        l = ArrayList.ArrayList()
        for i in range(self.n - 1):
            if self.has_edge(i, j):
                l.append(i)
        return l

    def in_degree(self, i):
        deg = 0
        for j in range(self.n - 1):
            if self.a[i][j]:
                deg = deg + 1
        return deg

    def out_degree(self, i):
        deg = 0
        for j in range(self.n - 1):
            if self.a[i][j]:
                deg = deg + 1
        return deg

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

    def size(self) -> int:
        return self.n

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            for j in range(0, self.n):
                if self.has_edge(i, j):
                    s += f"{i, j}"
        return s


'''
g = AdjacencyMatrix(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(1, 4)
g.add_edge(4, 5)

print(g.dfs(1))
'''


