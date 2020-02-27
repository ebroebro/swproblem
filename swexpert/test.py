#1258 행렬 찾기

def DFS(x,y):
    if 0>x or x>=n or y<0 or y>=n or [x,y] in visited or map_list[x][y] in visited:
        return
    visited.append([x,y])
    for l in range(4):
        newX=x+dx[l]
        newY=y+dy[l]
        if 0<=newX<n and 0<=newY<n and map_list[newX][newY]!=0 and [newX,newY] not in visited:
            DFS(newX,newY)


n= int(input())
map_list =[]
for i in range(n):
    data_list = list(map(int,input().split()))
    map_list.append(data_list)

dy=[1,-1,0,0]
dx=[0,0,-1,1]
visited=[]

rslt = []
for i in range(n):
    for j in range(n):
        if 0<=i<n and 0<=j<n and [i,j] not in visited and map_list[i][j]!=0:
            tmpx=i
            tmpy=j
            DFS(i,j)
            tmp_list= visited[visited.index([tmpx,tmpy]):]
            hmax=0
            hmin=987654321
            wmax=0
            wmin=987654321
            for k in range(len(tmp_list)):
                if tmp_list[k][0]>hmax:
                    hmax=tmp_list[k][0]
                if tmp_list[k][0]<hmin:
                    hmin=tmp_list[k][0]
                if tmp_list[k][1]>wmax:
                    wmax=tmp_list[k][1]
                if tmp_list[k][1]<wmin:
                    wmin=tmp_list[k][1]
            rslt.append([hmax-hmin+1, wmax-wmin+1])

# print(rslt)

for i in range(len(rslt)):
    for j in range(i,len(rslt)):
        if rslt[i][0]*rslt[i][1]>rslt[j][0]*rslt[j][1]:
            rslt[i],rslt[j]=rslt[j],rslt[i]
        elif rslt[i][0]*rslt[i][1]==rslt[j][0]*rslt[j][1] and rslt[i][0]>rslt[j][0]:
            rslt[i], rslt[j] = rslt[j], rslt[i]

print("#{}".format(1),end='')
print(" {}".format(len(rslt)),end='')
for i in range(len(rslt)):
    for j in range(2):
        print(" {}".format(rslt[i][j]),end='')
print()