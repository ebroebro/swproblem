#3752 시험 가능한 점수


T=int(input())
for z in range(T):
    n=int(input())
    data_list = list(map(int,input().split()))
    cnt=0
    check_list = [0 for _ in range(sum(data_list)+1)]
    check_list[0]=1
    for j in range(n):
        for i in range(len(check_list)-1,-1,-1):  #큰것부터 하는 이유는 더하고 나서 그다음에 영향을 안주기 위해서
            if check_list[i]:
                check_list[data_list[j]+i]=1

    for i in check_list:
        if i:
            cnt+=1

    print("#{} {}".format(z+1,cnt))

