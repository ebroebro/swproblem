#knapsack 3282
#이거는 배운거 써야할듯? 그 부분집합 문제로 해결하기. 가지치기 편하려면 backtracking 쓰는게 좋을듯 ?
# T=int(input())
# for z in range(T):
n,k = list(map(int,input().split()))
v_list=[]
c_list=[]
for _ in range(n):
    v,c = list(map(int,input().split()))
    v_list.append(v)
    c_list.append(c)
#부피제한이 k 있는거임 가치가 높아야해
rslt_list=[]

def knapsack(data, k, input, s1,s2):
    if k == input:
