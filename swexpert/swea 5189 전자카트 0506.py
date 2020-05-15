#5189 전자카트

def f(start,sum):
    global min_sum
    if len(visited) == n:
        if min_sum >sum+map_list[start][0]:
            min_sum=sum+map_list[start][0]
        return

    for k in range(n):
        if map_list[start][k] and k not in visited and min_sum>sum+map_list[start][k]:
            visited.append(k)
            f(k,sum+map_list[start][k])
            visited.pop()


T= int(input())
for z in range(T):
    n= int(input())
    map_list=[]
    for i in range(n):
        tmp_list=list(map(int,input().split()))
        map_list.append(tmp_list)
    min_sum=987654321


    visited=[0]
    f(0,0)

    print("#{} {}".format(z+1,min_sum))