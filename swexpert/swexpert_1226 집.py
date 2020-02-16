#1226

def DFS(startx,starty):
    global isOkay, visited, map_list
    visited.append([startx,starty])
    if map_list[startx][starty] ==3:
        isOkay=1
        return
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    for i in range(4):
        newx=startx+dx[i]
        newy=starty+dy[i]
        if 0<=newx<16 and 0<=newy<16 and map_list[newx][newy]!=1 and ([newx,newy] not in visited) :
            DFS(newx,newy)

#map 만들기 16*16
for _ in range(10):
    z=int(input())
    map_list=[]
    for i in range(16):
        data= int(input())
        data_list=[]
        for j in range(16):
            data_list.append(data%10)
            data//=10
        data_list = data_list[::-1]
        if data_list.count(2):
            startx=i
            starty= data_list.index(2)
        map_list.append(data_list)
    visited=[]
    isOkay=0

    DFS(startx,starty)

    print("#{} {}".format(z,isOkay))