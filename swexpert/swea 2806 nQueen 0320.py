#2806 nQueen
def f(post):
    global cnt
    if post ==n:
        cnt+=1
        return
    for i in range(n):
        if i not in visited and (i-post) not in cross and (i+post) not in cross2:
            visited.append(i)
            cross.append(i-post)
            cross2.append(i+post)
            f(post+1)
            visited.pop()
            cross.pop()
            cross2.pop()
T=int(input())
for z in range(T):
    n=int(input())
    visited=[]
    cross=[] #차이
    cross2=[] #합
    cnt=0
    f(0)
    print("#{} {}".format(z+1,cnt))