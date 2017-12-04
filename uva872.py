# -*- coding: utf-8 -*-

visited = [0,0,0,0,0,0]
G = [[0,1, 0, 0, 0, 0],
	[0, 0, 1, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 1, 0, 1, 1],
	[1, 1, 0, 0, 0, 1],
	[0, 0, 1, 0, 0, 0]]
resultado = []
lista= [0,0,0,0,0,0]

def OrdemTopoAlt(G, graph):
	L = []
	for i in range(6):
		G[i] = 0

	# import ipdb; ipdb.set_trace()
	for i in range(6):
		for j in range(6):
			if graph[i][j]:
				G[j] = G[j] + 1
	for i in range(6):
		if G[i] == 0:
			L.append(i)

	k = 0
	while L:
		v = L[0]
		print v
		L.remove(v)
		for i in range(6):
			if graph[v][i]:
				G[i] = G[i] - 1
				if G[i] == 0:
					L.append(i)

def main():
	global G, resultado, lista
	input("%d\n\n", &N);
 
    while line:  
        line = raw_input()
        lin = line.split(' ')
        tam = len(lin)
 
        getline(cin, line);
        ss.clear();
        ss.str(line);
        adj.clear();
        adj.resize(256);
        while(ss >> a >> b >> c)
            adj[a].push_back(c);
 
        if(!dfs(""))
            printf("NO\n");
        if(!getline(cin, line)) break;
	# OrdemTopo(G)
	# print resultado
	OrdemTopoAlt(lista, G)

if __name__ == "__main__":
    main()