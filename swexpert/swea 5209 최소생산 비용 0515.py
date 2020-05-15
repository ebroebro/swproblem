#5209 최소 생산비용
def backtracking(now,sum):
    global min_sum
    if now == n:
        if min_sum > sum :
            min_sum = sum
        return

    for col in range(n):
        if col not in visited and min_sum >= sum+map_list[now][col]:
            visited.append(col)
            backtracking(now+1,sum+map_list[now][col])
            visited.pop()

t=int(input())
for z in range(t):
    n= int(input())
    map_list = [list(map(int,input().split())) for _ in range(n)]
    visited=[]
    min_sum=987654321
    backtracking(0,0)

    print("#{} {}".format(z+1,min_sum))