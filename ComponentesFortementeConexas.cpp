#include <stdio.h>

#define N 3

int G[N][N]={{0,1,0},
             {0,0,1},
             {0,0,0}};
int GL[N][N];
int posnum[N]={0,0,0},visit[N]={0,0,0};
int nump=0;

void DFS(int v)
{
visit[v]=1;
int i;
for (i=0;i<N;i++)
   if (G[v][i] && visit[i]==0)
      DFS(i);
nump++;
posnum[v] = nump;
}

void DFS2(int v)
{
visit[v]=2;
int i;
for (i=0;i<N;i++)
   if (GL[v][i] && visit[i]==0)
      DFS2(i);
}

int main() {
	int i,j;
DFS(0);
for (i=0;i<N;i++)
   for (j=0;j<N;j++)
      GL[i][j]=G[j][i];
while (1)
   {
   int maior=-1,pm=0;
   for (i=0;i<N;i++)
     if (posnum[i]>maior && visit[i]==1)
        {
        maior=posnum[i];
		pm=i;
		}
   if (maior==-1) break;
   DFS2(pm);
   for (i=0;i<N;i++)
      if (visit[i]==2)
         {
         printf("%d ",i);
         visit[i]=3;
		 }
   printf("\n");
   }
  return 0;
}
