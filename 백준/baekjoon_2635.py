#2635 수 이어가기
n = int(input())
max_list=[]
for j in range(n+1):
    data_list=[n,j]
    for i in range(n):
        num = data_list[i]-data_list[i+1]
        if num<0 :
            break
        data_list.append(num)

        if len(max_list) < len(data_list):
            max_list = data_list

print(len(max_list))
for e in max_list:
    print(e, end= ' ')
print()
