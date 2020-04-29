#5185 이진수

t=int(input())
for z in range(t):
    print("#{} ".format(z+1), end='')
    a, data_list=input().split()
    a= int(a)
    data_list=list(data_list)

    for data in data_list:
        if data.isnumeric():
            data = int(data)
        else:
            data = ord(data) - ord('A') + 10
        for i in range(3,-1,-1):
            if data:
                rslt=data//(pow(2,i))
                data=data%(pow(2,i))
                print(rslt,end='')
            else:
                print(0,end='')
    print()
