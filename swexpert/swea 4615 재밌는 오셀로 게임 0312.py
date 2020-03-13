#4615 재밌는 오셀로 게임
from pprint import pprint


T=int(input())
for z in range(T):
    n,m = list(map(int,input().split()))
    #흑돌 1 -> 0 백돌 2->1
    map_list=[[9 for _ in range(n)] for _ in range(n)]  #빈곳을 9로
    #기본 세팅을 할까?
    map_list[n//2-1][n//2-1]=1
    map_list[n//2][n//2]=1
    map_list[n//2][n//2-1]=0
    map_list[n//2-1][n//2]=0

    # pprint(map_list)
    dy=[1,-1,0,0,1,1,-1,-1]
    dx=[0,0,1,-1,-1,1,-1,1]

    for i in range(m):
        y,x,dol= list(map(int,input().split()))
        dol-=1
        x-=1
        y-=1
        map_list[x][y]=dol
        for j in range(8):
            stack=[]
            newx=x+dx[j]
            newy=y+dy[j]
            if 0<=newx<n and 0<=newy<n and map_list[newx][newy]==1-dol:
                # stack.append([newx,newy])
                while True:
                    if newx<0 or newy<0 or newx>=n or newy>=n or map_list[newx][newy]==9: #빈칸이거나 벗어나면 그냥 끝내기
                        break
                    elif map_list[newx][newy]==1-dol:
                        stack.append([newx,newy])
                        newx+=dx[j]
                        newy+=dy[j]
                    elif map_list[newx][newy]==dol:
                        while stack:
                            tmp=stack.pop()
                            map_list[tmp[0]][tmp[1]]=dol
                        break

    #이제 숫자 세기
    white_cnt=0
    black_cnt=0
    for i in range(n):
        for j in range(n):
            if map_list[i][j]==0:
                black_cnt+=1
            elif map_list[i][j]==1:
                white_cnt+=1

    print("#{} {} {}".format(z+1,black_cnt,white_cnt))