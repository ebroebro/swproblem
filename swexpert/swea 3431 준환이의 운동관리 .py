T=int(input())
for z in range(T):
    L,U,X= list(map(int, input().split()))
    print("#{}".format(z+1),end=' ')
    if X >U :
        print('-1')
    elif X < L :
        print(L-X)
    else:
        print(0)