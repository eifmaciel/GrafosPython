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
N= 0
def printResult():
	global resultado
	if resultado:
		for i in resultado:
			print lin[i]
			# print  lin[i], end="")
		print "\n"
	else:
		print 'NO'

def dfs(Idx):
	global N, lista, lin, G, visited
	# import ipdb; ipdb.set_trace()
	print  'inicio', Idx, N
	if Idx == N:
		print  "aqui"
		has = 1
		print  lista[0]
		i = 1
		for i in range(N):
			print  lista[i]
		# printResult()
		return
	i=0
	j=0
	for i in range(N):
		if not visited[i]:
			for j in range(Idx):
				pos1 = lin.index(lin[i])
				pos2 = lin.index(lista[j])
				if G[pos1][pos2]:
					pass
			if(j == Idx):
				print  j, Idx, 'aqui'
				lista[Idx] = lin[i]
				visited[i] = 1
				print  Idx+1
				dfs(Idx+1)
				visited[i] = 0

def OrdemTopoAlt(G, graph, N):
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
	global G, resultado, lista, lin, N
	import sys
	grau = []
	line =True
	# sys.stdin = open('arq2.txt')
	# import ipdb; ipdb.set_trace()
	t = input()
	white = raw_input()
	# while line:
	line = raw_input()
	lin = line.split(' ')
	tam = len(lin)
	line2 = raw_input()
	pega = line2.split(' ')
	inicialize(tam)
	for i in range(tam):
		grau.append(0)
	print grau
	for i in pega:
		dado = i.split('<')
		pos1 = lin.index(dado[0])
		pos2 = lin.index(dado[1])
		G[pos1][pos2] = 1
		grau[pos2] += 1
	N= tam


	# dfs(0)
	OrdemTopoAlt(lista, G, tam)
	printResult()



if __name__ == "__main__":
    main()
