#5688 세제곱근을 찾아라.
T=int(input())
for z in range(T):
    n=int(input())
    post=1
    while True:
        if post*post*post >n:
            rslt=-1
            break
        elif post*post*post ==n:
            rslt=post
            break
        post+=1
    print("#{} {}".format(z+1,rslt))
