



from collections import deque
G = []
visited = []
def take_input(filename):
    global G 
    global visited
    global pre
    global found
    global result
    global dist
    global m,n,mind,time
    global start 
    global finish
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
        G.append(adjacentvertices)
    visited = [0 for _ in range(len(G))]
    pre = [0 for _ in range(len(G))]
    dist = [0 for _ in range(len(G))]
    start = [0 for _ in range(len(G))]
    finish = [0 for _ in range(len(G))]
    found = 0
    result = []
    m = 0
    n = 0
    mind = 29999999
    time =0







def dfs(s,x,y):
    global found
    global m
    global n
    global mind
    global time
    visited[s] = 1
    start[s]= time
    time =time+1
    for  v in G[s]:
        if((s==x and v==y)or(s==y and v==x)):
            found =1
        if(not visited[v]):
            pre[v] = s
            dist[v] = dist[s]+1
            temp,m,n = dfs(v,x,y)
            mind= min(temp,mind)
        elif(found and v!=pre[s]):
            x = min(abs(dist[s]-dist[v]),mind)
            if(x!=mind):
                m=s
                n=v
            mind = x
    finish[s] = time
    time = time+1
    print(mind,m,n)
    return mind,m,n



take_input('input.txt')
_,x,y = dfs(0,3,4)
print(pre)
print(x,y)
out =  x
print(y)
for i in range(x-y):
    print(out)
    out = pre[out]
print(out)


    