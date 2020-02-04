#2559. 수열

n, k = list(map(int, input().split()))
data= list(map(int,input().split()))

data_list=[]
for i in range(n-k):
    data_list.append(sum(data[i:i+k]))
print(max(data_list))