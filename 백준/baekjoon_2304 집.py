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

max_h = max(height)
area+= max_h

# ----> 이방향
start = 0



#<==== 이방향
