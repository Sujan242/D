
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


class DFS:
    def __init__(self):
        self.edges = []
        self.v = 6
        self.lists = []
        self.visited = []
        self.prev = []
        self.distance = []
        self.queue = Queue()
        self.s = 0
        self.time=0
        self.start=[]
        self.finish=[]
        self.G= []

    def take_input(self):
        file=open('input.txt','r')
        for line in file:
            line=line.strip()
            adjacentVertices = []
            first=True
            for node in line.split(' '):
                if first:
                    first=False
                    continue
                adjacentVertices.append(int(node))
            self.G.append(adjacentVertices)
        file.close()
        print(self.G)
        self.s = int(input("enter the source vertex \n"))
        self.lists = [[]*1 for _ in range(self.v)]
        self.prev = [[]*1 for _ in range(self.v)]
        self.visited = [[0]*1 for _ in range(self.v)]
        self.start = [[0]*1 for _ in range(self.v)]
        self.finish = [[0]*1 for _ in range(self.v)]
        self.distance = [[]*1 for _ in range(self.v)]
        return self.v,self.s

    def do_dfs(self, u):
        self.visited[u]=1
        self.start[u]=self.time
        self.time = self.time+1
        for v in self.G[u]:
            if(self.visited[v]!=1):
                self.prev[v] = u
                print("tree edge : ",u,v)
                self.do_dfs(v)
            else:
                if(self.start[u]<self.start[v]):
                    print("backedge", u,v)
        self.finish[u] = self.time
        self.time = self.time+1




x = DFS()
n,s = x.take_input()
x.do_dfs(s)
print("start time ",x.start)
print("end time ",x.finish)

# for i in range(0,n):
#     if(x.visited[i]==0):
#         x.do_dfs(i)
