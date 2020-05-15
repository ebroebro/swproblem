#5201 컨테이너 운반

t=int(input())
for z in range(t):
    n,m= list(map(int,input().split()))
    n_list=list(map(int,input().split()))
    m_list=list(map(int,input().split()))
    n_list=sorted(n_list)
    m_list=sorted(m_list)
    rslt=0
    while True:
        if len(m_list)==0:
            break
        if len(n_list)==0:
            break
        tmp=m_list[-1]
        if n_list[-1]<=tmp:
            rslt+=n_list[-1]
            m_list.pop()
        n_list.pop()
    print("#{} {}".format(z+1,rslt))