#1861 정사각형 방
def f(x,y,cnt):
    global maxcnt
    if maxcnt < cnt :
        maxcnt=cnt

    for i in range(4):
        newx=x+dx[i]
        newy=y+dy[i]
        if 0<=newx<n and 0<=newy<n  and map_list[x][y]+1==map_list[newx][newy] :
            f(newx,newy,cnt+1)

T=int(input())
for z in range(T):
    n=int(input())
    map_list=[list(map(int,input().split())) for _ in range(n)]

    dy=[1,0,-1,0]
    dx=[0,1,0,-1]
    rsltcnt=0
    for i in range(n):
        for j in range(n):
            maxcnt=0
            f(i,j,1)
            if maxcnt > rsltcnt:
                rsltcnt=maxcnt
                rslt = map_list[i][j]
            elif maxcnt == rsltcnt and map_list[i][j]<rslt :
                rslt = map_list[i][j]

    print("#{} {} {}".format(z+1,rslt,rsltcnt))
