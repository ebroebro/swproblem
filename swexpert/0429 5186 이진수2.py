#5186 이진수2
t=int(input())
for z in range(t):
    data=float(input())
    rslt=[]
    while True:
        data*=2
        if data>1:
            rslt.append(1)
            data-=1
        elif data == 1:
            rslt.append(1)
            print("#{} {}".format(z+1,''.join(list(map(str,rslt)))))
            break
        else:
            rslt.append(0)
        if len(rslt)>12:
            print("#{} overflow".format(z+1))
            break

