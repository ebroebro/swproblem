#4880 토너먼트 카드게임

def rock_paper(a,b):  #번호를 넣자
    global winner
    tmp1 = data_list[a]
    tmp2 = data_list[b]
    if tmp1 != tmp2:
        if tmp1 == 1:
            if tmp2 == 2:
                winner = b
            else:
                winner = a
        elif tmp1 == 2:
            if tmp2 == 3:
                winner =b
            else:
                winner =a
        elif tmp1==3:
            if tmp2 == 1:
                winner =b
            else:
                winner =a
    else:
        winner = min(a,b)
    return winner

def cardgame(start,end):
    if start==end:
        return start
    a=cardgame(start,(end+start)//2)
    b=cardgame((start+end)//2+1,end)
    return rock_paper(a,b)

T=int(input())
for z in range(T):
    n=int(input())
    data_list=list(map(int,input().split()))
    print("#{} {}".format(z+1,cardgame(0,n-1)+1))