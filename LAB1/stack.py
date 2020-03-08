class stack:
    def __init__(self):
        self.stacklist = []
    def push(self,x):
        self.stacklist.append(x)
    def pop(self):
        if (not self.isEmpty()):
            temp = self.stacklist[:-1]
            self.stacklist = []
            self.stacklist = temp
        else:
            print("stack is empty")
    def print(self):
        print(self.stacklist)
    def isEmpty(self):
        if(self.stacklist == []):
            return True

stack1 = stack()
y = []

while True:
    print("1. push 2. pop 3. print 4. exit \n")
    char  = int(input("choose your option \n"))
    if(char==1):
        x = input("enter the element \n")
        stack1.push(x)
    elif(char==2):
        stack1.pop()
    elif(char==3):
        stack1.print()
    else:
        exit



               