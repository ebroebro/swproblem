T=int(input())
for z in range(T):
    n=int(input())
    numbers=list(map(int,input().split()))
    new_list=[]
    for _ in range(5):
        new_list.append(max(numbers))
        numbers.remove(max(numbers))
        new_list.append(min(numbers))
        numbers.remove(min(numbers))
    print("#{}".format(z+1),end=' ')
    print(*new_list)