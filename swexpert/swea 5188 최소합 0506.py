#5188 최소합

def f(x,y,sum):
    global min_sum
    if x == n-1 and y == n-1:
        if min_sum > sum :
            min_sum=sum
        return
    for j in range(2):
        newx=x+dx[j]
        newy=y+dy[j]
        if 0<=newx<n and 0<=newy<n and sum+map_list[newx][newy] < min_sum:
            f(newx,newy,sum+map_list[newx][newy])

T= int(input())
for z in range(T):
    n= int(input())
    map_list=[]
    for i in range(n):
        tmp_list=list(map(int,input().split()))
        map_list.append(tmp_list)

    dx=[0,1]
    dy=[1,0]
    min_sum=987654321

    f(0,0,map_list[0][0])

    print("#{} {}".format(z+1,min_sum))