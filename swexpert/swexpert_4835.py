#swexpert_4835 구간합
T=int(input())
for z in range(T):
    N,M = list(map(int,input().split()))
    num = list(map(int,input().split()))
    max,min=0,10000*M
    for i in range(len(num)-M+1):
        sum=0
        for j in range(M):
            sum+=num[i+j]
        if sum>max:
            max=sum
        if sum<min:
            min=sum
    print("#{} {}".format(z+1,max-min))