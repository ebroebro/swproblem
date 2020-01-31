#1948. 날짜 계산기
T=int(input())
for z in range(T):
    m_d = {1:31,2:28 ,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

    m1,d1,m2,d2 = list(map(int,input().split()))
    day=0
    for i in range(m1,m2):
        day+=m_d[i]
    day=day-d1+d2+1
    print("#{} {}".format(z+1,day))