#1244. 스위치 켜고 끄기
def change_switch(switch,n,m):
    for z in range(m):
        b, a = list(map(int, input().split()))
        if b==1 :
            for i in range(len(switch)):
                if (i+1)%a == 0:
                    switch[i] = (switch[i] ^ 1)

        if b==2 :
            a=a-1
            blaa=0
            for i in range(n):
                start=a-i
                end=a+i
                if start>=0 and end<n:
                    if switch[start]==switch[end]:
                        blaa= i
                        # print(c)
                        # print("{} {}".format(start,end))
                    else:
                        break
                else:
                    break

            if blaa!=0 :
                for i in range(a-blaa,a+blaa+1):
                    switch[i] = (switch[i] ^ 1)
            else:
                switch[a] = (switch[a]^1)
    return switch

n= int(input())
switch= list(map(int,input().split()))
m= int(input())
print(' '.join(list(map(str,change_switch(switch,n,m)))))