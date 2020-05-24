#5249 최소 신장 트리 프림
def Dijkstra(G,s,N):
    minW=[float('inf') for i in range(N)]
    parents = [None for i in range(N)]
    visited = [0 for i in range(N)]
    minW[s]=0

    for i in range(N):
        minidx, minval = -1, float('inf')
        for j in range(N):
            if not visited[j] and minW[j] <minval :
                minval = minW[j]
                minidx = j
        visited[minidx] =1
        for v, val in G[minidx]:
            print(minW)
            print(v)
            if len(minW) > v and not visited[v] and val < minW[v]:
                minW[v] = val
                parents[v] = minidx
    return sum(minW)

# t = int(input())
# for z in range(t):
N,E = map(int, input().split())
edges=[]
for i in range(E):
    n1,n2,val = map(int,input().split())
    edges.append((n1,n2,val))
graph= dict()
for edge in edges :
    s, e,val = edge
    if graph.get(s):
        graph[s].append((e,val))
    else:
        graph[s] =[(e,val)]

# print("#{}".format(z+1),end=' ')
print(Dijkstra(graph,0,N))