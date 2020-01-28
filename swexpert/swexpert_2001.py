# 2001. 파리 퇴치
T=int(input())
for num in range(T):
    N, M = list(map(int, input().split()))
    #print("{} {}".format(N,M))
    data_list=[]
    for i in range(N):
        data_list.append(list(map(int, input().split())))
    sum=0

    for i in range(N-M+1):
        for j in range(N-M+1):
            new_sum=0
            for k in range(M):
                for l in range(M):
                    new_sum+=data_list[i+k][j+l]

            if sum < new_sum:
                sum = new_sum
    print("#{0} {1}".format(num+1,sum))
