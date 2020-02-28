#1486 장훈이의 높은 선반 다시 해보기
def dfs(position):
    global sum, min
    if sum >= b and sum -b < min :
        min = sum-b
        return
    for i in range(position,n):
        if visited[i]==0 and sum +data_list[i] - b <min:
            sum+=data_list[i]
            visited[i]=1
            dfs(i)
            visited[i]=0
            sum-=data_list[i]


T=int(input())
for z in range(T):
    n, b = list(map(int,input().split()))  #n 사람 수  b기준값
    data_list = list(map(int,input().split()))

    min=987654321
    sum=0
    visited=[0]*n

    dfs(0)
    print("#{} {}".format(z+1,min))