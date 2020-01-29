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
        for i in range(start+1,end+1): #이렇게 해도 되는 이유...
            if charger_station[i]==1: #앞에 존재해도 뒤에있으면 그것때문에 값이 바뀌기 때문에 뒤에 있는 정류장값만 남음..
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