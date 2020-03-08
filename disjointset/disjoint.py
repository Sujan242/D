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


def main():
    ds = DisjointSets()
    
    nodes = []
    for i in range(10):
        node = ds.makeset(i)
        nodes.append(node)

    ds.union(nodes[0],nodes[1])
    print(ds.findset(nodes[0]))    # Should print 1
    ds.union(nodes[0],nodes[2])
    print(ds.findset(nodes[2]))    # Should print 1
    ''' Add more tests!'''

if __name__ == '__main__':
    main()




