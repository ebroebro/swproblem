T = int(input())
for test_case in range(1, T + 1):
    K,N,M = map(int,input().split())
    station = list(map(int,input().split()))
    nosun = [0]*(N+1)
    for i in station:
        nosun[i] +=1
    start = 0
    cnt = 0
    end = K
    while True:
        zero  = 0
        for i in range(start+1, end+1):
            if nosun[i] ==1:
                start = i
            else:
                zero +=1
        if zero ==K:
            cnt = 0
            break
        cnt +=1
        end = K+start
        if end>=N:
            break
    print('#{0} {1}'.format(T,cnt))