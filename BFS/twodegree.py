from collections import deque

Graph = [] 

def takeinput(filepath):
    global Graph
    global visited
    global uarr
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
        

    print(Graph)

twodegree = [0 for _ in range(len(Graph))]
def dfs(s):
    global visited
    global twodegree
    visited[s] = 1

    for v in Graph[s]:
        twodegree[s]=twodegree[s]+len(Graph[v])
    for  v in Graph[s]:
        if(not visited[v]):
            dfs(v)
    

xarr = [7,6,4,3,0,1,5,9,12,11,8] 
def xarray(s):
    m = xarr[s]
    visited[s] = 1
    for v in Graph[s]:
        if(not visited[v]):
            m = (max(xarray(v),m))
            uarr[s] = m
    return m
m = 0

parr = [2,3,6,1,4,5] 
uarr= [2,3,6,1,4,5]
def price_pro(s):
    visited[s]= 1
    m = parr[s]
    for v in Graph[s]:
        m = min(price_pro(v),m)
        uarr[s]=m
    return m
        




d = deque([])

def simple(s,x):
    visited[s] = 1
    d.append(s)
    for v in Graph[s]:
        if(v==x):
            d.append(x)
            print(d)
            d.pop()
        if(not visited[v]):
            simple(v,x)
            d.pop()


# def simple2(s):
#     visited[s] = 1
#     for v in Graph[s]:
#         if(not visited[v]):
#             simple2(s)
#         else:
            

takeinput('input.txt')
# for i in range(len(Graph)):
#     if(visited[i]==0):
#         print(i)
#         price_pro(i) 
# print(uarr)
simple(4,5)