def f(idx,num,sum):
    global cnt
    if num ==n:
        if sum==k:
            cnt+=1
        return
    elif idx==12:
        return
    else:
        if sum+number_list[idx] <=k:
            f(idx+1,num+1,sum+number_list[idx])
        f(idx+1,num,sum)

T=int(input())
for z in range(T):
    n,k = list(map(int,input().split()))
    number_list=[i for i in range(1,13)]
    cnt=0
    f(0,0,0)
    print("#{} {}".format(z+1,cnt))