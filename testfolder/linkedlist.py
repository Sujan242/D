class Node:
    def __init__(self):
        self.value = None
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None


    def getnode(self,value):
        x = Node()
        x.value = value
        x.next = None
        return x


    
    def insert(self,value):
        if self.head == None:
            x = self.getnode(value)
            self.head = x
            self.tail = x
        else:
            x = self.getnode(value)
            self.tail.next = x
            self.tail  =x
            
    
    def printf(self):
        x = self.head
        while x!=None:
            print(x.value)
            x = x.next


list = Linked_list()
for i in range(8):
    list.insert(i)
list.printf()
