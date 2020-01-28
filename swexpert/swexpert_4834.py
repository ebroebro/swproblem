#4834 숫자카드
T=int(input())
for z in range(T):
    N=int(input())
    num=int(input())
    cnt=[0]*10
    for i in range(N):
        cnt[num%10]+=1
        num//=10
    max=0
    idx=0
    for i in range(10):
        if max < cnt[i]:
            max=cnt[i]
            idx=i
        elif max ==cnt[i]:
            if i > idx :
                idx=i
    print("#{} {} {}".format(z+1,idx, max))