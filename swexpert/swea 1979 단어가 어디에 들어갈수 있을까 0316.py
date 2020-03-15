#1979 단어가 어디에 들어갈 수 있을까
T=int(input())
for z in range(T):
    n,k = list(map(int,input().split()))
    map_list= [list(map(int,input().split())) for _ in range(n)]
    rotate_list= list(map(list,zip(*map_list)))
    rslt_cnt=0
    for i in range(n):
        for start in range(n-k+1):
            if map_list[i][start]==1:
                cnt=0
                for j in range(k):
                    if start+j>=n:
                        break
                    elif map_list[i][start+j]==0:
                        break
                    else:
                        cnt+=1
                if cnt == k:
                    if start+k>=n:
                        if start == 0:
                            rslt_cnt += 1
                        elif map_list[i][start - 1] == 0:
                            rslt_cnt += 1
                    elif map_list[i][start+k]==0:
                        if start==0:
                            rslt_cnt+=1
                        elif map_list[i][start-1]==0:
                            rslt_cnt+=1
            if rotate_list[i][start] == 1:
                cnt = 0
                for j in range(k):
                    if start + j >= n:
                        break
                    elif rotate_list[i][start + j] == 0:
                        break
                    else:
                        cnt += 1
                if cnt == k:
                    if start + k >= n:
                        if start == 0:
                            rslt_cnt += 1
                        elif rotate_list[i][start - 1] == 0:
                            rslt_cnt += 1
                    elif rotate_list[i][start + k] == 0:
                        if start == 0:
                            rslt_cnt += 1
                        elif rotate_list[i][start - 1] == 0:
                            rslt_cnt += 1
    print("#{} {}".format(z+1,rslt_cnt))