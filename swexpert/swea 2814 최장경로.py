#2814 최장경로


def DFS(here):
    global max
    visited.append(here)
    if max <len(visited):
        max=len(visited)
        # print(visited)
    for i in range(1,n+1):
        if map_list[here][i] and i not in visited:
            DFS(i)
            visited.pop()


T=int(input())
for z in range(T):
    n,m = list(map(int,input().split()))
    map_list=[[0 for _ in range(n+1)] for _ in range(n+1)]
    for _ in range(m):
        x,y = list(map(int,input().split()))
        map_list[x][y]=1
        map_list[y][x]=1

    check = list(range(1,n+1))
    visited=[]
    max=0
    #시작점을 달리하면서
    for i in check:
        DFS(i)
        visited=[]

    print("#{} {}".format(z+1,max))