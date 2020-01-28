#4828 min max
T=int(input())
for i in range(T):
    n= int(input())
    data_list= list(map(int,input().split()))
    max=1
    min=1000000
    for j in data_list:
        if max< j:
            max=j
            print(max)
        if min>j:
            min=j
            print(min)
    result = max-min
    print("#{0} {1}".format(1+i,result))