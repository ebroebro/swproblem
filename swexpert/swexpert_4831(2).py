def check_charge(K,N,M,charger_num):
    charger_station = [0]*(N+1)
    for i in charger_num: # 충전기 정류소 저장
        charger_station[i]=1

    start = 0 #시작점 바뀔때 마다 reset 되게 만들자.
    end = K #시작점과 대비해 어디까지 가야하는지 보기!
    cnt=0
    while end <N : #마지막 정류장 도착 전까지 돌리겠음
        life = K  # 하나 움직일때마다 life가 하나씩 줄어든다?!
        for i in range(end, start,-1):
            if charger_station[i]==1:
                start=i
                end=start+K
                cnt+=1
                break
            else :
                life-=1
        if life ==0 :
            cnt=0
            break
    return cnt

T=int(input())
for i in range(T):
    K,N,M = list(map(int, input().split()))
    charger_num = list(map(int, input().split()))
    print("#{} {}".format(i+1,check_charge(K,N,M,charger_num)))