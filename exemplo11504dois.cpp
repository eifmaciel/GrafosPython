//----------------------------
// LAM PHAN VIET
// UVA 11504 - Dominos
// Time limit: 3.000s
//----------------------------
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <vector>
#include <stack>
using namespace std;

#define For(i, a, b) for (int i=a; i<=b; i++)
#define maxN 100001
int n, Part[maxN], Count;
bool Free[maxN];
vector< vector<int> > adj, radj;
vector<int> Node;

void Init() {
    memset(Free, true, n+1);
    adj = vector< vector<int> >(n+1);
    radj = vector< vector<int> >(n+1);
    Count = 0;
    Node.clear();
}

void DFS1(int u) {
    Free[u] = false;
    for (int i=0, size=adj[u].size(); i<size; i++){
        if (Free[adj[u][i]]) DFS1(adj[u][i]);
    }
    Node.push_back(u);
}

void DFS2(int u, int p) {
    Free[u] = true;
    Part[u] = p;
    for (int i=0, size=radj[u].size(); i<size; i++)
        if (!Free[radj[u][i]]) DFS2(radj[u][i], p);
}

main() {
//    freopen("504.inp", "r", stdin); freopen("504.out", "w", stdout);
    int Case, m, u, v;
    scanf("%d", &Case);
    while (Case--) {
        scanf("%d %d", &n, &m);
        Init();
        while (m--) {
            scanf("%d %d", &u, &v);
            adj[u].push_back(v);
            radj[v].push_back(u);
        }
        For (i, 1, n)
            if (Free[i]) DFS1(i);
        int nPart = 0;
        for (int i=Node.size()-1; i>=0; i--)
            if (!Free[Node[i]]) {
                DFS2(Node[i], ++nPart);
            }
        bool Com[nPart+1];
        memset(Com, true, nPart+1);
        for(int i=0;i<n;i++){
            for(int j=0;j<adj[i].size();j++){
                printf("c%d%d =  %d\n", i, j, adj[i][j]);
            }
        }
        For (u, 1, n)
            for (int i=0, size=adj[u].size(); i<size; i++) {
                int v = adj[u][i];
                printf("v %d\n", v);
                printf("Part[u] %d Part[v] %d\n", Part[u], Part[v]);
                if (Part[u]!=Part[v]) Com[Part[v]] = false;
            }
        int ans = 0;
        For (i, 1, nPart)
            if (Com[i]) ans++;
        printf("%d\n", ans);
    }
}
