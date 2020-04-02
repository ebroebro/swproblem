#5097 회전
T=int(input())
for z in range(T):
    n,m= list(map(int,input().split()))
    data_list = [0 for i in range(100000)]
    tmp_list =list(map(int,input().split()))
    for i in range(n):
        data_list[i]=tmp_list[i]
    front=-1
    rear=n-1
    for i in range(m):
        front+=1
        tmp=data_list[front]
        rear+=1
        data_list[rear]=tmp
    print("#{} {}".format(z+1,data_list[front+1]))