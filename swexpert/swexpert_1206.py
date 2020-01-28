#1206
# import sys
# sys.stdin = open("1206input.txt","r")

T=10
for j in range(T):
    N= int(input())
    list_data = list(map(int, input().split()))
    #cnt = [0] * len(list_data)
    cnt=0
    for i in range(2, N - 2):
        while (list_data[i] > list_data[i - 1]) and (list_data[i] > list_data[i - 2]) and (
                list_data[i] > list_data[i + 1]) and (list_data[i] > list_data[i + 2]):
            list_data[i] -= 1
            cnt+=1
            #cnt[i] += 1
    #print("#{0} {1}".format(j+1, sum(cnt)))
    print("#{0} {1}".format(j + 1, cnt))