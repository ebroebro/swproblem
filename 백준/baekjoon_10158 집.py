#10158 개미
w,h = list(map(int,input().split()))
# map_list = [[0 for _ in range(w+1)] for _ in range(h+1)]
p,q = list(map(int,input().split())) # [q][p]
hr=int(input())

dy=[1,-1]  #오른쪽위/ 왼쪽위/오른쪽아래/왼쪽아래
dx=[1,-1]   #바뀐다 느낌은 그 index번호가 1-a 이다 라는 거로 하면 될듯?
a=0
b=0
cnt=0
while True:
    if cnt==hr:
        print("{} {}".format(p,q))
        break
    newp = p + dx[a]
    newq=q+dy[b]
    if 0<=newp<=w and 0<=newq<=h:
        p=newp
        q=newq
        cnt+=1
    if 0<=newp<=w and (newq<0 or newq>h):
        b=1-b
    if 0<=newq<=h and (newp<0 or newp>w):
        a=1-a
    if (newp<0 or newp>w) and (newq<0 or newq>h):
        a=1-a
        b=1-b

