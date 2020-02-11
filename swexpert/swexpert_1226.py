#1226. 미로1
from pprint import pprint

map_list= []
for i in range(16):
    data_list=[]
    data=int(input())
    for j in range(16):
        data_list.insert(0,data%10)
        data//=10
    map_list.append(data_list)
    if data_list.count(2):
        startx=i
        starty=data_list.index(2)
    if data_list.count(3):
        endx=i
        endy=data_list.index(3)
# pprint(map_list)

dy=[1,-1,0,0]
dx=[0,0,1,-1]
herex=startx
herey=starty
cnt=0
def findmap(herex,herey):
    global cnt, dy,dx,map_list

    for i in range(4):
        nextx=herex+dx[i]
        nexty=herey+dy[i]
        if nextx==endx and nexty==endy:
            cnt = 1
            return
        elif map_list[nextx][nexty]!=1:

            herex=nextx
            herey=nexty
            map_list[herex][herey] = 1
            findmap(herex, herey)
    return

findmap(herex,herey)
print(cnt)
