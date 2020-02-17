#4466 최대성적표 만들기
#처음엔 그냥 그 갯수만큼 받고, 나머지 하나는 가지거 있는 것중 최저점이랑 비교해서
#맞는지 확인하면 될거 같은데
T=int(input())
for z in range(T):
    n,k = list(map(int,input().split()))
    data_list = list(map(int,input().split()))
    rslt_list=data_list[:k]
    for i in range(k,n):
        tmp = min(rslt_list)
        if tmp < data_list[i]:
            rslt_list[rslt_list.index(tmp)]=data_list[i]
    print("#{} {}".format(z+1,sum(rslt_list)))