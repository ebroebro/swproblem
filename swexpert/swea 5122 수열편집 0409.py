#5122 수열편집 0409

T=int(input())
for z in range(T):
    n,m,l=list(map(int,input().split()))
    data_list=list(map(int,input().split()))
    for i in range(m):
        tmp = list(input().split())
        if tmp[0]=='I':
            data_list.insert(int(tmp[1]),int(tmp[2]))
        elif tmp[0]=='C':
            data_list[int(tmp[1])]=int(tmp[2])
        elif tmp[0]=='D':
            data_list.pop(int(tmp[1]))
    if len(data_list)>l:
        print("#{} {}".format(z+1,data_list[l]))
    else:
        print("#{} -1".format(z + 1))
