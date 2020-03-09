T=int(input())
for z in range(T):
    str1 = list(set(input()))
    str2=input()
    cnt_max=0
    for i in str1:
        cnt=0
        for j in str2:
            if i ==j:
                cnt+=1
        if cnt_max < cnt:
            cnt_max=cnt
    print("#{} {}".format(z+1,cnt_max))