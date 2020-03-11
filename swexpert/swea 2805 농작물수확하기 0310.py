T=int(input())
for z in range(T):
    n=int(input())
    map_list=[]
    for _ in range(n):
        tmp_list=[]
        tmp=int(input())
        for _ in range(n):
            tmp_list.append(tmp%10)
            tmp//=10
        map_list.append(tmp_list[::-1])

    center=(n-1)//2
    tmp=0
    sum_number=0
    for i in range(n):
        for j in range(center-tmp,center+tmp+1):
            sum_number+=map_list[i][j]
        if i <center:
            tmp+=1
        else:
            tmp-=1

    print("#{} {}".format(z+1,sum_number))