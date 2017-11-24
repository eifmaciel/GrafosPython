#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <string>
#include <vector>

#define rep(i,n) for(i=0;i<(n);i++)
#define min(a,b) (((a)<(b))?(a):(b))
#define MAXN 105

int n;
char s[5000];

struct Node {
 int level;
 int low;
 int noChildren;
 vector<int> adj;
}nd[MAXN];

int res;
bool isArtic[MAXN];

vector<string> parse(const string& s,const string& delim=" ") {
 vector<string>res;
 string t;
 for(int i=0;i!=s.size();i++) {
  if(delim.find(s[i]) != string::npos) {
   if(!t.empty()) {
    res.push_back(t);
    t="";
   }
  }
  else t+=s[i];
 }
 if(!t.empty()) res.push_back(t);
 return res;
}

void dfs(int x) {
 nd[x].low = nd[x].level;

 int i, y;
 rep(i, nd[x].adj.size()) {
  y = nd[x].adj[i];
  if( nd[y].level == -1) { //unvisited
   nd[y].level = nd[x].level + 1;
   nd[x].noChildren++;
   dfs(y);
   nd[x].low = min(nd[x].low, nd[y].low);

   if(nd[x].level > 0 && nd[y].low >= nd[x].level) { // x is a non-root node and there's no way from y to any upper level of x
    isArtic[x] = 1;
   }
  }
  else if (nd[y].level < nd[x].level - 1) { //y's depth is lower than x's parent....so its a back edge
   nd[x].low = min(nd[x].low, nd[y].level);
  }
 }

 if(nd[x].level == 0) { //root node
  if(nd[x].noChildren >= 2) isArtic[x] = 1;
 }
}

int main() {
 vector<string> vs;
 int i;
 int u,v;
 
 while(scanf(" %d",&n)==1) {
  if(n == 0) break;
  gets(s); //garbage
  rep(i,n) nd[i].adj.clear(), nd[i].noChildren = 0,  nd[i].low = nd[i].level = -1;
  while(gets(s)) {
   vs = parse(s);
   if(vs.size() == 1 && vs[0] == "0") break;
   u = atoi(vs[0].c_str()) - 1;
   for(i=1;i<vs.size();i++) {
    v = atoi(vs[i].c_str()) - 1;
    nd[u].adj.push_back(v);
    nd[v].adj.push_back(u);
   }
  }

  memset(isArtic, 0, sizeof(isArtic));
  nd[0].level = 0;
  dfs(0);
  res = 0;
  rep(i,n) if(isArtic[i]) res++;
  printf("%d\n",res);
 }
 return 0;
}