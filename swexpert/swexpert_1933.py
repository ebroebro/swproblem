#1933. 간단한 N의 약수
n=int(input())
result=[]
for i in range(1,n+1):
    if n%i ==0:
        result.append(i)
new_result = list(map(str, result))
print(' '.join(new_result))