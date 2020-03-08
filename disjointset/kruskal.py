import disjoint

def kruskal(G,weightlist,edge):
    vertex = []
    x = disjoint.DisjointSets()
    for i in range(len(G)):
        vertex.append(x.makeset(i))
    T = set()
    position = sorted(range(len(weightlist)), key=weightlist.__getitem__)
    for i in range(len(position)):
        if(x.findset(vertex[edge[position[i]][0]])!=x.findset(vertex[edge[position[i]][1]])):
            print(edge[position[i]][0],edge[position[i]][1])
            T = T.union(edge[i])
            x.union(vertex[edge[position[i]][0]],vertex[edge[position[i]][1]])
    print("final",T)
    for i in range(len(T)):
        print(edge[i])


















def main():
    ''' Adjacency List representation. G is a list of lists. '''
    G = [] 
    numberto_edge = {}
    W = []
    file=open('disjointset/input2.txt','r')
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
            if not ((G[j][i][0],j) in numberto_edge.values()):
                print(G[j][i][0],j,)
                numberto_edge[k] = (j,G[j][i][0])
                W.append(G[j][i][1])
                k = k+1


    print(G)
    print(W)
    print(numberto_edge)
    kruskal(G,W,numberto_edge)
if __name__ == '__main__':
    main()
