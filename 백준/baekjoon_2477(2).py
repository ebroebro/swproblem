#2477. 참외밭
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
for i in range(6):
    dis.append(dis[i])

#3을 더하는 경우로... 찾기
minus_h = dis[dis.index(max_w)+3]
minus_w = dis[dis.index(max_h)+3]
minus = minus_h*minus_w
print(n*(size-minus))