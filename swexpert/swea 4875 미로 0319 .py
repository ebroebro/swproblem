#4875 미로
def f(x,y):
    global flag
    if flag==1:
        return
    for i in range(4):
        newx=x+dx[i]
        newy=y+dy[i]
        if 0<=newx<n and 0<=newy<n:
            if map_list[newx][newy]==2:
                flag=1
                return
            elif map_list[newx][newy]==0:
                map_list[newx][newy]=9
                f(newx,newy)
                map_list[newx][newy]=0
T=int(input())
for z in range(T):
    n=int(input())
    map_list=[]
    flag=0
    for _ in range(n):
        data_list=[]
        tmp=int(input())
        for _ in range(n):
            data_list.insert(0,tmp%10)
            tmp//=10
        map_list.append(data_list)
    for i in range(n):
        for j in range(n):
            if map_list[i][j]==3:
                start_x=i
                start_y=j

    dy=[0,1,-1,0]
    dx=[1,0,0,-1]

    f(start_x,start_y)
    print("#{} {}".format(z+1,flag))