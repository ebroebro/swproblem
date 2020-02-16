#10163 색종이
map_list=[[0 for _ in range(101)] for _ in range(101)]
n=int(input())
cnt=0
for num in range(1,n+1):
    x,y,w,h = list(map(int,input().split())) #map_list[y][x] w:x, h:y
    for i in range(h):
        for j in range(w):
            map_list[y+i][x+j]=num

for num in range(1,n+1):
    area=0
    for i in range(101):
        for j in range(101):
            if map_list[i][j]==num:
                area+=1
    print(area)



