#1952 수영장




def f(now, sum):
    global minPrice
    if now >12 :
        if minPrice > sum:
            minPrice =sum
            return
    else:
        # f(now+1,sum+day*use_days[now])# 이거는 어차피 now+1이 같으니까 ,, 둘중 작은 걸 보내주도록 하면 되겠다.
        if min(day*use_days[now],month)+sum <= minPrice:
            f(now+1,min(day*use_days[now],month)+sum)
        f(now+3,sum+month3)
T=int(input())
for z in range(T):
    day, month, month3, year=list(map(int,input().split())) #1일, 1달, 3달, 1년
    use_days= [0]+list(map(int,input().split()))  #1월 ~ 12월
    minPrice=year #1년 비용권비용을 초기 최소값으로 두기
    f(1,0)  #f(월,sum)
    print("#{} {}".format(z+1,minPrice))