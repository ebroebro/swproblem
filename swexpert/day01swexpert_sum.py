from pprint import pprint

def max_sum(data):
    max = 0
    #가로
    for i in range(100):
        if max < sum(data[i]):
            max=sum(data[i])

    #세로
    for j in range(100):
        tot=0
        for i in range(100):
            tot+=data[i][j]
        if max <tot:
            max=tot

    #대각선1
    tot=0
    for i in range(100):
        tot+=data[i][i]
    if max<tot:
        max=tot
    #대각선2
    tot=0
    for i in range(1,100):
        tot+=data[i][99-i]
    if max<tot:
        max=tot

#대각선 왜
# data[x][x] 이건 안대져??

    return max



for z in range(10):
    n=int(input())
    data = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(100):
         data[i]=list(map(int, input().split()))
    print("#{} {}".format(n,max_sum(data)))