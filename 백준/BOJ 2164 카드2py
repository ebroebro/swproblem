#10250 ACM 호텔

T=int(input())
for _ in range(T):
# #     H,W,N = list(map(int,input().split()))
# #     height = str(N%H)
# #     ho = str("%02d" %(N//H+1))
# #
# #     rslt = height + ho
# #     print(rslt)
    H,W,N = list(map(int,input().split()))
    map_list = [[0 for _ in range(H+1)] for _ in range(W+1)]
    no=0
    for i in range(1,W+1):
        for j in range(1,H+1):
            map_list[i][j]=no
            no += 1
            if no==N:
                height = str(j)
                ho = str("%02d" %(i))
                rslt= height+ho
                break
        if no ==N:
            height = str(j)
            ho = str("%02d" % (i))
            rslt = height + ho
            break
print(rslt)