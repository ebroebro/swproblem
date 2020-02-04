#1859. 백만 장자 프로젝트 (이게 .. 진짜 답. )
T=int(input())
for z in range(T):
    n=int(input())
    in_data = list(map(int,input().split()))
    sum=0
    start=in_data[-1]  #뒤에서부터.....
    for i in range(n-1,-1,-1):
        if in_data[i]<start :
            sum+=start-in_data[i]
        else:
            start=in_data[i]  #start값 바꿔주기 가능이네
    print("#{} {}".format(z+1,sum))