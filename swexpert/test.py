n=int(input())
a,b=n-1,n
while True :
    c=(a+b)/2
    if c**2 > n :
        b=c
    elif c**2 <n :
        a=c
    if round(a,5)==round(b,5):
        print(a)
        break