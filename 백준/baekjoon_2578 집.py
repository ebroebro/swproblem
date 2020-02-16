#2578. 빙고
from pprint import pprint

map_list=[]
for _ in range(5):
    map_list.append(list(map(int,input().split())))
check_list=[]
for _ in range(5):
    check_list.extend(list(map(int,input().split())))
# pprint(map_list)
# print(check_list)
for num in check_list:
    for i in range(5):
        if map_list[i].count(num):
            map_list[i][map_list[i].index(num)]=0
            break
    total=0
    #가로
    for i in range(5):
        if map_list[i].count(0)==5:
            total+=1
    #세로
    for j in range(5):
        cnt=0
        for i in range(5):
            if map_list[i][j]==0:
                cnt+=1
        if cnt ==5:
            total+=1
    #대각선
    cnt1,cnt2=0,0
    for i in range(5):
        if map_list[i][i]==0:
            cnt1+=1
        if map_list[i][4-i]==0:
            cnt2+=1
    if cnt1 ==5:
        total+=1
    if cnt2==5:
        total+=1

    #빙고
    if total >=3:
        print(check_list.index(num)+1)
        break