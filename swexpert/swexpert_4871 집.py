#4871 그래프 경로
def DFS(here):
    global isOkay, visited, G
    visited.append(here)
    if here == G:
        isOkay = 1
        return
    for i in range(V + 1):
        if (map_list[here][i]) and (i not in visited):
            DFS(i)

T=int(input())
for z in range(T):
    V,E = list(map(int,input().split())) #V 노드 수 E 간선 수
    map_list = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for _ in range(E):
        start,stop = list(map(int, input().split()))
        map_list[start][stop]=1
    S,G = list(map(int,input().split()))
    visited=[]
    isOkay=0
    DFS(S)
    print("#{} {}".format(z+1,isOkay))
