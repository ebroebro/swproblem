#2814 최장경로
def f(post,cnt):
    global max_cnt
    if max_cnt <cnt :
        max_cnt = cnt
    for i in range(1,n+1):
        if map_list[post][i]==1 and i not in visited:
            visited.append(i)
            f(i,cnt+1)
            visited.pop()
T=int(input())
for z in range(T):
    n,m=list(map(int,input().split()))
    map_list=[[0 for _ in range(n+1)] for _ in range(n+1)]
    max_cnt=0
    for _ in range(m):
        a,b=list(map(int,input().split()))
        map_list[a][b]=1
        map_list[b][a]=1

    for j in range(1,n+1):
        visited=[j]
        f(j,1)

    print("#{} {}".format(z+1,max_cnt))