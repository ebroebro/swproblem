#swea 2001 파리퇴치
T=int(input())
for z in range(T):
    n,m =list(map(int,input().split()))
    map_list =[list(map(int,input().split())) for _ in range(n)]
    max_sum=0
    for l in range(n-m+1):
        for k in range(n-m+1):
            tmp_sum=0
            for i in range(m):
                for j in range(m):
                    tmp_sum+=map_list[l+i][k+j]
            if tmp_sum > max_sum:
                max_sum=tmp_sum
    print("#{} {}".format(z+1,max_sum))