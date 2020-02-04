#1954 달팽이 숫자
from pprint import pprint

def snail_num(data_map):
    num=0
    a=0
    b=0
    while True:
        ##오른쪽
        while True:
            num += 1
            data_map[a][b]=num
            b+=1
            if (bool(data_map[a][b])) or b>n-1:
                num-=1
                b-=1
                break
        ##아래
        while True:
            num += 1
            data_map[a][b]=num
            a+=1
            if (bool(data_map[a][b])) or a>n-1:
                num-=1
                a-=1
                break
        #왼쪽
        while True:
            num += 1
            data_map[a][b]=num
            b-=1
            if (bool(data_map[a][b])) or b<0:
                num-=1
                b+=1
                break
        #위로
        while True:
            num += 1
            data_map[a][b]=num
            a-=1
            if (bool(data_map[a][b])) or a<0:
                num-=1
                a+=1
                break
        if num==n**2-1:
            break

    rslt=''
    for i in range(n):
        rslt+=' '.join(list(map(str,data_map[i][:n])))+'\n'

    return rslt

T=int(input())
for z in range(T):
    n= int(input())
    data_map = [[0]*(n+1) for i in range(n+1)]
    print("#{}".format(z+1))
    print(snail_num(data_map),end="")
