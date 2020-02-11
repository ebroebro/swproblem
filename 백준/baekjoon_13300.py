#13300. 방 배정
'''

방 14개 미리 만들기

시작은 방 12

각 방별로 k 개 넘으면 따로 계산 해서 될때마다 +1
'''

n,k = list(map(int,input().split()))
room = [0 for _ in range(13)]

for i in range(n):
    student = list(map(int,input().split()))
    if student[0]==0 :
        room[student[1]]+=1
    elif student[0]==1:
        room[student[1]+6]+=1
# print(room)
cnt=0
for i in range(1,13):
    if room[i]:
        cnt+=1
        while room[i]>k:
            cnt+=1
            room[i]-=k
# print(room)

print(cnt)
