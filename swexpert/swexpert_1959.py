#1959.두개의 숫자열
T=int(input())
for z in range(T):
    N, M = list(map(int, input().split()))
    data1=list(map(int, input().split()))
    data2=list(map(int, input().split()))

    if len(data1)>len(data2):
        A=data2
        B=data1
    else:
        A = data1
        B = data2
    max=0
    for i in range(len(B)-len(A)+1):
        sum = 0
        for j in range(len(A)):
            sum+=A[j]*B[j+i]
        if max < sum :
            max=sum
    print("#{} {}".format(z+1,max))