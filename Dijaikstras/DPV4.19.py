import heapq
class Vertex:
    def __init__(self):
        self.dist = float('infinity')
        self.pred = None
        self.path = ""
        self.cost = 0



def calculate_distances(graph,starting_vertex,pq,cost):
    vertex_list = []
    for i in range(len(graph)): 
        x = Vertex()
        x.cost = cost[i]
        vertex_list.append(x)
    vertex_list[starting_vertex].dist = cost[starting_vertex]
    pq[starting_vertex][0]= 0
    heapq.heapify(pq)
    while(len(pq)>0):
        vertex = heapq.heappop(pq)
        if(vertex_list[vertex[1]].dist>=vertex[0]):
            for neighbour in graph[vertex[1]]:
                node = neighbour[0]
                weight = neighbour[1]
                if(vertex_list[node].dist>vertex_list[vertex[1]].dist+weight+vertex_list[node].cost):
                    vertex_list[node].dist= vertex_list[vertex[1]].dist+weight+vertex_list[node].cost
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
    vertexcost = []

    file=open('inputcost.txt','r')
    for line in file:
        line=line.strip()
        adjacentVertices = []
        first=True
        second = False
        for edge in line.split(' '):
            if first:
                first=False
                second =True
                continue
            if second:
                second=False
                vertexcost.append(int(edge))
                continue
            node,weight = edge.split(',')
            adjacentVertices.append((int(node),int(weight)))
        G.append(adjacentVertices)
    file.close()
    pq=[]
    print(G)
    print(vertexcost)
    for i in range(len(G)):
        pq.append([float('infinity'),i])   
    calculate_distances(G,0,pq,vertexcost)

if __name__ == '__main__':
    main()























