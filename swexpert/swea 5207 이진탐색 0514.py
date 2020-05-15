#5207 이진탐색

t=int(input())
for z in range(t):
    n,m = list(map(int,input().split()))
    n_list=sorted(list(map(int,input().split())))  # 정렬해야하나? 해야하네
    m_list=list(map(int,input().split()))

    cnt=0
    for num in m_list:
        start=0
        end=n-1
        flag=0
        while True : # 조건이 있어야하나?
            mid=(start+end)//2

            if n_list[mid]==num:
                cnt+=1
                break
            #오른쪽
            elif n_list[mid]<num:
                if flag==1:
                    break
                start=mid+1
                flag=1
            elif n_list[mid]>num:
                if flag==-1:
                    break
                end=mid-1
                flag=-1

    print("#{} {}".format(z+1,cnt))
