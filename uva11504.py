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
        if adj[u][i] and not Free[i]:
            DFS1(i)
    Node.append(u)

def DFS2(u, p):
    Free[u] = True
    Part[u] = p
    for i in range(len(adj[u])):
        if not Free[i]:
            DFS2(i, p)

def main():
    Case = 0
    m = 0
    u = 0
    v = 0
    Case = int(input())
    Com = []
    var = ""
    result = []
    global Free, Part, Count, adj, radj, Node, N
    while Case:
        var = input()
        divide = var.split(' ')
        N = int(divide[0])
        m = int(divide[1])
        Init(N)
        for i in range(N):
            Com.append(True)
        while m:
            line = input()
            pecas = line.split(' ')
            pos1 = int(pecas[0])
            pos2 = int(pecas[1])
            adj[pos1-1].append(pos2-1)
            radj[pos2-1].append(pos1-1)
            m -= 1

        for i in range(N):
            if Free[i]:
                DFS1(i)
        nPart = 0
        i = len(Node) - 1
        while i<= len(Node) and i > 0:
            if not Free[Node[i]]:
                DFS2(Node[i], nPart)
                nPart += 1
            i -= 1
        print(adj)
        for u in range(N):
            for i in range(N):
                v = adj[u][i]

                print("v %d" % v)
                print("Part[u] %d Part[i] %d" %(Part[u], Part[i]))
                if (Part[u] != Part[i]):
                    Com[Part[v]] = False
        ans = 0
        i = 1
        while i <= nPart:
            if Com[i]:
                ans += 1
            i += 1
        result.append(ans)
        Case -= 1
    for i in result:
        print(i)
    return 0


if __name__ == "__main__":
    main()
