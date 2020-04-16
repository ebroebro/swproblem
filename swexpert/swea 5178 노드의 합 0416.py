#5178 노드의 합
def f(post):
    if post==0:
        return
    f(L[post])
    f(R[post])
    if V[post]==0:
        V[post]=V[R[post]]+V[L[post]]


T= int(input())
for z in range(T):
    n,m,l = list(map(int,input().split()))
    L=[0]*(n+1)
    R=[0]*(n+1)
    P=[0]*(n+1)
    V=[0]*(n+1)
    leaf=[]
    #leaf 값
    for i in range(m):
        tmp=list(map(int,input().split()))
        V[tmp[0]]=tmp[1]
        leaf.append(tmp[0])

    #부모형제 관계
    for i in range(1,n+1):
        if 2*i <= n:
            L[i]=2*i
        if 2*i+1 <= n:
            R[i]=2*i+1
        P[i]=i//2


    f(1)

    print("#{} {}".format(z+1,V[l]))