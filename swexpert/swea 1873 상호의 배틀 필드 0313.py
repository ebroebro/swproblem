#1873 상호의 배틀필드
T=int(input())
for z in range(T):
    h,w=list(map(int,input().split()))
    map_list = [list(input()) for _ in range(h)]
    n=int(input())
    input_list=list(input())
    char=['R','L','U','D']
    change=['>','<','^','v']
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]

    for i in range(h):
        for j in range(w):
            if map_list[i][j] in change:
                x=i
                y=j

    for i in range(n):
        if input_list[i] in char:
            tmp= char.index(input_list[i])
            map_list[x][y]=change[tmp]
            if 0<=x+dx[tmp]<h and 0<=y+dy[tmp]<w and map_list[x+dx[tmp]][y+dy[tmp]]=='.':
                map_list[x][y]='.'
                x=x+dx[tmp]
                y=y+dy[tmp]
                map_list[x][y]=change[tmp]
        elif input_list[i]=='S':
            tmp = change.index(map_list[x][y])
            tmpx=x
            tmpy=y
            while 0<=tmpx<h and 0<=tmpy<w:
                if map_list[tmpx][tmpy] == '#':
                    break
                elif map_list[tmpx][tmpy]=='*':
                    map_list[tmpx][tmpy]='.'
                    break
                else:
                    tmpx+=dx[tmp]
                    tmpy+=dy[tmp]
    print("#{}".format(z+1),end=' ')
    for i in range(h):
        print(''.join(map_list[i]))