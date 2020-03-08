
	

import queue as q
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque([])

    def Is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


class BFS:
    def __init__(self):
        self.edges = []
        self.v = 0
        self.G = []
        self.color = []
        self.prev = []
        self.distance = []
        self.queue = Queue()
        self.s = 0

    # def take_input(self):
    #     self.v = int(input("enter the number of vertices \n"))
    #     self.s = int(input("enter the source vertex"))
    #     print("if you want to stop giving the input the press control+c")
    #     try:
    #         while True:
    #             (m, n) = [int(x)
    #                       for x in input("enter the edges \n").split(' ')]
    #             x = (m, n)
    #             self.edges.append(x)
    #     except:
    #         self.lists = [[]*1 for _ in range(self.v)]
    #         self.prev = [[]*1 for _ in range(self.v)]
    #         self.color = [['white']*1 for _ in range(self.v)]
    #         self.distance = [[]*1 for _ in range(self.v)]
    #         for x in self.edges:
    #             self.lists[x[0]].append(x[1])
    #             self.lists[x[1]].append(x[0])
    #         print(self.lists)
    #         return self.v,self.s
    def take_input(self,filename):
        file = open(filename,'r')
        for line in file:
            line = line.strip()
            first = True
            adjacentvertices = []
            for node in line.split(' '):
                if first:
                    first= False
                    continue
                adjacentvertices.append(int(node))
            self.G.append(adjacentvertices)
        print(self.G)

    def do_bfs(self, s):
        self.v = len(self.G)
        self.prev = [0 for _ in range(self.v)]
        self.color = ['white' for _ in range(self.v)]
        self.distance = [0 for _ in range(self.v)]
        self.queue.enqueue(s)
        self.prev[s] = None
        self.color[s] = 'grey'
        self.distance[s] = 0
        while(not (self.queue.Is_empty())):
            m = self.queue.dequeue()
            for u in self.G[m]:
                if(self.color[u] == 'white'):
                    print(u)
                    self.queue.enqueue(u)
                    self.distance[u] = self.distance[m]+1
                    self.color[u] = 'grey'
                    self.prev[u] = m
            self.color[m] = 'black'
        print(self.distance)
        print(self.color)
        return self.color


q = Queue()
q.enqueue(0)
x = BFS()
x.take_input('input.txt')
color = x.do_bfs(0)
for i in range(1,len(color)):
    if(color[i][0]=='white'):
        color = x.do_bfs(i)
