#2304. 창고 다각형
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

print(max_index)
# area = max(height)  #가운데 제일 큰값
# print(area)
area=0


#앞에서 가운데로
next_max=height[0]
next_pst=pst[0]
for i in height[0:max_index]:
    if i > next_max :
        next_max=i
    area+=next_max
print(area)
#뒤에서 가운데로
next_max=height[-1]
next_pst=pst[-1]
height2=height[max_index:n]
for i in height2[::-1]:
    if i > next_max :
        next_max=i
    area+=next_max

print(area)