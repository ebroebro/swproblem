#2628 종이자르기

#가로 세로 따로 해서 가장 긴 길이를 각각 구해서 곱해주겠다!
w, h = list(map(int,input().split())) # 가로 세로
n=int(input())   # 자르는 횟수
wide=[0 for _ in range(w)]
height=[0 for _ in range(h)]
for z in range(n) :
    a, b = list(map(int,input().split()))
    if a == 0: # 가로 자르기
        height[b]=1
    if a == 1: # 세로 자르기
        wide[b]=1
wide=wide[1:]   #맨앞줄 0없애보자
height=height[1:]

# 자른거 각각 0 개수 구하고 그것의 max구해서 +1 해주기
# 가로 길이
max_wide=0
start=0

while True:
    cnt = 0
    for i in range(start,len(wide)):
        if wide[i]==0:
            cnt+=1
        else:
            start+=cnt+1
            break
    if max_wide < cnt:
        max_wide =cnt
    if start+cnt ==len(wide):   #  혹시 이거 안되면 그냥 while 을 for 문으로 바꾸자.
        break
#세로길이
start=0
max_height=0
while True:
    cnt = 0
    for i in range(start,len(height)):
        if height[i]==0:
            cnt+=1
        else:
            start+=cnt+1
            break
    if max_height < cnt:
        max_height =cnt
    if start+cnt ==len(height):   #  혹시 이거 안되면 그냥 while 을 for 문으로 바꾸자.
        break

##
print((max_height+1)*(max_wide+1))
