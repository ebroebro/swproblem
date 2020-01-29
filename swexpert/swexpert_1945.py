#1945. 간단한 소인수분해
T=int(input())
for z in range(T):
    a,b,c,d,e=0,0,0,0,0
    N=int(input())
    while True:
        if N%2:
            break
        N//=2
        a+=1

    while True:
        if N%3:
            break
        N//=3
        b+=1

    while True:
        if N%5:
            break
        N//=5
        c+=1

    while True:
        if N%7:
            break
        N//=7
        d+=1

    while True:
        if N % 11:
            break
        N //= 11
        e += 1

    print("#{} {} {} {} {} {}".format(z+1,a,b,c,d,e))