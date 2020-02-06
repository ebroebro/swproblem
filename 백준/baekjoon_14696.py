#14696. 딱지놀이
T=int(input())
for z in range(T):
    a_input = list(map(int,input().split()))
    b_input = list(map(int,input().split()))

    Alist=[0 for _ in range(5)]
    Blist=[0 for _ in range(5)]

    for i in range(1,a_input[0]+1):
        Alist[a_input[i]]+=1
    for i in range(1,b_input[0]+1):
        Blist[b_input[i]]+=1

    winner ='D'
    for i in range(4,0,-1):
        if Alist[i]>Blist[i]:
            winner='A'
            break
        if Alist[i]<Blist[i]:
            winner='B'
            break
    print(winner)