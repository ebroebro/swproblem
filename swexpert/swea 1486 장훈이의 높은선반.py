#1486 장훈이의 높은 선반
def backtracking(position):
    global sum,min
    if sum >=b and sum-b <min :
        min = sum -b
        return
    for i in range(position,n):
        if visited[i]==0 and sum+data_list[i]-b <= min:
            sum+=data_list[i]
            visited[i]=1
            backtracking(i)
            visited[i]=0
            sum-=data_list[i]

T=int(input())
for z in range(T):
    n, b = list(map(int,input().split()))  #n 사람 수  b기준값
    data_list = list(map(int,input().split()))
    visited = [0]*n  #같은 것도 있기 때문에.. 이렇게 해야해
    sum =0
    min=987654321  #sum이 b 이상인것 중 그 차이가 가장 작아야해
    backtracking(0)
    print("#{} {}".format(z+1,min))