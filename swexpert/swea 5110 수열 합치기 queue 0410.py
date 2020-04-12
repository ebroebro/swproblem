#5110 수열 합치기 queue
from collections import deque

T=int(input())
for z in range(T):
    n,m = list(map(int,input().split()))

    data_list=list(map(int,input().split()))
    for i in range(m-1):
        tmp_dq=deque(list(map(int,input().split())))
        tmp=tmp_dq[0]
        for j in range(len(data_list)):
            if tmp < data_list[j]:
                idx=j
                break
        else:
            idx=len(data_list)
        left_list=data_list[:idx]
        right_list=data_list[idx:]
        tmp_dq.extendleft(left_list[::-1])
        tmp_dq.extend(right_list)
        data_list=list(tmp_dq)
    print("#{}".format(z+1),end='')
    for _ in range(10):
        print(' ',end='')
        print(data_list.pop(), end='')
    print()
