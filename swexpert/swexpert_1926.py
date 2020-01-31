#1926. 간단한 369게임
N=int(input())
nums=[i for i in range(1,N+1)]
str_nums=list(map(str, nums))
cnt=[0]*N
for i in range(N):
    if '3' in str_nums[i]:
        cnt[i] += str_nums[i].count('3')
    if '6' in str_nums[i]:
        cnt[i] += str_nums[i].count('6')
    if '9' in str_nums[i]:
        cnt[i] += str_nums[i].count('9')
for i in range(N):
    if cnt[i]==0 :
        pass
    elif cnt[i] > 0 :
        str_nums[i]='-'*cnt[i]
print(' '.join(str_nums))