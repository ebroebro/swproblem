#swea 3349 최소값으로 이동하기_2
T=int(input())
for z in range(T):
    w,h,n=list(map(int,input().split()))
    map_list=[]
    for _ in range(n):
        a,b=list(map(int,input().split()))
        map_list.append([a-1,b-1])
    cnt=0
    for i in range(n-1): #start는 map_list[i] 도착지는 map_list[i+1]로 할꺼임
        posta=map_list[i][0]
        postb=map_list[i][1]
        while posta!=map_list[i+1][0] or postb!=map_list[i+1][1]:
            if (posta-map_list[i+1][0])*(postb-map_list[i+1][1])>0:
                if posta>map_list[i+1][0]:
                    posta-=1
                    postb-=1
                elif posta<map_list[i+1][0]:
                    posta+=1
                    postb+=1
                cnt+=1
            else:
                cnt+=abs(posta-map_list[i+1][0])
                cnt+=abs(postb-map_list[i+1][1])
                break
    print("#{} {}".format(z+1,cnt))