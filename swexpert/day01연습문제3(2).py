#달팽이 문제
#먼저 배열 받고 해보기...
from pprint import pprint

data=[[0 for _ in range(5)] for _ in range(5)]  #n*n 배열을 초기화 해요
in_data=[]
for i in range(5):
    in_data.append(list(map(int, input().split())))
nums=[]
for i in range(5):
    for j in range(5):
        nums.append(in_data[i][j])
new_nums=sorted(nums)
###########숫자 받고 정렬

dy = [1,0,-1,0]
dx = [0,1,0,-1]
idx=0
x,y=0,0
while True :
    for dir in range(4):
        while True :
            data[x][y] = new_nums[idx]
            newX = x+ dx[dir]
            newY = y+ dy[dir]
            if 0<=newX<=4 and 0<=newY<=4 and data[newX][newY]==0 :
                x,y = newX, newY
            else:
                break
            idx += 1
    if idx >=len(new_nums) -1:  ##idx 다 쓰면 끝남 그니 .. idx 24되면 끝
        break
pprint(data)