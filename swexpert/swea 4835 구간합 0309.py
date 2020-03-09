T=int(input())
for z in range(T):
    n,m = list(map(int,input().split()))
    numbers = list(map(int,input().split()))
    sum_number=0
    for i in range(m):
        sum_number+=numbers[i]
    min=sum_number
    max=sum_number

    for i in range(m,n):
        sum_number+=numbers[i]
        sum_number-=numbers[i-m]
        if sum_number > max:
            max=sum_number
        if sum_number < min:
            min=sum_number
    print("#{} {}".format(z+1,max-min))