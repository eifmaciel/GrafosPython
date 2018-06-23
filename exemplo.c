#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define O 1000


int mat[100][100], n;
int depth[100], lowpt[100];
int visited[100], cont;

int DFS(int no, int d, int pai) {
	int i, back = O, child = 0, tmp, flag = 0;
 	
 	depth[no] = d;
 	
 	for(i = 1; i <= n; i++) {
  		if(mat[no][i] == 1) {
   			if(visited[i] == 0) {
    			visited[i] = 1;
    			tmp = DFS(i, d+1, no);
    			if(tmp >= d) flag = 1;
    			if (back > tmp){
    				back = tmp;
    			}
    			child ++;
   			}  else {
    			if(i != pai){
    				if (back > depth[i] ){
     					back = depth[i];
     				}
     			}
   			}
  		}
 	}
 	lowpt[no] = back;
 	if(no == 1) {
  		if(child > 1){
   			cont++;
   		}
 	} else {
  		cont += flag;
 	}
 	return lowpt[no];
}


int main() {
	int x, y;
	char c;
	while(scanf("%d", &n) == 1 && n) {
		memset(mat, 0, sizeof(mat));
		memset(depth, 0, sizeof(depth));
		memset(lowpt, 0, sizeof(lowpt));
		memset(visited, 0, sizeof(visited));

		while(scanf("%d", &x) == 1 && x) {
			while(scanf("%d%c", &y, &c) == 2) {
				mat[x][y] = 1;
				mat[y][x] = 1;
				if(c == '\n'){
					break;
				}
			}
		}
		visited[1] = 1;
		cont = 0;
		DFS(1, 1, 0);
		printf("%d\n", cont);
	}
    return 0;
}

