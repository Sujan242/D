import heapq
class Vertex:
    def __init__(self):
        self.dist = float('infinity')
        self.pred = None
        self.path = ""
        self.flag = False



def calculate_distances(graph,starting_vertex,pq):
    vertex_list = []
    for _ in range(len(graph)): 
        vertex_list.append(Vertex())
    vertex_list[starting_vertex].dist = 0
    pq[starting_vertex][0]= 0
    heapq.heapify(pq)
    while(len(pq)>0):
        vertex = heapq.heappop(pq)  
        if(vertex_list[vertex[1]].dist==vertex[0]):
            vertex_list[vertex[1]].dist = True
        if(vertex_list[vertex[1]].dist>=vertex[0]):
            for neighbour in graph[vertex[1]]:
                node = neighbour[0]
                weight = neighbour[1]
                if(vertex_list[node].dist>vertex_list[vertex[1]].dist+weight):
                    vertex_list[node].dist= vertex_list[vertex[1]].dist+weight
                    heapq.heappush(pq,[vertex_list[node].dist,node])
                    vertex_list[node].pred = vertex[1]
                    vertex_list[node].path = vertex_list[vertex[1]].path+str(vertex[1])+","
    for i in range(len(graph)):
        print("Node ",i," is at a distance of  ",vertex_list[i].dist,"from ",starting_vertex)
        vertex_list[i].path += str(i)
        print("path",vertex_list[i].path)







def main():
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
    pq=[]
    for i in range(len(G)):
        pq.append([float('infinity'),i])   
    calculate_distances(G,0,pq)

if __name__ == '__main__':
    main()























