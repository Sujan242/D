import heapq
class Vertex:
    def __init__(self):
        self.dist = float('infinity')
        self.visited = 0
        self.path_changer = None
        self.weight = 0



def prims(graph,pq):
    vertex_list = []
    for _ in range(len(graph)): 
        vertex_list.append(Vertex())
    vertex_list[0].dist = 0
    pq[0][0]= 0
    heapq.heapify(pq)
    T =set()
    sum = 0
    while(len(pq)>0):
        vertex = heapq.heappop(pq)            
        if(vertex_list[vertex[1]].visited==0):
            if(vertex_list[vertex[1]].path_changer!= None):
                T.add((vertex_list[vertex[1]].path_changer,vertex[1]))
                sum = sum+vertex_list[vertex[1]].weight
            print("Node added",vertex_list[vertex[1]].path_changer,vertex[1])
            for neighbour in graph[vertex[1]]:
                node = neighbour[0]
                weight = neighbour[1]
                if(vertex_list[node].dist>weight):
                    vertex_list[node].dist=weight
                    vertex_list[node].path_changer = vertex[1]
                    vertex_list[node].weight = weight
                    heapq.heappush(pq,[vertex_list[node].dist,node])                    
            vertex_list[vertex[1]].visited=1
    print(T,sum)   








def main():
    ''' Adjacency List representation. G is a list of lists. '''
    G = [] 

    file=open('input4.txt','r')
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
    pq=[]
    print(G)
    for i in range(len(G)):
        pq.append([float('infinity'),i])   
    prims(G,pq)

if __name__ == '__main__':
    main()























