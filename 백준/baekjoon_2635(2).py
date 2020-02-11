#2635 수 이어가기
n = int(input())
max_list=[n]
for i in range(1,n):
    data_list=[n,i]
    while True:
        num = data_list[len(data_list)-1]+data_list[len(data_list)-2]
        if num <0 :
            break
        else:
            data_list.append(num)
    if len(max_list) < len(data_list):
        max_list = data_list



print(len(max_list))
for e in max_list:
    print(e, end= ' ')
print()
