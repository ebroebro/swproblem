#2819 격자판에 숫자붙이기
def f(x,y,n,tmp):
    global cnt
    if n==6:
        if tmp not in rslt:
            rslt.append(tmp)
            cnt+=1
        return
    for i in range(4):
        newX=dx[i]+x
        newY=dy[i]+y
        if 0<=newX<4 and 0<=newY<4:
            f(newX,newY,n+1,tmp+str(map_list[newX][newY]))

T=int(input())
for z in range(T):
    map_list=[list(map(int,input().split())) for _ in range(4)]
    # print(map_list)
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]
    rslt =[]
    cnt=0

    for i in range(4):
        for j in range(4):
            tmp=str(map_list[i][j])
            f(i,j,0,tmp)
    # print(rslt)
    print("#{} {}".format(z+1,cnt))