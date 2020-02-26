#2164 수찾기
n=int(input())
check = list(map(int,input().split()))
m=int(input())
data= list(map(int,input().split()))

for i in data:
    ans=0
    for j in check:
        if i ==j:
            ans=1
            break
    print(ans)