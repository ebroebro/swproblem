#1970 쉬운거스름돈
T=int(input())
for z in range(T):
    won = [50000,10000,5000,1000,500,100,50,10]
    cnt = [0]*len(won)

    N=int(input())
    # i=0
    # while True :
    #     if N<=0:
    #         break
    #     else:
    #         if N >= won[i]:
    #             N-=won[i]
    #             cnt[i]+=1
    #         else:
    #             i+=1

    for i in range(len(won)):
        cnt[i]=N//won[i]
        N-=cnt[i]*won[i]




    print("#{}".format(z+1))
    print(' '.join(list(map(str,cnt))))