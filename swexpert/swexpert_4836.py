#4836 색칠하기
#이 문제는 같은 색끼리 겹치지 않는다고 했기 때문에 굳이 색깔별로 모눈을 만들어 줄필요는 없다
#1, 2로 한다음에 그 칸의 값이 3인게 몇개인지 골라보겠다.
#문제를 ... 잘읽어야 겠구나...

from pprint import pprint  #이쁘게 인쇄해줌...
T=int(input())
for z in range(T):
    N= int(input())

    field= [[0]*10 for i in range(10)]
    for i in range(N):
        r1,c1,r2,c2,color = list(map(int, input().split()))
        for j in range(r1,r2+1):
            for k in range(c1,c2+1):
                field[j][k]+=color

    cnt=0
    for j in range(10):
        for k in range(10):
            if field[j][k]==3:
                cnt+=1

    print("#{} {}".format(z+1,cnt))
