#태혁이의 사랑은 타이밍


def m_check(D,H,M):
    if D < d:
        return -1
    else:
        H+=24*(D-d)
        if H <h :
            return -1
        else:
            M+= 60*(H-h)
            if M <m :
                return-1
            else:
                return M-m

T=int(input())
for z in range(T):
    D,H,M = list(map(int,input().split()))
    d,h,m=11,11,11
    print("#{} {}".format(z+1,m_check(D,H,M)))
