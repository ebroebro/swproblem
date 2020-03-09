T=int(input())
for z in range(T):
    n,m = list(map(int,input().split()))
    a_list = list(map(int,input().split()))
    b_list = list(map(int,input().split()))
    if n>m:
        a_list,b_list = b_list,a_list
        n,m=m,n
    #짧은게 a_list 긴게 b_list
    sum_max=0
    for j in range(m-n+1):
        sum=0
        for i in range(n):
            sum+=a_list[i]*b_list[i+j]
        if sum >sum_max:
            sum_max=sum
    print("#{} {}".format(z+1,sum_max))