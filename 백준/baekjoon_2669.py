#2669 직사각형 네개의 합집합의 면적 구하기

# 꼭지점 x,y 로 먼저 원래 합을 구하고
# 사각형 부분을 1로 표시하고 겹치는 부분 빼기??
# 아니면 사각형 부분 1로 표시다 해놓고 1 count 해도 될거 같기도 하고

map_list = [[0 for _ in range(100)] for _ in range(100)]

# 만족하는 것에 1 넣기!!
for _ in range(4):
    x1,y1,x2,y2 = list(map(int,input().split()))
    for i in range(x1,x2):
        for j in range(y1,y2):
            map_list[i][j]=1
    count=0
    for i in range(100):
        for j in range(100):
            if map_list[i][j]==1:
                count+=1

print(count)