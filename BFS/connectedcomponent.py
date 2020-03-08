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
        self.lists = []
        self.color = []
        self.prev = []
        self.distance = []
        self.queue = Queue()
        self.s = 0

    def take_input(self):
        self.v = int(input("enter the number of vertices \n"))
        print("if you want to stop giving the input the press control+c")
        try:
            while True:
                (m, n) = [int(x)
                          for x in input("enter the edges \n").split(' ')]
                x = (m, n)
                self.edges.append(x)
        except:
            self.lists = [[]*1 for _ in range(self.v)]
            self.prev = [[]*1 for _ in range(self.v)]
            self.color = [['white']*1 for _ in range(self.v)]
            self.distance = [[]*1 for _ in range(self.v)]
            for x in self.edges:
                self.lists[x[0]].append(x[1])
                self.lists[x[1]].append(x[0])
            print(self.lists)
            return self.v
    def do_bfs(self, s):
        print(s,end =" ")
        self.queue.enqueue(s)
        self.prev[s] = None
        self.color[s] = 'grey'
        self.distance[s] = 0
        while(not (self.queue.Is_empty())):
            m = self.queue.dequeue()
            for u in self.lists[m]:
                if(self.color[u][0] == 'white'):
                    print(u,end =" ")
                    self.queue.enqueue(u)
                    self.distance[u] = self.distance[m]+1
                    self.color[u] = 'grey'
                    self.prev[u] = m
            self.color[m] = 'black'
        return self.color


x = BFS()
n = x.take_input()
color = x.color
count = 0
for i in range(0,n):
    if(color[i][0]=='white'):
        count += 1
        print("component"+str(count)+ " :", end=" ")
        color = x.do_bfs(i)
