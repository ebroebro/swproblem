#2058 자릿수 더하기
N=int(input())
sum=0
while True :
    if N == 0:
        break
    sum+=N%10
    N//=10
print(sum)