#3143 가장 빠른 문자열 타이핑
T=int(input())
for z in range(T):
    A,B= input().split()
    post=0
    cnt=0
    while True:
        if post>=len(A):
            break
        else:
            if post+len(B)<=len(A) and A[post:post+len(B)]==B:
                post+=len(B)
                cnt+=1
            else:
                post+=1
                cnt+=1
    print("#{} {}".format(z+1,cnt))