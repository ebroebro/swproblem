#2563 색종이
from pprint import pprint
###나는 이거를 걍 안에 있으면 1로 바꾸고
##1을 count해보겠다.
paper = [[0 for i in range(100)] for i in range(100)]
pprint(paper)
n = int(input())
for i in range(n):
    a,b = list(map(int,input().split()))
    for i in range(a,a+10):
        for j in range(b,b+10):
            paper[i][j]=1

pprint(paper)

cnt=0
for i in range(100):
    for i in range(100):
        if paper[i][j]==1:
            cnt+=1
print(cnt)