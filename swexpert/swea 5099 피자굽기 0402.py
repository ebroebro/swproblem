#5099 피자굽기 0402
T=int(input())
for z in range(T):
    n,m = list(map(int,input().split()))
    data_list=list(map(int,input().split()))
    rslt_list=[[data_list[i],i+1] for i in range(m)]
    tmp_list=[rslt_list[i] for i in range(n)]
    check=n
    cnt=1
    flag=0
    while True:
        if flag==1:
            break
        else:
            if tmp_list[0][0]==0 and check < m:
                tmp_list[0]=rslt_list[check]
                check+=1
            tmp=tmp_list.pop(0)
            tmp[0]//=2
            tmp_list.append(tmp)
            cnt=0
            if check >=m:
                for i in tmp_list:
                    if i[0]!=0:
                        cnt+=1
                        rslt=i[1]
                if cnt==1:
                    flag=1
    print("#{} {}".format(z+1,rslt))