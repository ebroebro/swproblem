#6190 추억의 2048 게임
from pprint import pprint


T=int(input())
for z in range(T):
    n,s = input().split()
    n=int(n)
    map_list= [list(map(int,input().split())) for _ in range(n)]
    #기본적으로 왼쪽으로 민다고 생각하자.
    #일단 돌리기
    new_list= [[0 for _ in range(n)] for _ in range(n)]
    if s=='up' or s == 'down':
        for i in range(n):
            for j in range(n):
                new_list[i][j] = map_list[j][i]
    else:
        for i in range(n):
            for j in range(n):
                new_list[i][j] = map_list[i][j]
    #계산 해보기
    rslt_list=[[0 for _ in range(n)] for _ in range(n)]
    tmp_list=[[0 for _ in range(n)] for _ in range(n)]
    if s == 'up' or s=='left':
        for i in range(n):
            post=0
            for j in range(n):
                if new_list[i][j]:
                    tmp_list[i][post]=new_list[i][j]
                    post+=1
            #0당기기

            for j in range(n-1):
                if tmp_list[i][j]==tmp_list[i][j+1]:
                    tmp_list[i][j]*=2
                    tmp_list[i][j+1]=0
            post=0
            for j in range(n):
                if tmp_list[i][j]:
                    rslt_list[i][post]=tmp_list[i][j]
                    post+=1
    else:
        for i in range(n):
            post=n-1
            for j in range(n-1,-1,-1):
                if new_list[i][j]:
                    tmp_list[i][post]=new_list[i][j]
                    post-=1
            #0당기기
            for j in range(n-1,0,-1):
                if tmp_list[i][j]==tmp_list[i][j-1]:
                    tmp_list[i][j]*=2
                    tmp_list[i][j-1]=0
            post=n-1
            for j in range(n-1,-1,-1):
                if tmp_list[i][j]:
                    rslt_list[i][post]=tmp_list[i][j]
                    post-=1


    #다시 돌리기
    rslt_list2=[[0 for _ in range(n)] for _ in range(n)]
    if s=='up' or s == 'down':
        for i in range(n):
            for j in range(n):
                rslt_list2[i][j] = rslt_list[j][i]
    else:
        for i in range(n):
            for j in range(n):
                rslt_list2[i][j] = rslt_list[i][j]


    print("#{}".format(z+1))
    for i in range(n):
        print(*rslt_list2[i])
