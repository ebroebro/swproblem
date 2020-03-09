T=int(input())
for z in range(T):
    p,a,b= list(map(int,input().split()))
    cnta=0
    cntb=0

    last=p
    start=1
    c=int((start+last)/2)
    while True:
        if a==c:
            break
        elif a > c:
            start=c
        else:
            last=c
        c=int((start+last)/2)
        cnta+=1

    last=p
    start=1
    c=int((start+last)/2)
    while True:
        if b==c:
            break
        elif b > c:
            start=c
        else:
            last=c
        c=int((start+last)/2)
        cntb+=1

    print("#{}".format(z+1),end=' ')
    if cnta <cntb:
        print('A')
    elif cnta >cntb:
        print('B')
    else:
        print('0')