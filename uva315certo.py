# -*- coding: utf-8 -*-

# Python program to find articulation points in an undirected graph

from collections import defaultdict

N = 6
visited = []
lowpt = []
pai = []
ap = [] #To store articulation points
nivel = []

mat =[]


def DFS(v):
    global mat, nivel, N 
    i = 1
    for i in range(N):
        if (mat[v][i]==0) and (nivel[i] == 1000):
            mat[v][i] = 2
            mat[i][v] = 0 
            pai[i] = v
            nivel[i] = nivel[v]+1
            DFS(i)

def f_lowpt(v):
    global mat, nivel, lowpt, N
    lowpt[v]= v
    for i in range(N):
        if mat[v][i]==2:
            if lowpt[i]==1000:
                f_lowpt(i)
            if(nivel[lowpt[i]] < nivel[lowpt[v]]):
                lowpt[v]= lowpt[i]
        if(mat[v][i]==1):
            if(nivel[i]< nivel[lowpt[v]]):
                lowpt[v]= i

def inicialize(N):
    global mat, nivel, lowpt, pai
    for i in range(N):
        pai.append(-1)
        lowpt.append(1000)
        nivel.append(1000)
        mat.append([])
        for j in range(N):
            mat[i].append(0)


def main():
    import sys
    global mat, nivel, lowpt, N
    sys.stdin = open('arquivo.txt')
    while True:
        n = int(input())
        inicialize(n)
        if not n:
            break
        for line in iter(raw_input, '0'):
            a = map(int, line.split())
            k = a[0]
            for v in a[1:]:
                mat[k-1][v-1] = 1
                k = v
        print mat
        N = n
    DFS(0)
    f_lowpt(0)
    print lowpt
    print nivel

if __name__ == "__main__":
    main()
