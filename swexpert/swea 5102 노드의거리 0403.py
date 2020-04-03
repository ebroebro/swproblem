#5102 노드의 거리
from pprint import pprint

v,e = list(map(int,input().split()))
map_list=[[0 for i in range(v+1)] for _ in range(v+1)]
for i in range(e):
    a,b = list(map(int,input().split()))
    map_list[a][b]=1
    map_list[b][a]=1
s,g=list(map(int,input().split()))
visited=[s]
