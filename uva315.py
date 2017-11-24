# -*- coding: utf-8 -*-

# Python program to find articulation points in an undirected graph

from collections import defaultdict

#This class represents an undirected graph
#using adjacency list representation

# Mark all the vertices as not visited
# and Initialize parent and visited,
# and ap(articulation point) arrays
tam = 6
visited = [False] * (tam)
disc = [float("Inf")] * (tam)
low = [float("Inf")] * (tam)
parent = [-1] * (tam)
ap = [False] * (tam) #To store articulation points
time = 0

'''A recursive function that find articulation points
using DFS traversal
u --> The vertex to be visited next
visited[] --> keeps tract of visited vertices
disc[] --> Stores discovery times of visited vertices
parent[] --> Stores parent vertices in DFS tree
ap[] --> Store articulation points'''
def APUtil(graph, u, visited, ap, parent, low, disc):

    #Count of children in current node
    children =0

    # Mark the current node as visited and print it
    visited[u]= True

    # Initialize discovery time and low value
    global time
    disc[u] = time
    low[u] = time
    time += 1
    # import ipdb; ipdb.set_trace()
    #Recur for all the vertices adjacent to this vertex
    for v in graph[u]:
        # If v is not visited yet, then make it a child of u
        # in DFS tree and recur for it
        if visited[v] == False :
            parent[v] = u
            children += 1
            APUtil(graph, v, visited, ap, parent, low, disc)

            # Check if the subtree rooted with v has a connection to
            # one of the ancestors of u
            low[u] = min(low[u], low[v])

            # u is an articulation point in following cases
            # (1) u is root of DFS tree and has two or more chilren.
            if parent[u] == -1 and children > 1:
                ap[u] = True

            #(2) If u is not root and low value of one of its child is more
            # than discovery value of u.
            if parent[u] != -1 and low[v] >= disc[u]:
                ap[u] = True

            # Update low value of u for parent function calls
        elif v != parent[u]:
            low[u] = min(low[u], disc[v])


#The function to do DFS traversal. It uses recursive APUtil()
def AP(graph):

    # Call the recursive helper function
    # to find articulation points
    # in DFS tree rooted with vertex 'i'
    for i in range(tam):
        if visited[i] == False:
            APUtil(graph, i, visited, ap, parent, low, disc)

    for i, value in enumerate(ap):
        if value:
            print(i)


# def transforma_grafo(lista):
#     graph = {}
#     for i in lista:
#         graph[i]


def main():
    import sys
    sys.stdin = open('arquivo.txt')
    graph = {}
    global tam
    while True:
        n = int(input())
        if not n:
            break
        for line in iter(raw_input, '0'):
            a = map(int, line.split())
            k = a[0]
            print a
            for v in a[1:]:
                print graph
                graph[k] = [v]
                k = v
    print graph
        

   # graph = {0:[], 1: [5, 2], 2: [1,3], 3: [2,4], 4: [3], 5: [1]}
    #graph = {0:[], 1: [2, 3], 2: [1,6], 3: [1], 4: [5,6], 5: [4], 6:[4,2]}

    # AP(graph)

if __name__ == "__main__":
    main()
