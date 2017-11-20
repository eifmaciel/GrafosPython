# -*- coding: utf-8 -*-

# Python program to find articulation points in an undirected graph

from collections import defaultdict

#This class represents an undirected graph
#using adjacency list representation

tam = 4
visited = [False] * (tam)
disc = [float("Inf")] * (tam)
low = [float("Inf")] * (tam)
parent = [-1] * (tam)
ap = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]] #To store articulation points

int dfs(int** graph, int node, int goal, int* path, size_t* path_size) {
  size_t i, size;
  int v;
  // se a busca atingiu o vértice de destino, retorna este
  if(node == goal) {
    return goal;

  // caso contrário, realiza a busca nos vértices adjacentes
  } else {

    // [
    // armazena a quantidade de vértices conectados ao vértice atual
    size = graph[node][0];
    // elimina o vértice atual da busca para que este
    // não volte a ser buscado novamente - elimina recursão infinita
    graph[node][0] = 0;
    // ]

    // para cada vértice v adjacente ->
    for(i = 1; i <= size; i++) {
      // se a busca no vértice adjacente atingiu o destino,
      // insere o vértice atual no caminho percorrido
      // e retorna o vértice de destino para que os níveis superiores
      // da recursão saibam que a busca foi concluída
      if(dfs(graph, graph[node][i], goal, path, path_size) == goal) {

        // path[*path_size] = node;
        // *path_size = *path_size + 1;
        // ^
        path[(*path_size)++] = node;

        return goal;
      }
    }
  }
}

def dfs(graph, node, goal, path, path_size):s
    i = 0, size= 0
    v = 0
    # se a busca atingiu o vértice de destino, retorna este
    if(node == goal):
        return goal

    # caso contrário, realiza a busca nos vértices adjacentes
    else:

        #  [
        # armazena a quantidade de vértices conectados ao vértice atual
        # size = graph[node][0];
        #  elimina o vértice atual da busca para que este
        #  não volte a ser buscado novamente - elimina recursão infinita
        # graph[node][0] = 0;
        #  ]

        # para cada vértice v adjacente ->
        for i in range(size):
            #  se a busca no vértice adjacente atingiu o destino,
            #  insere o vértice atual no caminho percorrido
            #  e retorna o vértice de destino para que os níveis superiores
            #  da recursão saibam que a busca foi concluída
            if(dfs(graph, graph[node][i], goal, path, path_size) == goal) {

            // path[*path_size] = node;
            // *path_size = *path_size + 1;
            // ^
            path[(*path_size)++] = node;

            return goal;
            }
        }
  }
}


def busca_DFS(graph, u):
  '''A recursive function that find articulation points
  using DFS traversal
  u --> The vertex to be visited next
  visited[] --> keeps tract of visited vertices
  disc[] --> Stores discovery times of visited vertices
  parent[] --> Stores parent vertices in DFS tree
  ap[] --> Store articulation points'''

  #Count of children in current node
  children =0

  # Mark the current node as visited and print it
  visited[u]= True


  #Recur for all the vertices adjacent to this vertex
  for v in graph[u]:
      # If v is not visited yet, then make it a child of u
      # in DFS tree and recur for it
      if visited[v] == False :
          parent[v] = u
          children += 1
          busca_DFS(graph, v)

          # Check if the subtree rooted with v has a connection to
          # one of the ancestors of u
          low[u] = min(low[u], low[v])

          # u is an articulation point in following cases
          # (1) u is root of DFS tree and has two or more chilren.
          if parent[u] == -1 and children > 1:
              ap[u][v] = 1

          #(2) If u is not root and low value of one of its child is more
          # than discovery value of u.
          if parent[u] != -1 and low[v] >= disc[u]:
              ap[u][v] = 1

          # Update low value of u for parent function calls
      elif v != parent[u]:
          low[u] = min(low[u], disc[v])


#The function to do DFS traversal. It uses recursive APUtil()
def ArticulationPointer(graph):

  # Mark all the vertices as not visited
  # and Initialize parent and visited,
  # and ap(articulation point) arrays

  # Call the recursive helper function
  # to find articulation points
  # in DFS tree rooted with vertex 'i'
  for i in range(tam):
      if visited[i] == False:
        busca_DFS(graph, i)
  print ap
  for index in ap:
    for j in ap:
        print index, j
        if ap[index][j]:
            print index, j

def main():
    graph = [[0,1,0,0], [1,0,1,0], [0,1,0,1], [0,0,1,0]]
    ArticulationPointer(graph)


if __name__ == "__main__":
    main()
