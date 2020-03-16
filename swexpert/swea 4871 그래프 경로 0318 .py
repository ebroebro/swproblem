#4871 그래프 경로
T=int(input())
for z in range(T):
    v,e=list(map(int,input().split()))
    map_list=[[0 for _ in range(v+1)] for _ in range(v+1)]
    for _ in range(e):
        start,end = list(map(int,input().split()))
        map_list[start][end]=1
    s,g= list(map(int,input().split()))
    flag=0
    def f(post):
        global flag
        if flag==1:
            return
        for i in range(v+1):
            if map_list[post][g]==1:
                flag=1
                return
            elif map_list[post][i]==1:
                map_list[post][i]=0
                f(i)
                map_list[post][i]=1
    f(s)
    print("#{} {}".format(z+1,flag))