#1979 어디에 단어가 들어수 있을까
def check(data):
    cnt=0
    #가로
    for i in range(N):
        check=0
        for j in range(N):
            if data[i][j]==0:
                check=0
            if data[i][j]==1:
                check +=1
                if check ==K:
                    if j !=N-1 :
                        if data[i][j+1]==0:
                            cnt+=1
                            check=0
                    else:
                        cnt+=1
                        break


    #세로
    for j in range(N):
        check=0
        for i in range(N):
            if data[i][j]==0:
                check=0
            if data[i][j]==1:
                check +=1
                if check ==K:
                    if i !=N-1 :
                        if data[i+1][j]==0:
                            cnt+=1
                            check=0
                    else:
                        cnt+=1
                        break
    return cnt

T= int(input())
for z in range(T):
    N,K = list(map(int,input().split()))
    data=[]
    for i in range(N):
        data.append(list(map(int,input().split())))
    print("#{} {}".format(z+1,check(data)))
