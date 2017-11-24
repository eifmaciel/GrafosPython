visited = [0, 0,0,0,0,0]
mat = [[0,1,1,1,0,0],
	[0,0,0,0,1,1],
	[0,0,0,0,0,0],
	[0,0,0,0,0,0],
	[0,0,0,0,0,1],
	[0,0,0,0,0,0],
	]
nump = 0
posnum = [0,0,0,0,0,0]
def dfs(v):
	global nump, posnum
	for i in range(6):
		if (mat[v][i] and visited[i]==0):
			dfs(i)
	nump += 1
	posnum[v] = nump

def main():
	dfs(0)
	for i in range(6):
		print posnum[i]

if __name__ == "__main__":
    main()