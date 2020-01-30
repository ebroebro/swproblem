#1966 숫자를 정렬하자
T=int(input())
for z in range(T):
    N= int(input())
    input_data=list(map(int, input().split()))
    result = sorted(input_data)
    print(result)
    print("#{} {}".format(z+1,' '.join(list(map(str, result)))))