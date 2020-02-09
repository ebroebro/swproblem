#2635 수 이어가기
n = int(input())
max_list=[]
for j in range(n+1):
    data_list=[n,j]
    i=0
    while True  # for문으로 했었는데 이게 잘못된듯.2만 하더라도 21101 이라서 2번 넘어 버리네..
        num = data_list[i]-data_list[i+1]
        if num<0 :
            break
        data_list.append(num)

        if len(max_list) < len(data_list):
            max_list = data_list
        i+=1
print(len(max_list))
print(*max_list)
