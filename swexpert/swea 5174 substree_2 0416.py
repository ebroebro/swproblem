#5174 substree
from pprint import pprint

def f(post):
    global cnt
    if L[post]:
        f(L[post])
        cnt+=1
    if R[post]:
        f(R[post])
        cnt+=1


T=int(input())
for z in range(T):
    e,n = list(map(int,input().split()))
    tmp_list=list(map(int,input().split()))
    L=[0]*(e+2)
    R=[0]*(e+2)
    P=[0]*(e+2)


    for i in range(0,len(tmp_list),2):
        if L[tmp_list[i]]:
            R[tmp_list[i]]=tmp_list[i+1]
        else:
            L[tmp_list[i]]=tmp_list[i+1]
        P[tmp_list[i+1]]=tmp_list[i]

    cnt=1
    f(n)
    print("#{} {}".format(z+1,cnt))
