#5102 노드의 거리_dfs
from pprint import pprint
def f(a):
    global cnt,min_rslt
    if a==g:
        if min_rslt > cnt:
            min_rslt=cnt

        return
    for i in range(v+1):
        if map_list[a][i]==1 and i not in visited and cnt < min_rslt:
            visited.append(i)
            cnt+=1
            f(i)
            visited.pop()
            cnt-=1

T=int(input())
for z in range(T):
    v,e = list(map(int,input().split()))
    map_list=[[0 for i in range(v+1)] for _ in range(v+1)]
    for i in range(e):
        a,b = list(map(int,input().split()))
        map_list[a][b]=1
        map_list[b][a]=1
    s,g=list(map(int,input().split()))
    visited=[s]
    cnt=0
    min_rslt=987654321

    f(s)
    if min_rslt==987654321:
        min_rslt=0
    print("#{} {}".format(z+1,min_rslt))