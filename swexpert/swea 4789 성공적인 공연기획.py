#성공적인 공연기획
import sys
sys.stdin = open('input.txt','r')
T=int(input())
for z in range(T):
    data=str(input())
    data_list = list(data)
    data_list = list(map(int,data_list))

    num=0
    need=0
    for i in range(len(data_list)):
        if data_list[i]:
            if i <=num:
                num+=data_list[i]
            else:
                tmp=i-num
                need+=tmp
                num+=tmp+data_list[i]

    print("#{} {}".format(z+1,need))