#2304. 창고 다각형
n=int(input())
data_list=[]
pst=[] #위치와
height=[] #높이

for _ in range(n):
    data = list(map(int, input().split()))
    data_list.append(data)
print(data_list)
data_list = sorted(data_list)
print(data_list)
for i in range(n):
    pst.append(data_list[i][0])
    height.append(data_list[i][1])
print(pst)
print(height)
start=0
rslt=0
while True:
    next=start+1
    max=height[start]
    while next<n:
        if height[start]<height[next]:
            rslt+= height[start]*(pst[next]-pst[start])
            start = next
            break
        else:
            if max < height[next]:
                max=height[next]
        next+=1
    rslt+=max*(pst[height.index(max)]-pst[start]+1)+height[start]-max
    start=pst[height.index(max)]
print(rslt)