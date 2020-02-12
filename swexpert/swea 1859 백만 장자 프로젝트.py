#1859 백만장자 프로젝트
'''
처음부터 하긴하는데
그 각각 기준으로 젤 끝에서 부터의 차이가 큰것을 찾는거야
그 기준값은 맨뒤에서 부터 하나씩 줄어들기로 하면 되지 않을까
'''



import sys
sys.stdin = open('input.txt','r')

T=int(input())
for z in range(T):
    n= int(input())
    data_list = list(map(int,input().split()))
    rslt=0
    max=data_list[-1]
    for i in range(len(data_list)-1,-1,-1):
        if max > data_list[i]:
            rslt+= max - data_list[i]
        else:
            max=data_list[i]

    print("#{} {}".format(z+1,rslt))
