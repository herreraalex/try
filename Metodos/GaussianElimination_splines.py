import numpy as np
import math 

def simpleGaussianElimination(A, b):
    Ab = concatenar(A, b)
    n = len(Ab)
    for k in range(n):
        print('step ',k)
        print(Ab)
        if(Ab[k][k]==0):
            Ab = searchAndSwapZero(Ab, n, k)
        for i in range(k+1, n):
            mult = Ab[i][k]/Ab[k][k]
            for j in range(k, n+1):
                Ab[i][j] = Ab[i][j] - mult*Ab[k][j]
    print('x ',backSubstitution(Ab))
    return backSubstitution(Ab)
def searchAndSwapZero(Ab, n, i):
    for j in range(i+1,n):
        if(Ab[j][i]!=0):
            temp = Ab[i]
            Ab[i] = Ab[j]
            Ab[j] = temp
            break
    return Ab

def partialGaussianElimination(A, b):
    Ab = concatenarMatriz(A, b)
    n = len(Ab)
    for k in range(n):
        print('step ',k)
        printMatriz(Ab)
        Ab = searchBiggerandSwap(Ab, n, k)
        for i in range(k+1, n):
            mult = Ab[i][k]/Ab[k][k]
            for j in range(k, n+1):
                Ab[i][j] = Ab[i][j] - mult*Ab[k][j]
    print('X ',backSubstitution(Ab))
    return backSubstitution(Ab)

def searchBiggerandSwap(Ab, n, i):
    row = i
    for j in range(i+1,n):
        if(abs(Ab[row][i]) < abs(Ab[j][i])):
            row = j
    temp = Ab[i]
    Ab[i] = Ab[row]
    Ab[row] = temp
    return Ab

def totalGaussianElimination(A, b):
    order = []
    Ab = concatenarMatriz(A, b)
    n = len(Ab)
    for k in range(n):
        print('step ',k)
        printMatriz(Ab)
        Ab, order = searchTheBiggestandSwap(Ab, n, k, order)
        for i in range(k+1, n):
            mult = Ab[i][k]/Ab[k][k]
            for j in range(k, n+1):
                Ab[i][j] = Ab[i][j] - mult*Ab[k][j]
    print('x ',sortResult(backSubstitution(Ab), order))
    return sortResult(backSubstitution(Ab), order)

def searchTheBiggestandSwap(Ab, n, k, order):
    row = k
    column = k
    for i in range(k,n):
        for j in range(k,n):
            if(abs(Ab[row][column]) < abs(Ab[i][j])):
                row = i
                column = j
    temp = Ab[k]
    Ab[k] = Ab[row]
    Ab[row] = temp
    Ab = swapColumn(Ab, k, column)
    order.append((k, column))
    return (Ab, order)

def swapColumn(Ab, c1, c2):
    for i in range(len(Ab)):
        temp = Ab[i][c1]
        Ab[i][c1] = Ab[i][c2]
        Ab[i][c2] = temp
    return Ab

def sortResult(x, order):
    for i in range(len(order)-1, -1, -1):
        temp = x[order[i][0]]
        x[order[i][0]] = x[order[i][1]]
        x[order[i][1]] = temp
    return x

def concatenarMatriz(A, b):
    n = len(A)
    for i in range(n):
        A[i].append(b[i])
    return A

#b = [[4],[5],[6]] this is the format
def concatenar(a,b):
    a = np.array(a)
    b =np.array(b)
    matriz = np.concatenate((a, b), axis=1)
    return matriz

def backSubstitution(Ab):
    n= len(Ab)
    x = []
    for i in range(n):
        x.append(0)

    for i in range(n-1, -1, -1):
        sum = 0
        for j in range(i+1, n):
            sum+= Ab[i][j]*x[j]
        x[i] = (Ab[i][n]-sum)/Ab[i][i]
    return x

def printMatriz(M):
    for i in range(len(M)):
        print(M[i])


A = [[0, -2, -2, -1], 
    [0, 8, -2, -2], 
    [-1, -1, 4, 0], 
    [-1, -2, 2, 7]]

b = [[1], [1], [1], [1]]
b2 = [1,1,1,1]

if __name__ == "__main__":
    #print('simple Gaussian Elimination')
    #Ab = simpleGaussianElimination(A,b)
    
    #print('----------------------')
    #print('Partial Gaussian Elimination')
    #Ab = partialGaussianElimination(A,b2)
    #print('----------------------')
   # print('Total Gaussian Elimination')
    totalGaussianElimination(A,b2)
