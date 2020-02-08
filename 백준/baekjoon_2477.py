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
dir.append(dir[0])
dis.append(dis[0])  #사라지는 부분이 젤 처음과 끝부분일수도 있다.

for i in range(7):
    if dir[i]==2 and dir[i+1]==4 :
        minus=dis[i]*dis[i+1]
        break
    if dir[i]==3 and dir[i+1]==2 :
        minus=dis[i]*dis[i+1]
        break
    if dir[i]==1 and dir[i+1]==3 :
        minus=dis[i]*dis[i+1]
        break
    if dir[i]==4 and dir[i+1]==1:
        minus=dis[i]*dis[i+1]
        break

print(n*(size-minus))