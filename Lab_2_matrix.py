import math as m
import numpy as np

def snake(nom,n):
    sch=1
    arr=np.zeros((2*n,2*n))
    if nom == 0:
        for i in range(n):
            if i % 2 == 0:
                for j in range(n):
                    arr[i,j]=sch
                    sch+=1
            else:
                for j in range(n-1, -1,-1):
                    arr[i, j] = sch
                    sch += 1
    elif nom==1:
        for i in range(n):
            if i % 2 == 0:
                for j in range(2*n-1, n-1,-1):
                    arr[i,j]=sch
                    sch+=1
            else:
                for j in range(n, 2*n+1):
                    arr[i, j] = sch
                    sch += 1
    elif nom == 2:
        for i in range(2*n-1,n-1,-1):
            if i % 2 == 1:
                for j in range(2*n-1, n-1,-1):
                    arr[i, j] = sch
                    sch += 1
            else:
                for j in range(n, 2 * n):
                    arr[i, j] = sch
                    sch += 1
    return arr
n1=int(input('введите размерность половины матрицы:\n'))
massiv=snake(0,n1)
massiv+=snake(1,n1)
massiv+=snake(2,n1)

print(massiv)