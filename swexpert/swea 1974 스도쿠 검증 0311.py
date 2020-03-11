T=int(input())
for z in range(T):
    map_list =[list(map(int,input().split())) for _ in range(9)]
    flag = 1
    check=[i for i in range(1,10)]
    rotate_list =list(map(list, zip(*map_list)))
    for i in range(9):
        if sorted(map_list[i]) != check:
            flag=0
            break
        if sorted(rotate_list[i]) != check:
            flag=0
            break

    if flag:
        for k in range(0,7,3):
            if flag:
                for l in range(0, 7, 3):
                    tmp_list = []
                    for i in range(3):
                        for j in range(3):
                            tmp_list.append(map_list[k+i][l+j])
                    if sorted(tmp_list)!=check:
                        flag=0
                        break
            else:
                break
    print("#{} {}".format(z+1,flag))