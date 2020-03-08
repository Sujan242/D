x = int(input("enter the number of the vertices"))
te = []
try :
    while(True):
        te.append(input())
except:
    print(te)
matrix = [[0]*x for _ in range(x)]
for k in range(len(te)):
    matrix[int(te[k][0])][int(te[k][1])] = 1
    matrix[int(te[k][1])][int(te[k][0])] = 1

                
print(matrix)
