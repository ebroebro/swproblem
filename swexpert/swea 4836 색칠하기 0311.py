T=int(input())
for z in range(T):
    map_list=[[0 for _ in range(10)] for _ in range(10)]
    n = int(input())
    cnt=0
    for _ in range(n):
        r1,c1,r2,c2,color = list(map(int,input().split()))
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                map_list[i][j]+=color
                if map_list[i][j] ==3:
                    cnt +=1
    print("#{} {}".format(z+1,cnt))