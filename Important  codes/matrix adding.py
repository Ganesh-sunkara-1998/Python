# adding of matrices...
matrix1=[[],[],[]]
matrix2=[[],[],[]]
matrix3=[[],[],[]]
for i in range(3):
    for j in range(1):
        e=int(input("enter your elements to store matrix1:-"))
        matrix1[i].append(e)
    print(matrix1)
for i in range(3):
    for j in range(1):
        e=int(input("enter your elements is to be stored in matrix2:-"))
        matrix2[i].append(e)
    print(matrix2)
for i in range(3):
    for j in range(1):
        e=int(input("enter your elements is to be stored in matrix3:-"))
        matrix3[i].append(e)
    print(matrix3)
list=[matrix1[i][j]+matrix2[i][j]+matrix3[i][j] for j in range(1) for i in range(3)]
print(list)
