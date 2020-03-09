T=int(input())
for z in range(T):
    n=int(input())
    check_list=[0 for _ in range(10)]
    numbers=int(input())
    for i in range(n):
        tmp = numbers%10
        numbers//=10
        check_list[tmp]+=1

    max_cnt=0
    max_num=0
    for i in range(10):
        if check_list[i]>=max_cnt:
            max_num=i
            max_cnt=check_list[i]

    print("#{} {} {}".format(z+1,max_num,max_cnt))