#1984. 중간 평균값 구하기

T=int(input())
for z in range(T):
    nums=list(map(int, input().split()))
    minmax=[]
    minmax.append(max(nums))
    minmax.append(min(nums))
    new_nums=[i for i in nums if i not in minmax]
    print("#{} {}".format(z+1,round((sum(new_nums)/len(new_nums)))))