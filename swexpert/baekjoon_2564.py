#2564. 경비원
from pprint import pprint

mapy,mapx = list(map(int,input().split())) #가로, mapy 세로 mapx
map_list = [[0 for _ in range(mapy+1)] for _ in range(mapx+1)]

# 줄세우기 ..
for i in range(mapy+1):
    map_list[0][i]=9
    map_list[mapx][i]=9
for i in range(mapx+1):
    map_list[i][0]=9
    map_list[i][mapy]=9

nstore = int(input())


for _ in range(nstore):
    store = list(map(int, input().split()))
    if store[0]==1:
        map_list[mapx][store[1]]=1
    if store[0]==2:
        map_list[0][store[1]]=1
    if store[0]==3:
        map_list[mapx-store[1]][0]=1
    if store[0]==4:
        map_list[mapx- store[1]][mapy]=1

#동근이 위치
pst = list(map(int,input().split()))
if pst[0] == 1:
    map_list[mapx][pst[1]] = 5
    x=mapx
    y=pst[1]
if pst[0] == 2:
    map_list[0][pst[1]] = 5
    x=0
    y=pst[1]
if pst[0] == 3:
    map_list[mapx - pst[1]][0] = 5
    x=mapx-pst[1]
    y=0
if pst[0] == 4:
    map_list[mapx - pst[1]][mapy] = 5
    x=mapx-pst[1]
    y=mapy
# pprint(map_list)
map_list2=map_list
#시계방향
pstx=x
psty=y
dy=[0,1,0,-1]
dx=[-1,0,1,0]
clk=[]  #여기다가 거리 그거 넣을 거임
# print("{} {}".format(dy,dx))
dis=0
while True:
    for i in range(4):
        while True:
            map_list2[pstx][psty]=0
            newY=psty+dy[i]
            newX=pstx+dx[i]
            if 0<=newX<=mapx and 0<=newY<=mapy and map_list2[newX][newY] :
                psty=newY
                pstx=newX
                dis+=1
                # pprint(map_list2)
                # print()
                if map_list2[pstx][psty] ==1: #가게를 만나면
                    clk.append(dis)
            else :
                break
    if dis == 2*(mapx+mapy)-1:
        break
# print(clk)

counterclk=[2*(mapx+mapy)-i for i in clk]

# print(counterclk)

rslt = [ min(counterclk[i],clk[i]) for i in range(len(clk))]

# print(rslt)
print(sum(rslt))