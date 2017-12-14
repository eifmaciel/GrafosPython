#include <stdio.h>


int G[100][100];
int GL[100][100];
int posnum[100], visit[100], Part[100];
int nump=0;
int N = 0;

void Init() {
    visit, true, n+1);
    adj = vector< vector<int> >(n+1);
    radj = vector< vector<int> >(n+1);
    Count = 0;
    Node.clear();
}

void DFS(int v){
    visit[v]=1;
    for(int i=0, i<sizeof(adj[u]); i++){
        if (visit[adj[u][i]]) DFS(adj[u][i]);
        }
    }
    nump++;
    posnum[v] = v;
}

void DFS2(int v, int p) {
    visit[v]=2;
    Part[v] = p;
    int i;
    for (i=0;i<N;i++){
        if (!visit[GL[v][i]]){
            DFS2(GL[v][i], p);
        }
    }
}

int main() {
	int i,j;
    int Case = 0 , n = 0, m = 0, u = 0, v = 0, soma = 0;
    int result[50], pos = 0;
    scanf("%d", &Case);
    while (Case--) {
        scanf("%d %d", &n, &m);
        N = n;

        while (m--) {
            scanf("%d %d", &u, &v);
            G[u][v] = 1;
        }
        for(int i=1; i<=N; i++){
            if(!visit[i]){
                DFS(i);
            }
        }
        for (i=0;i<N;i++){
            for (j=0;j<N;j++){
                GL[i][j]=G[j][i];
            }
        }
        int nPart = 0;
        for (int i=nump; i>=0; i--){
            if (!visit[posnum[i]]) {
                DFS2(posnum[i], ++nPart);
            }
        }
        int Com[nPart+1];
        for(i=0; i<nPart; i++){
            Com[i] = 1;
        }
        for(int u=1; u<=N; u++){
            for (int i=0; i<N; i++) {
                int v = G[u][i];
                if (Part[u]!=Part[v]){
                    Com[Part[v]] = 0;
                }
            }
        }
        int ans = 0;
        for (i=1; i<=nPart; i++){
            if (Com[i]) ans++;
        }
        printf("%d\n", ans);
    }


    return 0;
}
