#5097 회전
T=int(input())
for z in range(T):
    n,m= list(map(int,input().split()))
    tmp_list=list(map(int,input().split()))
    for i in range(m):
        tmp=tmp_list.pop(0)
        tmp_list+=[tmp]
    print("#{} {}".format(z+1,tmp_list[0]))