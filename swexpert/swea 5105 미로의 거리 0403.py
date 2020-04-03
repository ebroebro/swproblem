#5105 미로의 거리
from pprint import pprint
def f(x,y):
    global rslt,cnt
    if map_list[x][y]==3:
        rslt+=cnt
        return
    for i in range(4):
        newx=x+dx[i]
        newy=y+dy[i]
        if 0<=newx<n and 0<=newy<n and [newx,newy] not in visited and map_list[newx][newy]!=1:
            visited.append([newx,newy])
            cnt+=1
            f(newx,newy)
            cnt-=1
            visited.pop()



T=int(input())
for z in range(T):
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
    cnt=0
    dy=[1,-1,0,0]
    dx=[0,0,1,-1]

    rslt=-1


    f(startx,starty)
    print("#{}".format(z+1), end=' ')
    if rslt <0 :
        print(0)
    else:
        print(rslt)