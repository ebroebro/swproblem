T=int(input())
for z in range(T):
    N=int(input())
    a_list=[]
    b_list=[]
    for i in range(N):
        a,b=list(map(int,input().split()))
        a_list.append(a)
        b_list.append(b)
    P=int(input())
    rslt_list =[]
    for i in range(P):
        c=int(input())
        cnt=0
        for j in range(N):
            if c>=a_list[j] and c<=b_list[j]:
                cnt+=1
        rslt_list.append(cnt)
    print("#{}".format(z+1),end=' ')
    print(*rslt_list)