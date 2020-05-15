#5202 화물도크

T=int(input())
for z in range(T):
    n=int(input())
    time_list=[0]*24
    work_list=[]
    max_cnt=0
    for i in range(n):
        tmp=list(map(int,input().split()))
        work_list.append(tmp)


    print("#{} {}".format(z+1,max_cnt))
