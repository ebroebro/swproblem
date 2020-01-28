#4831 전기버스

#def electric_bus(K,N,M):
T=int(input())
for z in range(T):
    K,N,M=list(map(int, input().split()))
    charger_list=list(map(int, input().split()))
    charger_station=[0]*(N+1)
    for i in charger_list:
        charger_station[i]=1

    start=0
    cnt=0
    end=K
    while 1:
        zero=0
        for i in range(start+1,end+1):
            if charger_station[i]==1:
                start=i
            else :
                zero+=1
        if zero == K:
            cnt= 0
            break
        cnt+=1
        end=K+start
        if end >=N:
            break
    print("#{} {}".format(z+1,cnt))