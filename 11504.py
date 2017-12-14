# -*- coding: utf-8 -*-

visit = []
nump = 0
posnum = []
GL = []
graph = []

def DFS(v):
    global visit, nump, GL, N, graph
    visit[v] = 1
    for i in range(N):
        if graph[v][i] and visit[i] == 0:
            DFS(i)
    nump+=1
    posnum[v] = nump

def DFS2(v):
    global visit, nump, GL, N
    visit[v]=2
    i = 0
    for i in range(N):
        if GL[v][i] and visit[i] == 0:
          DFS2(i)


def inicializa(n):
    global visit, posnum,GL, graph, nump
    visit = []
    posnum = []
    GL = []
    graph = []
    nump = 0
    for i in range(n):
        posnum.append(0)
        visit.append(0)
        GL.append([])
        graph.append([])

        for j in range(n):
            GL[i].append(0)
            graph[i].append(0)


def main():
    global visit, nump, posnum, N, GL, graph
    nomes = []
    soma = 0
    result = []
    count = 0
    valor = int(input())
    while valor:
        var = input()
        divide = var.split(' ')
        N = int(divide[0])
        p = int(divide[1])
        inicializa(N)
        for i in range(p):
            line = input()
            pecas = line.split(' ')
            pos1 = int(pecas[0])-1
            pos2 = int(pecas[1])-1
            graph[pos1][pos2] = 1
        for i in range(N):
            if not visit[i]:
                DFS(i)

        for i in range(N):
            for j in range(N):
                GL[i][j] = graph[j][i]
        soma = 0
        cout = 0
        flag = True
        while True:
            maior = -1
            pm = 0
            for i in range(N):
                if posnum[i] > maior and visit[i] == 1:
                    maior = posnum[i]
                    pm = i
            if maior == -1:
                break
            DFS2(pm)
            for i in range(N):
                if visit[i] == 2:
                    if i == 0:
                        flag = True
                    if flag:
                        cout+=1
                        flag = False
                    print(i)
                    visit[i] = 3
        result.append(cout)
        valor -= 1
    for i in result:
        print(i)
    print("")
    return 0

if __name__ == "__main__":
    main()
