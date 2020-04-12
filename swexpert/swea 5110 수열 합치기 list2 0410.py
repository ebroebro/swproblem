#5110 수열 합치기 list2 list[idx:idx] 쓰면 중간 공간 비워줌...
T=int(input())
for z in range(T):
    n,m = list(map(int,input().split()))
    data_list=list(map(int,input().split()))
    for i in range(m-1):
        tmp_list=list(map(int,input().split()))
        tmp=tmp_list[0]
        for j in range(len(data_list)):
            if tmp < data_list[j]:
                idx=j
                break
        else:
            idx=len(data_list)
        data_list[idx:idx]=tmp_list
    rslt_list=data_list[::-1]
    print("#{}".format(z+1),end=' ')
    print(*rslt_list[:10])
