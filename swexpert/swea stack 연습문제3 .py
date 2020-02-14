#stack 연습문제 3
from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')

data_list=list(map(int,input().split()))
new_list = list(set(data_list))
node=len(new_list)
line=len(data_list)//2
visited=[]

map_list = [[0 for _ in range(node+1)] for _ in range(node+1)]

for i in range(line):
    map_list[data_list[2*i]][data_list[2*i+1]]=1
    map_list[data_list[2*i+1]][data_list[2*i]]=1

# pprint(map_list)
def DFS(here):
    global visited
    visited.append(here)
    if sorted(visited) == sorted(new_list):
        return
    for j in range(node+1):
        if map_list[here][j]==1 and j not in visited:
            DFS(j)
            print(j)

DFS(1)


print(*visited)