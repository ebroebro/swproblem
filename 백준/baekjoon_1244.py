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

# 1<-> 0 바꾸기  1-a 하면 편하네... ㄷㄷ

## 출력 형식도 잘 좀 보자......
#20개씩 출력하기
# ans = list(map(str,change_switch(switch,n,m)))
# start=0
# while True:
#     if len(ans[start:])>=20:
#         print(' '.join(ans[start:20]))
#         start+=20
#     else :
#         print(' '.join(ans[start:]))
#         break

for i,e in enumerate(change_switch(switch,n,m)):
    if i and not(i%20):  #i 가 존재하고 그 i가 20의 배수라면? print()한번 넣어주는거
        print()
    print(e,end=" ")


    '''    
for i in range(0,howmany,20):   인쇄 이렇게도 되네 ..
    print(*switch[i:i+20])
디버깅
'F8' 한줄씩 변수값 바뀌는 거 볼수 있음

'''