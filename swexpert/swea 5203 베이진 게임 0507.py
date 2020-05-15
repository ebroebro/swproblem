#5203 베이진 게임
t=int(input())
for z in range(t):
    print('#{} '.format(z+1),end='')
    tmp_list=list(map(int,input().split()))
    one_rslt=False
    two_rslt=False
    one_list=[0 for _ in range(10)]
    two_list=[0 for _ in range(10)]
    for i in range(0,len(tmp_list),2):
        one_list[tmp_list[i]]+=1
        two_list[tmp_list[i+1]]+=1
        for j in range(8):
            if one_list[j]>=1 and one_list[j+1]>=1 and one_list[j+2]>=1:
                one_rslt=True
            if two_list[j] >= 1 and two_list[j + 1] >= 1 and two_list[j + 2] >= 1:
                two_rslt = True
        for j in range(10):
            if one_list[j]==3:
                one_rslt=True
            if two_list[j]==3:
                two_rslt=True
        if one_rslt==True:
            print('1')
            break
        elif two_rslt==True:
            print('2')
            break
    else:
        print('0')