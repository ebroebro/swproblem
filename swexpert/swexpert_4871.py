#4871 그래프 경로
node,line= list(map(int,input().split()))
map_list = [[0 for _ in range(node+1)] for _ in range(node+1)]
for _ in range(line):
    info = list(map(int,input().split()))
    map_list[info[0]][info[1]]=1
S,G=list(map(int,input().split()))
visited=[]
isOkay=0

def DFS(here):
    global isOkay, visited,G
    visited.append(here)
    if here == G:
        isOkay = 1
        return
    for i in range(1,here+1):
        if map_list[here][i]==1 and not visited:
            i=here
            DFS(here)

DFS(S)

print(isOkay)