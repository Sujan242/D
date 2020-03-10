class Node:
    def __init__(self,x):
        self.value = x
        self.parent = self
        self.height = 0

    def __str__(self):
        return str(self.value)

    

class DisjointSets: 


    def getnode(self,value):
        x = Node(value)
        return x


        
    def makeset(self,value):
        return self.getnode(value)

    def findset(self,x):
        if(x.parent == x):
            return x
        x.parent = self.findset(x.parent)
        return x.parent

    def union(self,x,y):
        px = self.findset(x)
        py = self.findset(y)
        if(px==py):
            return
        if(px.height>py.height):
            py.parent = px
        elif(px.height<py.height):
            px.parent = py
        else:
            px.parent = py
            py.height = py.height+1






def kruskal(edges,vertexs,x):
    edges = sorted(edges,key = lambda x:x[1],reverse=True)
    T = set()
    sum = 0
    for i in range(len(edges)):
        if(x.findset(vertexs[edges[i][0][0]])!=x.findset(vertexs[edges[i][0][1]])):
            T.add(edges[i][0])
            sum = sum+edges[i][1]
            x.union(vertexs[edges[i][0][0]],vertexs[edges[i][0][1]])
    print(T,sum)


    
    



def take_input():
    rem_node = [0,3,1,4]
    Graph = []
    k_graph  = []
    file = open('input3.txt','r')
    k = 0
    removedgraph = []
    u_to_v_graph = []

    for line in file:
        first = True
        adjacentvertices = []
        for node in line.split(' '):
            if first:
                first =False
                continue
            edge,weight = node.split(',') 
            adjacentvertices.append((int(edge),int(weight)))
            k_graph.append(((k,int(edge)),int(weight)))
            if (k not in rem_node and int(edge) not in rem_node):
                removedgraph.append(((k,int(edge)),int(weight)))
            elif int(edge) not in rem_node and k in rem_node:
                u_to_v_graph.append(((k,int(edge)),int(weight)))



        k += 1
        Graph.append(adjacentvertices)
    # print(Graph)
    print(k_graph)
    print(removedgraph)
    print(u_to_v_graph)
    x = DisjointSets()
    vertexs= []
    for i in range(len(Graph)):
        vertexs.append(x.makeset(i))
    kruskal(k_graph,vertexs,x)


        


def main():
    take_input()


if __name__ == '__main__':
    main()




