#5174 substree
from pprint import pprint

def f(post):
    global cnt
    for i in range(1,e+2):
        if map_list[i][post]==1 and i not in visited:
            visited.append(i)
            cnt+=1
            f(i)
T=int(input())
for z in range(T):
    e,n = list(map(int,input().split()))
    tmp_list=list(map(int,input().split()))
    map_list=[[0 for i in range(e+2)] for i in range(e+2)]
    for i in range(1,e+1):
        map_list[tmp_list[i*2-1]][tmp_list[i*2-2]]=1

    visited=[n]
    cnt=1


    f(n)
    print("#{} {}".format(z+1,cnt))