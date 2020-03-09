T=int(input())
for z in range(T):
    n,m=list(map(int,input().split()))
    sports=list(map(int,input().split()))
    people=list(map(int,input().split()))
    check_list=[0 for i in range(n)]

    max_cnt=0
    rslt=0
    for i in range(m):
        for j in range(n-1,-1,-1):
            if sports[j] <=people[i]:
                tmp=j
        check_list[tmp]+=1
        if check_list[tmp]>max_cnt:
            max_cnt=check_list[tmp]
            rslt=tmp+1

    print("#{} {}".format(z+1,rslt))
