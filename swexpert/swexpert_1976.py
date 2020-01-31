#1976. 시각 덧셈
# T=int(input())
# for z in range(T):


h1,m1,h2,m2 = list(map(int,input().split()))
h,m = 0,0
h=h1+h2
m=m1+m2
if h >12:
    h-=12
if m >=60:
    m-=60
    h+=1




    # print("#{} {} {}".format(z+1,h,m))