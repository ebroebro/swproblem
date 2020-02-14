#2806 n queen
def nQueen(here):
    global cnt, row, check1, n, check2
    if here == n:
        cnt += 1
        return

    for j in range(n):
        if j not in row and (here - j not in check1) and (here + j not in check2):
            row[here] = j
            check1[here] = here - j
            check2[here] = here + j
            nQueen(here + 1)
            row[here] = 9999
            check1[here] = 9999
            check2[here] = 9999

T=int(input())
for z in range(T):
    n= int(input())
    row = [9999 for _ in range(n)]
    check1 = [9999 for _ in range(n)]
    check2 = [9999 for _ in range(n)]
    here=0
    visited=[]
    cnt=0


    nQueen(0)
    print("#{} {}".format(z+1,cnt))