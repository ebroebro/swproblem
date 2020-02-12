#2304. 창고 다각형
import sys
sys.stdin=open('input.txt','r')

n=int(input())
data_list=[]
pst=[] #위치와
height=[] #높이

for _ in range(n):
    data = list(map(int, input().split()))
    data_list.append(data)
data_list = sorted(data_list)
for i in range(n):
    pst.append(data_list[i][0])
    height.append(data_list[i][1])

max_index= height.index(max(height)) #가운데 값
area = max(height)  #가운데 제일 큰값
#앞에서 가운데로
next_max=height[0]
next_pst=pst[0]
for i in range(max_index+1):
    if next_max < height[i]:
        area+=(pst[i]-next_pst)*next_max
        next_max=height[i]
        next_pst=pst[i]
#뒤에서 가운데로
next_max=height[len(height)-1]
next_pst=pst[len(height)-1]
for i in range(n-1,max_index-1,-1):
    if next_max <height[i]:
        area += abs(pst[i] - next_pst) * next_max
        next_max = height[i]
        next_pst = pst[i]
print(area)