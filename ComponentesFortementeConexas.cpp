#include <stdio.h>


int G[100][100];
int GL[100][100];
int posnum[100], visit[100];
int nump=0;
int N = 0;

void DFS(int v){
    visit[v]=1;
    int i;
    for (i=0;i<N;i++)
       if (G[v][i] && visit[i]==0)
          DFS(i);
    nump++;
    posnum[v] = nump;
}

void DFS2(int v) {
    visit[v]=2;
    int i;
    for (i=0;i<N;i++){
        if (GL[v][i] && visit[i]==0){
            DFS2(i);
        }
    }
}

int main() {
	int i,j;
    int Case, n, m, u, v, soma;
    scanf("%d", &Case);
    while (Case--) {
        scanf("%d %d", &n, &m);
        N = n;

        while (m--) {
            scanf("%d %d", &u, &v);
            G[u][v] = 1;
        }
        DFS(0);
        for (i=0;i<N;i++){
            for (j=0;j<N;j++){
                GL[i][j]=G[j][i];
            }
        }
        while (1){
            int maior=-1,pm=0;
            for (int i=0;i<N;i++){
                if (posnum[i]>maior && visit[i]==1){
                    maior=posnum[i];
                    pm=i;
                }
            }
            if (maior==-1){
               break;
            }
            DFS2(pm);
            soma = 0;
            for (int i=0;i<N;i++){
                if (visit[i]==2){
                    soma++;
                    visit[i]=3;
        		}
            }
            printf("\n");
        }
        printf("%d ",soma);
    }

    return 0;
}
