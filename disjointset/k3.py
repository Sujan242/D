import disjoint

def kruskal(G,edge):
    vertex = []
    x = disjoint.DisjointSets()
    for i in range(len(G)):
        vertex.append(x.makeset(i))
    T = set()
    edge = sorted(edge, key=lambda x: x[1])
    for i in range(len(edge)):
        if(x.findset(vertex[edge[i][0][0]])!=x.findset(vertex[edge[i][0][1]])):
            print(edge[i][0][0],edge[i][0][1])
            T.add(edge[i][0])
            x.union(vertex[edge[i][0][0]],vertex[edge[i][0][1]])
    print("final",T)
    print(T)


















def main():
    ''' Adjacency List representation. G is a list of lists. '''
    G = [] 
    numberto_edge = []
    file=open('input2.txt','r')
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
    k = 0
    for j in range(len(G)):
        for i in range(len(G[j])):
            if not (((G[j][i][0],j),G[j][i][1]) in numberto_edge):
                numberto_edge.append(((j,G[j][i][0]),G[j][i][1]))
                k = k+1


    print(numberto_edge)
    kruskal(G,numberto_edge)
if __name__ == '__main__':
    main()
