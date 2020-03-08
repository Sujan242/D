from collections import deque
 

Graph = []
d = deque([])
start =[]
finish= []
visited = []


def takeinput(filepath):
    global Graph
    global d
    global visited
    global start 
    global finish 
    file = open(filepath,'r')
    for line  in file:
        line = line.strip()
        adjacentvertices = []
        first = True
        for node in line.split(" "):
            if first:
                first = False
                continue
            adjacentvertices.append(int(node))
        Graph.append(adjacentvertices)
        visited = [0 for _ in range(len(Graph))]
        start = [0 for _ in range(len(Graph))]
        finish = [0 for _ in range(len(Graph))]
        

    print(Graph)

def dfs(q):
    s = []
    s.append(q)
    time = 0
    while(len(d)!=0):
        start[s]= time
        time = time+1
        q = s[-1]
        s.pop()
        for v in Graph[s]:
            if((visited[v]==0)):
                print(v)
                d.append(v)
                start[v]=time
                time = time+1
        s = d.pop()
        finish[s]=time
        time=time+1


takeinput('/home/shashikanth/181IT242-20200131T200152Z-001/181IT242/DSALAB/input.txt')
dfs(0)
