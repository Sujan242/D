
graph = []
visited = []
finish = []
start = []
pred = []
time = 0 
grev = []
track_h_finish = []
flag = True
def DFS(s,graph):
    global time
    global flag
    print(s)
    visited[s] = 1
    start[s] = time
    time = time + 1 
    for node in graph[s]:
        if(visited[node]==0):
            pred[node] = s
            DFS(node,graph)
    finish[s] = time
    if flag:
        track_h_finish.append(s)
    time = time + 1 
    return time
    

def take_input():
    global graph
    global start
    global finish
    global pred
    global visited
    global time
    global grev
    global track_h_finish 
    file = open("inputsscc2.txt",'r')
    for line in file:
        adjacentvertices  = []
        first = True
        for node in line.split(' '):
            if first:
                first = False
                continue
            adjacentvertices.append(int(node))
        graph.append(adjacentvertices)
    grev = [[] for _ in range(len(graph))]
    print(graph)
    for i in range(len(graph)):
        adjacentvertices = []
        for node in graph[i]:
            grev[node].append(i)

    visited = [0]*len(graph)
    pred =    [None]*len(graph)
    finish =  [0]*len(graph)
    start =   [0]*len(graph)



def scc(visited):
    for _ in range(len(graph)):
            starting_vertex = track_h_finish.pop()
            if(visited[starting_vertex]==0):
                print("component")
                DFS(starting_vertex,graph)
            else:
                continue



def main():
    global visited
    global flag
    take_input()
    for i in range(len(graph)):
        if visited[i]==0:
            DFS(i,grev)
    print(visited,finish,track_h_finish)
    visited = [0]*len(graph)
    flag = False
    scc(visited)


if __name__ == '__main__':
    main()




