#2072 홀수만 더하기
T= int(input())
for z in range(T):
    sum=0
    nums=list(map(int,input().split()))
    for i in nums:
        if i%2:
            sum+=i
    print("#{} {}".format(z+1,sum))