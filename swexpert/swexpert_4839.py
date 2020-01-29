#4839 이진탐색
T=int(input())
for z in range(T):
    P,Pa,Pb=list(map(int, input().split()))
    cnta,cntb=0,0

    #A페이지 찾기
    l,r=1,P
    while True:
        c=int((l+r)/2)
        if Pa == c:
            break
        elif Pa > c:
            l= c
        elif Pa < c:
            r=c
        cnta+=1

    #B페이지 찾기
    l,r=1,P
    while True:
        c=int((l+r)/2)
        if Pb == c:
            break
        elif Pb > c:
            l= c
        elif Pb < c:
            r=c
        cntb+=1
    #승자 판단
    if cntb > cnta:
        result = 'A'
    elif cntb < cnta:
        result ='B'
    elif cnta==cntb:
        result = '0'
    print("#{} {}".format(z+1,result))