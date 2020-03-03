#1865 동철이의 일분배
n=int(input())
map_list=[list(map(int,input().split())) for _ in range(n)]
maxP=0
visited=[]

def f(people, percent,k):
    global maxP
    if people ==k:
        if maxP < percent:
            maxP=percent
        return
    else:
        for j in range(n):
            if j not in visited and map_list[people][j]:
                percent*=map_list[people][j]/100
                visited.append(j)
                f(people+1,percent,k)
                visited.pop()
                percent/=map_list[people][j]/100

f(0,0,n)
print(round(maxP*100,7))
