# 1986. 지그재그 숫자
# 배열 초기화 방법 중에
# c= [0]*12 0으로 12개 칸 만드는거.. 이렇게 쓸수 있네 ? ?

T= int(input())
for i in range(1,T+1):
    result = 0
    N=int(input())
    for j in range(1,N+1):
        if j %2 :
            result += j
        else :
            result -= j
    print("#{0} {1}".format(i,result))