#2063 중간값찾기
n=int(input())
data_list = list(map(int, input().split()))
num=int((n-1)/2)
new_list=sorted(data_list)
print(new_list[num])