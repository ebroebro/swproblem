#4837.부분집합의 합
def subset_cnt(n,k):
    data_set = [i for i in range(1, 13)]
    cnt=0
    for i in range(2**12):
        subset=[]
        for j in range(13):    ## 이거 (1,13) 하고 , ,, 그냥 j값을 쓰면 안되는 이유.. 그러면 000000000이거빠짐..
            if i& (1<<j):
                subset.append(data_set[j])
        # print(subset)
        if len(subset)==n and sum(subset)==k:
            cnt+=1
    return cnt


T=int(input())
for z in range(T):
    n, k = list(map(int, input().split()))
    print("#{} {}".format(z+1,subset_cnt(n,k)))