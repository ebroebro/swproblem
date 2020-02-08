#13304. 방 배정
'''

방 14개 미리 만들기
 12학년 남녀는 한방

3-4 남 5-6 남
3-4 여 5-6 여

시작은 방 다섯개
여 0 남1

각 방별로 k 개 넘으면 따로 계산 해서 될때마다 +1
'''

n,k = list(map(int,input().split()))
room = [0 for _ in range(5)]

for i in range(n):
    student = list(map(int,input().split()))
    if student[1]==1 or student[1]==2 :  #1,2학년이면 0번방
        room[0]+=1
    if student[0]==0:
        if student[1]==3 or student[1]==4:  # 여 34 1번방
            room[1]+=1
        if student[1] == 5 or student[1] == 6:  # 여 56 3번방
            room[2] += 1
    if student[0]==1:
        if student[1]==3 or student[1]==4 : # 남 34 2번방
            room[3]+=1
        if student[1]==5 or student[1]==6 : # 남 56 4번방
            room[4]+=1
# print(room)
cnt=0
for i in range(5):
    if room[i]:
        cnt+=1
        while room[i]>k:
            cnt+=1
            room[i]-=k
# print(room)

print(cnt)
