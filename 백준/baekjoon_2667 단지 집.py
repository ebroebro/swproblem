#2667 단지번호붙이기 집

import sys
sys.stdin=open('input.txt','r')

n= int(input())
map_list =[]
for _ in range(n):
    data = int(input())
    data_list = []
    for _ in range(n):
        data_list.insert(0, data%10)
        data//=10
    map_list.append(data_list)
# print(map_list)

rslt=[]
def DFS(x,y):
    global cnt,map_list
    map_list[x][y]=0
    dy=[0,0,-1,1]
    dx=[1,-1,0,0]
    for i in range(4):
        newX=x+dx[i]
        newY=y+dy[i]
        if 0<=newX<n and 0<=newY<n and map_list[newX][newY]==1:
            # visited.append
            DFS(newX,newY)
            cnt += 1

for x in range(n):
    for y in range(n):
        if map_list[x][y]==1:
            cnt=1
            DFS(x,y)
            if cnt !=0 :
                rslt.append(cnt)

print(len(rslt))
for i in sorted(rslt):
    print(i)