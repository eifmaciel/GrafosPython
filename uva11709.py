# -*- coding: utf-8 -*-

posnum=[0,0,0, 0,0,0]
visit=[0,0,0, 0,0,0]
N = 6
nump = 0

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

def main():
    import sys
    global visit, nump, posnum, N
    nomes = ["McBride, John", "Smith, Peter", "Brown, Anna"]
    graph = [[0,1,1,1,0,0],
             [0,0,0,0,1,1],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,1],
             [0,0,0,0,0,0]]
    GL = [[0,0,0, 0,0,0],[0,0,0, 0,0,0],[0,0,0, 0,0,0], [0,0,0, 0,0,0],[0,0,0,0,0,0],[0,0,0, 0,0,0]]


    sys.stdin = open('arq.txt')
    while True:
        primeira = raw_input()

        if primeira  == '0 0':
            break
        else:
            linha = primeira.split()
            p = int(linha[0])
            t = int(linha[1])
            for i in range(p):
                a = raw_input()
                nomes.append(a)

                for v in a[1:]:
                    print graph
                    graph[k] = [v]
                    k = v


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
                print i
                visit[i]=3
    return 0

if __name__ == "__main__":
    main()
