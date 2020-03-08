

class DFS:
    def __init__(self):
        self.v = 6
        self.visited = []
        self.prev = []
        self.s = 0
        self.time=0
        self.start=[]
        self.finish=[]
        self.G= []
        self.sst = 0
        self.flag=0

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
        self.visited = [ 0 for _ in range(self.v)]
        self.start = [ 0 for _ in range(self.v)]
        self.finish = [ 0 for _ in range(self.v)]
        self.distance = [[]*1 for _ in range(self.v)]
        return self.v,self.s

    def do_dfs(self, u):
        self.visited[u]=1
        self.start[u]=self.time
        self.time = self.time+1
        self.sst = self.start[u] 
        for v in self.G[u]:
            if(self.visited[v]!=1):
                self.prev[v] = u
                self.sst = min(self.do_dfs(v),self.sst)
                print(self.sst)
            elif(v!=self.prev[u]):
                self.sst = min(self.start[v],self.sst)
                print(self.sst)

        self.finish[u] = self.time
        self.time = self.time+1
        if(self.sst==self.start[u] and self.start[u]!=0):
            print(self.prev[u],u)
        x =self.sst
        return x

    def check_cyclic_edge(self,u,x,y):
        self.visited[u]=1
        self.start[u]=self.time
        self.time = self.time+1
        for v in self.G[u]:
            if(self.visited[v]!=1):
                self.prev[v] = u
                self.check_cyclic_edge(v,x,y)   
            elif(v!=self.prev[u]):
                if(v==x and u==y or u==x and v==y):
                    print("that is part of cycle")
                elif(self.start[x]<self.start[u] and self.start[y]>self.start[v]):
                    print("that is the part of the cycle")
                print("back edge found",v,u)
        self.finish[u] = self.time
        self.time = self.time+1



x = DFS()
x.take_input()
x.do_dfs(0)




                # self.sst = min(self.start[v],self.sst)
                # if(self.sst<=int(self.start[x]) and \
                #     self.sst<=int(self.start[y]) and \
                #     self.start[u]>=int(self.start[x]) and \
                #     self.start[u]>=int(self.start[y]) and\
                #     int(self.finish[v])>=int(self.finish[x]) and \
                #     int(self.finish[v])>=int(self.finish[y]) and \
                #     int(self.finish[u])<=int(self.finish[x] )and \
                #     int(self.finish[u])<=int(self.finish[y])):
                #         self.flag = 1