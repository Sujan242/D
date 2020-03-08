import heapq

''' Adjacency List representation. G is a list of lists. '''
G = [] 

file=open('input.txt','r')
for line in file:
    line=line.strip()
    adjacentVertices = []
    first=True
    for edge in line.split(' '):
        if first:
            first=False
            continue
        node,weight = edge.split(',')
        adjacentVertices.append((int(node),int(weight)))
    G.append(adjacentVertices)
file.close()
print(G)

H1=[]
for i in range(len(G)):
    H1.append(i)

class vertex:
    def __init__(self):
        self.visited=0
        self.pred=None
        self.dist=1000
        self.path=""

def Dijkstra(G,s,H):
    global H1
    v=[]
    for i in range(len(G)):
        v.append(vertex())
    v[s].dist=0
    H[s][0]=0
    heapq.heapify(H)
    print(H)
    while H!=[]:
        x=heapq.heappop(H)
        u=x[1]
        if(v[x[1]].dist>=x[0]):
            for edge in G[u]:
                node=edge[0]
                weight=edge[1]
                if v[node].dist>v[u].dist+weight:
                    v[node].dist=v[u].dist+weight
                    heapq.heappush(H,[v[node].dist,node])
                    v[node].pred=u
                    v[node].path=v[u].path+str(u)+","
                
    for i in range(len(G)):
        print("node",i,"distance",v[i].dist)
        v[i].path+=str(i)
        print("path",v[i].path)        


def main():
    H=[]
    for i in range(len(G)):
        H.append([1000,i])
    s=int(input("enter the source vertex\n"))
    Dijkstra(G,s,H)



if __name__ == "__main__":
    main()