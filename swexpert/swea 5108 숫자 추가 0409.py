#5108 숫자 추가 0409
T=int(input())
for z in range(T):
    n,m,l=list(map(int,input().split()))
    data_list=list(map(int,input().split()))
    for i in range(m):
        idx, a= list(map(int,input().split()))
        data_list.insert(idx,a)
    print("#{} {}".format(z+1,data_list[l]))