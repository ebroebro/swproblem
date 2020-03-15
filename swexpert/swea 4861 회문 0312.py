T=int(input())
for z in range(T):
    n,m=list(map(int,input().split()))
    map_list=[input() for _ in range(n)]
    new_list=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_list[j][i]=map_list[i][j]

    for i in range(n):
        for j in range(n-m+1):
            tmp= map_list[i][j:j+m]
            if tmp==tmp[::-1]:
                rslt=tmp
                break
            tmp=new_list[i][j:j+m]
            if tmp==tmp[::-1]:
                rslt=tmp
                break
        if tmp==tmp[::-1]:
            rslt=tmp
            break

    print("#{} {}".format(z+1,''.join(rslt)))