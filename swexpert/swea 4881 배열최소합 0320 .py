#4881 배열 최소합
def f(post,sum):
    global min_sum
    if post ==n:
        if min_sum > sum:
            min_sum = sum
            return
    for i in range(n):
        if i not in visited and sum+map_list[post][i]<min_sum:
            visited.append(i)
            f(post+1,sum+map_list[post][i])
            visited.pop()
T=int(input())
for z in range(T):
    n=int(input())
    map_list=[list(map(int,input().split())) for _ in range(n)]
    min_sum=987654321
    visited=[]
    f(0,0)
    print("#{} {}".format(z+1,min_sum))