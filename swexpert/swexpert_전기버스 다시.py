#전기버스 다시
import sys
sys.stdin = open('input.txt','r')

T=int(input())
for z in range(T):
    K,N,M = list(map(int,input().split())) #M 충전기 개수
    charge_node = list(map(int,input().split()))
    node = [0 for _ in range(N+1)]
    for i in charge_node:
        node[i]=1
    life=K
    here=0
    cnt=0
    while True :
        if here +K>=N:
            rslt=cnt
            break
        if life==0:
            rslt=0
            break
        for i in range(K,-1,-1):
            if here+K>=N:
                rslt=cnt
                break
            if life==0:
                rslt=0
                break

            life-=1
            if here+i<=N and node[here+i]==1:
                here=here+i
                if here==N:
                    rslt=cnt
                    break
                life=K
                cnt+=1
                break
        else:
            here+=1
    print("#{} {}".format(z+1,rslt))
