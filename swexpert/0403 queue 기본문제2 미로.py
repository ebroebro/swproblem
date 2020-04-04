#0403 queue를 이용한 bfs
from pprint import pprint

n=int(input())
map_list=[]
for i in range(n):
    tmp_list=[]
    tmp=int(input())
    for j in range(n):
        tmp_list.insert(0,tmp%10)
        tmp//=10
    map_list.append(tmp_list)
for i in range(n):
    for j in range(n):
        if map_list[i][j]==2:
            startx=i
            starty=j
visited=[[startx,starty]]
queue=[[startx,starty]]
cnt=0
dy=[1,-1,0,0]
dx=[0,0,1,-1]

while queue:
    tmp = queue.pop(0)
    for i in range(4):
        newx=tmp[0]+dx[i]
        newy=tmp[1]+dy[i]
        if 0<=newx<n and 0<=newy<n and [newx,newy] not in visited and map_list[newx][newy]!=1:
            queue.append([newx,newy])
            visited.append([newx,newy])

print(visited)