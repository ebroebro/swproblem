#3378 스타일리쉬 들여쓰기
T=int(input())
for z in range(T):
    p,q=list(map(int,input().split()))
    # check_list=['(',')','{','}','[',']']
    check_list=[0,0,0]
    check_list2=[]
    pointer_check=[]
    map_list=[]
    for i in range(p):
        map_list.append(list(input()))
        cnt=0
        for j in map_list[i]:
            if j =='.':
                cnt+=1
            else:
                pointer_check.append(cnt)
                break

    for i in range(p):
        for j in map_list[i]:
            if j =='(':
                check_list[0]+=1
            elif j ==')':
                check_list[0]-=1
            elif j=='{':
                check_list[1]+=1
            elif j=='}':
                check_list[1]-=1
            elif j=='[':
                check_list[2]+=1
            elif j==']':
                check_list[2]-=1
        tmp_list=check_list.copy()
        check_list2.append(tmp_list)
    #
    # print(check_list2)
    # print(pointer_check)

    flag=0
    r=[]
    c=[]
    s=[]
    for i in range(1,21):
        for j in range(1,21):
            for k in range(1,21):
                tmp_r=i
                tmp_c=j
                tmp_s=k
                cnt_check=0
                for m in range(p-1):
                    if tmp_r*(check_list2[m][0])+tmp_c*(check_list2[m][1])+tmp_s*(check_list2[m][2]) == pointer_check[m+1]:
                        cnt_check+=1
                    else:
                        break
                if cnt_check ==p-1:
                    r.append(tmp_r)
                    c.append(tmp_c)
                    s.append(tmp_s)

    #새로운 단락에 적용하기
    check_list=[0,0,0]
    rslt_list=[0]
    for i in range(q):
        my_list=list(input())
        for j in my_list:
            if j == '(':
                check_list[0] += 1
            elif j == ')':
                check_list[0] -= 1
            elif j == '{':
                check_list[1] += 1
            elif j == '}':
                check_list[1] -= 1
            elif j == '[':
                check_list[2] += 1
            elif j == ']':
                check_list[2] -= 1
        if i!=q-1:
            rslt_list.append(r[0] * (check_list[0]) + c[0] * (check_list[1]) + s[0] * (check_list[2]))
            for m in range(1,len(r)):
                tmp_rslt_list=r[m]*(check_list[0])+c[m]*(check_list[1])+s[m]*(check_list[2])
                if tmp_rslt_list!=rslt_list[i+1]:
                    rslt_list[i+1]=-1
                    break
    print("#{}".format(z+1), end=' ')
    print(*rslt_list)