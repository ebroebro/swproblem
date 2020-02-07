#1267. 작업순서
from pprint import pprint

v,e = list(map(int,input().split()))
data= list(map(int,input().split()))
map_list=[[0 for i in range(v+1)] for i in range(v+1)] ## 0 부터 그 숫자 번호 까지
indegree =[0 for i in range(v+1)]
indegree[0]=99
visited=[]  #한번 왔다간 놈은 visited에 append해주자
for i in range(e):
    x=data[2*i]
    y=data[2*i+1]
    map_list[x][y]=1
    map_list[y][x]=1
# pprint(map_list)
#받는 것의 개수가 0인것이 우선순위를 갖는다
for i in range(e):
    indegree[data[2*i+1]]+=1

while True:
    for i in range(v+1):
        if indegree[i]==0 and (i not in visited):
            visited.append(i)
            for j in range(v+1):
                if map_list[i][j]==1:
                    indegree[j]-=1
    if len(visited)==v:
        break

print("#{} {}".format(1,' '.join(list(map(str,visited)))))