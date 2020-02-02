#1976 시각덧셈
T=int(input())
for z in range(T):
    t1,m1,t2,m2 = list(map(int, input().split()))
    t,m=0,0
    t=t1+t2
    m=m1+m2
    if m>=60:
        m-=60
        t+=1
    if t>12:
        t-=12
    print("#{} {} {}".format(z+1,t,m))