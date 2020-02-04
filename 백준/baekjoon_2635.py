#2635 수 이어가기


n = int(input())
max=0
max_list=[]
for j in range(1,n+1):
    data_list=[n,j]
    for i in range(n):
        num = data_list[i]-data_list[i+1]
        if num<0 :
            break
        data_list.append(num)
    # print(data_list)
    if len(max_list) < len(data_list):
        max_list = data_list
    # print(max_list)
print(len(max_list))
print(' '.join(list(map(str,max_list))))