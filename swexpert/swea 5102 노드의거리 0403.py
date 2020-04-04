#5102 노드의 거리 BFS
from pprint import pprint
T=int(input())
for z in range(T):
    v,e = list(map(int,input().split()))
    map_list=[[0 for i in range(v+1)] for _ in range(v+1)]
    for i in range(e):
        a,b = list(map(int,input().split()))
        map_list[a][b]=1
        map_list[b][a]=1
    s,g=list(map(int,input().split()))
    visited=[0 for _ in range(v+1)]
    visited[s]=1
    queue=[s]
    cnt=0
    rslt=-1

    while queue:
        tmp=queue.pop(0)
        for i in range(v+1):
            if map_list[tmp][i] ==1 and visited[i]==0:
                visited[i]=visited[tmp]+1
                queue.append(i)
            if i == g :
                rslt=visited[i]
        if rslt >0:
            break
    if rslt>0:
        rslt-=1
    else:
        rslt=0

    print("#{} {}".format(z+1,rslt))
