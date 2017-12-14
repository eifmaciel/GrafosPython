# -*- coding: utf-8 -*-

n = 0
Part = []
Count = 0
Free = []
adj = []
radj = []
Node = []
N = 0


def Init(n):
    global Free, Part, Count, adj, radj, Node
    Free = []
    Part = []
    Count = 0
    adj = []
    radj = []
    Node = []
    for i in range(n):
        Free.append(True)
        Part.append(0)
        adj.append([])
        radj.append([])


def DFS1(u):
    global Free, Node, adj, N
    Free[u] = False
    for i in range(len(adj[u])):
        if Free[adj[u][i]]:
            DFS1(adj[u][i])
    Node.append(u)


def DFS2(u, p):
    Free[u] = True
    Part[u] = p
    for i in range(len(radj[u])):
        if not Free[radj[u][i]]:
            DFS2(radj[u][i], p)


def main():
    Case = 0
    m = 0
    u = 0
    v = 0
    Case = int(input())
    Com = []
    var = ""
    result = []
    import sys
    sys.setrecursionlimit(1500)
    global Free, Part, Count, adj, radj, Node, N
    while Case:
        var = input()
        divide = var.split(' ')
        N = int(divide[0])
        m = int(divide[1])
        Init(N)
        Com = []
        for i in range(N):
            Com.append(True)
        for j in reversed(range(m)):
            line = input()
            pecas = line.split(' ')
            pos1 = int(pecas[0])
            pos2 = int(pecas[1])
            adj[pos1-1].append(pos2-1)
            radj[pos2-1].append(pos1-1)

        for i in range(N):
            if Free[i]:
                try:
                    DFS1(i)
                except:
                    print("")
        nPart = 0
        for i in reversed(range(len(Node))):
            if not Free[Node[i]]:
                try:
                    DFS2(Node[i], nPart)
                    nPart += 1
                except:
                    print("")
        for u in range(N):
            for i in range(len(adj[u])):
                v = adj[u][i]
                if (Part[u] != Part[v]):
                    Com[Part[v]] = False
        ans = 0
        i = 0
        for i in range(nPart):
            if Com[i]:
                ans += 1
        result.append(ans)
        Case -= 1
    for i in result:
        print(i)
    print("")
    return 0


if __name__ == "__main__":
    main()
