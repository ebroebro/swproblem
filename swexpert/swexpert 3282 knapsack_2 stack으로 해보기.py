#knapsack 3282
#이거는 배운거 써야할듯? 그 부분집합 문제로 해결하기. 가지치기 편하려면 backtracking 쓰는게 좋을듯 ?
import sys
sys.stdin=open('input.txt','r')





T=int(input())
for z in range(T):
    n,k = list(map(int,input().split()))
    v_list=[]
    c_list=[]
    for _ in range(n):
        v,c = list(map(int,input().split()))
        c_list.append(c)
        v_list.append(v)
    #부피제한이 k 있는거임 가치가 높아야해
    rslt_list=[] #index번호를 집어넣어야할듯
    input=n
    max=0


    
    stack=[i]


    def knapsack(s_v, s_c):
        global rslt_list, k, max, c_list, v_list
        if s_v <= k and s_c >= max:
            max = s_c
        for i in range(len(c_list)):
            if i not in rslt_list and s_v + v_list[i] <= k and s_c + c_list[i] >= max:
                rslt_list.append(i)
                s_v += v_list[i]
                s_c += c_list[i]
                knapsack(s_v, s_c)
                rslt_list.pop()
                s_v -= v_list[i]
                s_c -= c_list[i]


    print("#{} {}".format(z+1,max))