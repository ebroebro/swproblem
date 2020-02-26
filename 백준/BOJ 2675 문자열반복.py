#2675 문자열 반복
T=int(input())
for _ in range(T):
    n,data = input().split()
    n=int(n)
    for i in data:
        for _ in range(n):
            print(i,end='')
    print()