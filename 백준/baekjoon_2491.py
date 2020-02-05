#2491 . 수열
n=int(input())
data_list = list(map(int,input().split()))
max_num =0
## 연속해서 커지는 경우
start =0
while True:
    cnt=0
    for i in range(start,len(data_list)-1):
        if data_list[i]<=data_list[i+1]:
            cnt+=1
        else:
            start+=cnt+1
            break
    if max_num < cnt :
        max_num =cnt
    if start + cnt >=len(data_list)-1:
        break

##연속해서 작아지는 경우
start =0
while True:
    cnt=0
    for i in range(start,len(data_list)-1):
        # print(start)
        if data_list[i]>=data_list[i+1]:
            cnt+=1
        else:
            start+=cnt+1
            break
    if max_num < cnt :
        max_num =cnt
    if start + cnt >=len(data_list)-1:
        break

print(max_num+1)