#10158 개미
w,h =list(map(int,input().split()))
p,q = list(map(int,input().split()))
t=int(input())

xrslt= (p+t)%(2*w)
if xrslt > w:
    xrslt=2*w-xrslt

yrslt=(q+t)%(2*h)
if yrslt >h:
    yrslt =2*h - yrslt

print("{} {}".format(xrslt,yrslt))