#5110 수열 합치기 list
T=int(input())
for z in range(T):
    n,m = list(map(int,input().split()))
    data_list=list(map(int,input().split()))
    for i in range(m-1):
        tmp_list=[]
        tmp_list=list(map(int,input().split()))
        tmp=tmp_list[0]
        for j in range(len(data_list)):
            if tmp < data_list[j]:
                idx=j
                break
        else:
            idx=len(data_list)
        while tmp_list:
            data_list.insert(idx,tmp_list.pop())
    rslt_list=data_list[::-1]
    print("#{}".format(z+1),end=' ')
    print(*rslt_list[:10])
