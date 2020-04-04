from sys import stdin

# bfs로 각 조합 경우 별 걸리는 시간 판단
def bfs(virus_tmp):
    global min_rslt
    visited=[[-1 for _ in range(n)] for _ in range(n)]
    queue=virus_tmp
    for i in range(m):
        visited[queue[i][0]][queue[i][1]] = 0
    while queue:
        tmp=queue.pop(0)
        for i in range(4):
            newx=tmp[0]+dx[i]
            newy=tmp[1]+dy[i]
            if 0<=newx<n and 0<=newy<n and visited[newx][newy]==-1 and map_list[newx][newy]!=1:
                visited[newx][newy]=visited[tmp[0]][tmp[1]]+1
                queue.append([newx,newy])
        cnt=0
        max_second=0
        for j in range(n):
            for k in range(n):
                if visited[j][k]>max_second:
                    max_second=visited[j][k]
                if visited[j][k]==-1:
                    cnt+=1
        if cnt==wall:
            if max_second < min_rslt:
                min_rslt=max_second
            break


#dfs로 조합 만들어내기
def dfs(virus_tmp,k):
    if k > len(virus):
        return
    if len(virus_tmp) ==m:
        bfs(virus_tmp)
        return
    elif k < len(virus):
        dfs(virus_tmp+[virus[k]],k+1)
        dfs(virus_tmp,k+1)



n,m = list(map(int,stdin.readline().split()))
map_list=[list(map(int,stdin.readline().split())) for _ in range(n)]
virus=[]
min_rslt=987654321
wall=0
for i in range(n):
    for j in range(n):
        if map_list[i][j]==2:
            virus.append([i,j])
        if map_list[i][j]==1:
            wall+=1

dx=[1,-1,0,0]
dy=[0,0,1,-1]

virus_tmp=[]
dfs(virus_tmp,0)
if min_rslt==987654321:
    min_rslt=-1

print(min_rslt)