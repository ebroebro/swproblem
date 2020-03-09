T=int(input())
for z in range(T):
    n=int(input())
    data_list = list(map(int,input().split()))
    max=0
    min=987654321
    for i in range(n):
        if data_list[i]>max:
            max= data_list[i]
        if data_list[i]<min:
            min = data_list[i]
    print("#{} {}".format(z+1,max-min))