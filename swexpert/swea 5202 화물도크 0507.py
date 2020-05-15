#5202 화물도크

def f(start,cnt):
    global max_cnt
    if start == n:
        if max_cnt < cnt:
            max_cnt=cnt
            return
    elif max_cnt== 24:
        return
    elif max_cnt > n-start+cnt:
        return
    else:
        flag=0
        for i in range(work_list[start][0],work_list[start][1]):
            if time_list[i]==1:
                flag=1
                break
        if flag==0:
            for i in range(work_list[start][0], work_list[start][1]):
                time_list[i]=1
            f(start+1,cnt+1)
            for i in range(work_list[start][0],work_list[start][1]):
                time_list[i]=0
        f(start+1,cnt)

T=int(input())
for z in range(T):
    n=int(input())
    time_list=[0]*24
    work_list=[]
    max_cnt=0
    for i in range(n):
        tmp=list(map(int,input().split()))
        work_list.append(tmp)
    f(0,0)

    print("#{} {}".format(z+1,max_cnt))
