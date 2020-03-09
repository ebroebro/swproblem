T=int(input())
for z in range(T):
    k,n,m = list(map(int,input().split()))
    flag = 0
    chargers = list(map(int,input().split()))
    post = [0 for i in range(n+1)]
    for i in range(len(post)):
        if i in chargers:
            post[i]=9
    cnt=0
    start=0
    while True:
        if start >=n:
            flag=cnt
            break
        for i in range(k,-1,-1):
            if start+i >=n:
                start=start+i
                break
            elif post[start+i]==9:
                start=start+i
                cnt+=1
                break
            elif i ==0:
                break
        if i ==0:
            break
    print("#{} {}".format(z+1,flag))