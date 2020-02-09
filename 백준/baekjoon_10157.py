# 10157. 자리배정

from pprint import pprint

# MAP 부터 만들기
C,R = list(map(int,input().split()))
# C, R = 7, 6
k= int(input())
# k = 11
map_list = [[0 for _ in range(C + 2)] for _ in range(R + 2)]
# 테두리까지 만들어 보기

# print(map_list)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 1, 1
num = 1
if k > C * R:
    print('0')
else:
    while True:
        for i in range(4):
            while True:
                map_list[y][x] = num
                if num == k:
                    rslt_list =[x,y]
                    break
                newX = x + dx[i]
                newY = y + dy[i]
                if 0 < newX <= C and 0 < newY <= R and map_list[newY][newX] == 0:
                    x = newX
                    y = newY
                    num += 1
                else:
                    break
            if num == C*R or num ==k:
                # print("{} {}".format(x,y))
                break
        if num == C * R or num == k:
            break
    print("{} {}".format(rslt_list[1],rslt_list[0]))
    print(map_list)