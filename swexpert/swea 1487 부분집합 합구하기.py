def f(idx,sum):
    global cnt
    if idx == n:
        if sum == w:
            cnt+=1
        return
    if sum+data_list[idx] <=w:
        f(idx+1,sum+data_list[idx])
    f(idx+1,sum)


T=int(input())
for z in range(T):
    n,w = list(map(int,input().split()))
    data_list=list(map(int,input().split()))
    cnt=0
    f(0,0)
    print("#{} {}".format(z+1,cnt))