#2304. 창고 다각형
import sys
sys.stdin=open('input.txt','r')

data_list = [0 for _ in range(1001)]  # 좌표 세팅하고
n = int(input())
start=1001
end=0
for _ in range(n):
    l,h=list(map(int,input().split()))
    data_list[l]=h
    if start > l :
        start=l
    if end < l:
        end = l
#start 주어진 수 중 가장 앞 수 /end 주어진 수 중 가장 뒤에 위치한 수
max_h= max(data_list)  #가장 큰 높이
max_index= data_list.index(max_h)   #가장 높은 위치
area= max_h  #가장 높은 곳 일단 계산 한번 해주기

# start----->max_index
left_max = data_list[start]
for i in range(start, max_index):
    if left_max < data_list[i]:
        left_max =data_list[i]
    area+=left_max

#max_index<-----end
right_max=data_list[end]
for i in range(end, max_index,-1):
    if right_max < data_list[i]:
        right_max =data_list[i]
    area+=right_max

print(area)