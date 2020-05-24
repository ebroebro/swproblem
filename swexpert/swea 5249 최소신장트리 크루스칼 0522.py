#5249 최소 신장 트리 크루스칼
def find_set(a):
    if a == parents[a]:
        return a
    else:
        return find_set(parents[a])

def Union(a,b):
    aroot= find_set(a)
    broot = find_set(b)
    if ranks[aroot] >= ranks[broot]:
        parents[broot]=aroot
    else:
        parents[aroot]=broot
    if ranks[aroot] == ranks[broot]:
        ranks[aroot]+=1

def Spanning_Tree(G):
    mst =[] #최소 신장 트리
    mst_cost = 0 #최소 신장 트리의 가중치

    G.sort(key = lambda x: x[2]) #가중치의 오름차순으로 정렬

    while len(mst) <N-1 and len(G):
        s,e,val = G.pop(0)
        if find_set(s) !=find_set(e): #같은 집합에 속해있지 않다면
            Union(s,e) #각각의 집합을 합친다.
            mst.append((s,e)) #그때의 간선을 mst에 저장
            mst_cost +=val #그때의 가중치를 저장
    return mst_cost

t = int(input())
for z in range(t):
    V,N = map(int, input().split())
    edges=[]
    for i in range(N):
        n1,n2,val = map(int,input().split())
        edges.append((n1,n2,val))
    parents =[i for i in range(N)]
    ranks= [0 for i in range(N)]
    print("#{}".format(z+1),end=' ')
    print(Spanning_Tree(edges))