#1979 단어가 어디에 들어갈 수 있을까
T=int(input())
for z in range(T):
    data_list=list(input())
    while True:
        flag = 1
        for i in range(len(data_list)-1):
            if data_list[i]==data_list[i+1]:
                del data_list[i]
                del data_list[i]
                flag=0
                break
        if flag ==1:
            break
    print("#{} {}".format(z+1,len(data_list)))