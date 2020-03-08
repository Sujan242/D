
from collections import deque
G = []
def take_input(filename):
    global G 
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
    print(G)




def dobfs(s):
    prev = [0 for _ in range(len(G))]
    distance = [0 for _ in range(len(G))]
    color = ['white' for _ in range(len(G))]
    q = deque([])
    q.append(s)
    prev[s] = None
    distance[s]=0
    color[s]='white'
    while(len(q)!=0):
        s = q.popleft()
        for v in G[s]:
            if(color[v]=='white'):
                q.append(v)
                prev[v]=s
                distance[v]=distance[s]+1
                color[v]='grey'
        color[s]='black'
    return distance,prev,distance





    

    



take_input('input.txt')
print(dobfs(0))