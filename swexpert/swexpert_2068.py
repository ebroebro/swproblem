#2068 최대수 구하기
T= int(input())
for z in range(T):
    data_list = list(map(int,input().split()))
    max=data_list[0]
    for i in data_list:
        if max<i:
            max=i
    print("#{} {}".format(z+1,max))