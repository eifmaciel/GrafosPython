# -*- coding: utf-8 -*-

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


def BuscaProfOrdenTopo(v):
	global G, visited, N, lin
	visited[v] = 1

	for j in range(N):
		if G[v][j]:
			if not visited[j]:
				BuscaProfOrdenTopo(j)
	print lin[v],

def OrdemTopo(G):
	global N, visited
	for i in range(N):
		visited[i] = 0
	for j in range(N):
		if not visited[j]:
			BuscaProfOrdenTopo(j)


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
	for i in pega:
		dado = i.split('<')
		pos1 = lin.index(dado[0])
		pos2 = lin.index(dado[1])
		G[pos1][pos2] = 1
	N= tam

	OrdemTopo(G)
	# dfs(0)
	# OrdemTopoAlt(lista, G, tam)
	# printResult()



if __name__ == "__main__":
    main()
