# -*- coding: utf-8 -*-

# __author__      = "Eliane I. F. Maciel"

# uva 315 Networking

# Programa desenvolvido em Python 3.5. Foi utilizado uma lista de adjacencias para representar o grafo.
# Usando o tipo de estrutura dicionário para armazenar a lista de adjacencias.
# graph = {0:[], 1: [5, 2], 2: [1,3], 3: [2,4], 4: [3], 5: [1]}


import sys
from collections import defaultdict


def ArticulationPoints(graph):
    def dfs(u):
        lowpt[u] = number[u] = contador[0]
        contador[0] += 1
        for v in graph[u]:
            if (number[v] == 0):
                pai[v] = u
                if (u == dfsRoot):
                    children[0] += 1
                dfs(v)
                if (lowpt[v] >= number[u]):
                    ap[u] = True
                if (lowpt[v] > number[u]):
                    lowpt[u] = min(lowpt[u], lowpt[v])
            elif (v != pai[u]):
                lowpt[u] = min(lowpt[u], number[v])
    lowpt = {}
    number = {}
    pai = {}
    ap = {}
    contador = [1]
    for v in graph:
        ap[v] = False
        number[v] = 0
        pai[v] = None

    for v in graph:
        if (number[v] == 0):
            dfsRoot = v
            children = [0]
            dfs(v)
            ap[dfsRoot] = (children[0] > 1)
    return sum(ap.values())

def main():
    sys.stdin = open('input.txt')
    while True:
        n = int(input())
        if not n:
            break
        graph = defaultdict(list)
        for line in iter(input, '0'):
            a = line.split(' ')
            k = int(a[0])
            for v in a[1:]:
                graph[k].append(v)
                graph[v].append(k)
        print(ArticulationPoints(graph))
    # return 0

if __name__ == "__main__":
    main()