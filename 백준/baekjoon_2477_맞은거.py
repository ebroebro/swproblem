#2477. 참외밭  ##이게 맞은거..
n=int(input())
dir=[0 for i in range(7)]
dis=[0 for i in range(7)]
max_w=0 #동서
max_h=0 #남북
for i in range(6):
    dir[i],dis[i]= list(map(int,input().split()))
    if dir[i]== 1 or dir[i]==2:
        if max_w< dis[i]:
            max_w=dis[i]
    if dir [i]==3 or dir[i]==4:
        if max_h < dis[i]:
            max_h =dis[i]
size=max_w*max_h
#제일 큰 거 두개 찾음

#이젠 케이스 별로 생각해야할듯 ??
minus=0 # 뺄거 찾기

#3을 더하는 경우로... 찾기
index_w = dis.index(max_w)+3
index_h = dis.index(max_h)+3
while True:
    if index_w < 6:
        minus_h = dis[index_w]
        break
    else :
        index_w-=6
while True:
    if index_h < 6:
        minus_w = dis[index_h]
        break
    else :
        index_h-=6
minus = minus_h*minus_w
print(n*(size-minus))