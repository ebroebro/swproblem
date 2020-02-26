#BOJ 2920 음계
data= list(map(int,input().split()))
check_as = sorted(data)
check_de = check_as[::-1]
ans = 'mixed'
if check_as ==data:
    ans='ascending'
if check_de == data:
    ans='descending'
print(ans)