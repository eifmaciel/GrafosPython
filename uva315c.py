# -*- coding: utf-8 -*-


link =[
[0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0], 
]

n = 7
depth = [0,0,0,0,0,0, 0]
low = [0,0,0,0,0, 0, 0]
used = [0,0,0,0,0,0, 0]
cut = 0

def DFS(node, d, parent):
    i = 1000
    back = 1000
    son = 0
    tmp = 0
    flag = 0
    global used, cut, link, n
    # import ipdb; ipdb.set_trace()
    
    depth[node] = d
    for i in range(n):
        if(link[node][i] == 1):
            if(used[i] == 0):
                used[i] = 1
                tmp = DFS(i, d+1, node)
                if(tmp >= d):
                    flag = 1
                if back < tmp:
                    back = back
                else:
                    back = tmp
                son+=1
            else:
                if(i != parent):
                    if back < depth[i]:
                        back = back
                    else:
                        depth[i]

    low[node] = back
    if(node == 1):
        if(son > 1):
            cut +=1
    else:
        cut += flag
    return low[node]


def main():
    x = 0
    y = 0
    c = 0
    global used, cut, link, n, depth, low
        

    import sys
    sys.stdin = open('arquivo.txt')
    while True:
        n = input()
        if not n:
            break
        num = n+1
        depth = [0] * num
        low = [0] * num
        used = [0] * num
        cut = 0
        link =[]
        for x in range(n):
            line = raw_input()
            if line == '0':
                break
            a = map(int, line.split())
            k = a[0]
            
            for v in a[1:]:
                link.append([0]*num)
                link[k][v] = 1
                link[v][k] = 1
                print link

        used[1] = 1
        cut = 0
        DFS(1, 1, 0)
        print cut
    # return 0


if __name__ == "__main__":
     main()