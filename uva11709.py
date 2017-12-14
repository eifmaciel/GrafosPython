# -*- coding: utf-8 -*-

posnum=[]
visit=[]
N = 0
nump = 0
nomes = []
GL = []
graph = []
soma = 0


def DFS(v, G):
    global visit, nump, posnum, N
    visit[v]=1
    for i in range(N):
        if (G[v][i] and visit[i]==0):
            DFS(i, G)
    nump += 1
    posnum[v] = nump

def DFS2(v,GL):
    visit[v]=2
    for i in range(N):
       if (GL[v][i] and visit[i]==0):
          DFS2(i, GL)

def inicializa(n):
    global visit, posnum,GL, graph
    for i in range(n):
        posnum.append(0)
        visit.append(0)
        GL.append([])
        graph.append([])

        for j in range(n):
            GL[i].append(0)
            graph[i].append(0)

def main():
    import sys
    global visit, nump, posnum, N, GL, graph
    nomes = []

    valor = input()

    while valor != '0 0':
        var = valor.split(' ')
        N = int(var[0])
        p = int(var[1])
        inicializa(N)
        for i in range(N):
	        a = input()
	        nomes.append(a)
        pos1 = None
        pos2 = None
        for j in range(p):
            b = input()
            c = input()
            pos1 = nomes.index(b)
            pos2 = nomes.index(c)
            graph[pos1][pos2] = 1
        print(graph)
        DFS(0, graph)
        for i in range(N):
            for j in range(N):
                GL[i][j]=graph[j][i]
        while (1):
            maior=-1
            pm=0
            for i in range(N):
                if (posnum[i]>maior and visit[i]==1):
                    maior=posnum[i]
                    pm=i
            if (maior==-1):
                break
            DFS2(pm, GL)
            for i in range(N):
                if (visit[i]==2):
                    soma += i
                    visit[i]=3
        print(soma)
        valor = input()
        if valor == '0 0':
            break

    return 0

if __name__ == "__main__":
    main()
