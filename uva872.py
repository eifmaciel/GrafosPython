# -*- coding: utf-8 -*-

# visited = [0,0,0,0,0,0]
# G = [[0,1, 0, 0, 0, 0],A  A<B B<C D<C D<E D<F E<A E<B E<F F<C
# 	[0, 0, 1, 0, 0, 0],B
# 	[0, 0, 0, 0, 0, 0],C
# 	[0, 0, 1, 0, 1, 1],D
# 	[1, 1, 0, 0, 0, 1],E
# 	[0, 0, 1, 0, 0, 0]]F
# resultado = []
# lista= [0,0,0,0,0,0]

visited = []
G = []
resultado = []
lista= []
lin = []

def printResult():
	global resultado
	if resultado:
		for i in resultado:
			print(lin[i], end="")
		print("\n")
	else:
		print('NO')

def dfs(Idx, n):
	if Idx == n:
		print("aqui");
		has = 1
		print(lista[0])
		i = 1
		for i in range(n):
			resultado.append(i)
		printResult()
		return
	i = 0
	j = 0
	for i in range(n):
		if not visited[i]:
			for j in range(Idx):
				print(lin[i], lista[j])
				# if(G[lin[i]-65][lista[j]-65]):
					# break
			if(j == Idx):
				lista[Idx] = lin[i]
				visited[i] = 1
				dfs(Idx+1, n)
				visited[i] = 0

def OrdemTopoAlt(G, graph, N, index):
	global resultado
	L = []
	for i in range(N):
		G[i] = 0

	# import ipdb; ipdb.set_trace()
	for i in range(N):
		for j in range(N):
			if graph[i][j]:
				G[j] = G[j] + 1
	for i in range(N):
		if G[i] == 0:
			L.append(i)

	k = 0
	while L:
		v = L[0]
		resultado.append(v)
		L.remove(v)
		for i in range(N):
			if graph[v][i]:
				G[i] = G[i] - 1
				if G[i] == 0:
					L.append(i)


def inicialize(N):
	global visited, lista, G, lin
	for i in range(N):
		visited.append(0)
		lista.append(0)
		G.append([])
		for j in range(N):
			G[i].append(0)
	# print G

def main():
	global G, resultado, lista, lin
	import sys
	line =True
	# sys.stdin = open('arq2.txt')
	# import ipdb; ipdb.set_trace()
	N = input()
	white = input()
	# while line:
	line = input()
	lin = line.split(' ')
	tam = len(lin)
	line2 = input()
	pega = line2.split(' ')
	inicialize(tam)
	for i in pega:
		dado = i.split('<')
		pos1 = lin.index(dado[0])
		pos2 = lin.index(dado[1])
		G[pos1][pos2] = 1

	dfs(0, tam)
	# OrdemTopoAlt(lista, G, tam, index)



if __name__ == "__main__":
    main()
