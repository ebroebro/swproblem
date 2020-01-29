#1284 수도요금경쟁
T=int(input())
for z in range(T):
    P, Q, R, S, W=list(map(int,input().split()))
    paya,payb=0,0
    # A사
    paya=W*P
    # B사
    if W<=R :
        payb=Q
    else :
        payb=Q + (W-R)*S
    result= paya if paya<=payb else payb
    print("#{} {}".format(z+1,result))