#1288. 새로운 불면증 치료법
T=int(input())
for z in range(T):
    N = int(input())
    cnt = [0]*10
    k=0
    while True :
        if 0 not in cnt:
            break
        k += 1
        New=k*N
        while True :
            if New==0:
                break
            num = New%10
            cnt[num]=1
            New//=10
    print("#{} {}".format(z+1,N*k))
