#10158 개미
w,h = list(map(int,input().split()))
p,q = list(map(int,input().split())) # [q][p]
hr=int(input())

x=p+hr
y=q+hr
if x > w:
    x-=w