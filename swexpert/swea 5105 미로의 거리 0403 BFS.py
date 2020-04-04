#5105 미로의 거리  BFS로 풀기
from pprint import pprint

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


    visited=[[0 for _ in range(n)] for _ in range(n)]
    visited[startx][starty]=1
    dy=[1,-1,0,0]
    dx=[0,0,1,-1]
    rslt=-1
    queue=[[startx,starty]]
    while queue:
        tmp = queue.pop(0)
        for i in range(4):
            newx=tmp[0]+dx[i]
            newy=tmp[1]+dy[i]
            if 0<=newx<n and 0<=newy<n and visited[newx][newy]==0 and map_list[newx][newy]!=1:
                queue.append([newx,newy])
                visited[newx][newy]=visited[tmp[0]][tmp[1]]+1
                if map_list[newx][newy]==3:
                    rslt=visited[newx][newy]
                    break
        if rslt >0:
            break

    # pprint(visited)
    print("#{}".format(z+1), end=' ')
    if rslt <0 :
        print(0)
    else:
        print(rslt-2)