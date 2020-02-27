#1258 행렬 찾기

T=int(input())
for z in range(T):
    n= int(input())
    map_list =[]
    for i in range(n):
        data_list = list(map(int,input().split()))
        map_list.append(data_list)
    #map_list 만들어 놨음

    rslt=[]
    # visited=[]
    for i in range(n):
        for j in range(n):
            if map_list[i][j]!=0:
                tmpi = i
                while True:
                   if tmpi>=n or map_list[tmpi][j]==0:
                       break
                   tmpj = j
                   while True:
                       if tmpj>=n or map_list[tmpi][tmpj]==0:
                           break
                       map_list[tmpi][tmpj]=0
                       tmpj+=1
                   tmpi+=1
                rslt.append([tmpi-i,tmpj-j])



    #아래 rslt가 있으면 순서맞춰서 바꿔주는 역할
    for i in range(len(rslt)):
        for j in range(i,len(rslt)):
            if rslt[i][0]*rslt[i][1]>rslt[j][0]*rslt[j][1]:
                rslt[i],rslt[j]=rslt[j],rslt[i]
            elif rslt[i][0]*rslt[i][1]==rslt[j][0]*rslt[j][1] and rslt[i][0]>rslt[j][0]:
                rslt[i], rslt[j] = rslt[j], rslt[i]

    print("#{}".format(z+1),end='')
    print(" {}".format(len(rslt)),end='')
    for i in range(len(rslt)):
        for j in range(2):
            print(" {}".format(rslt[i][j]),end='')
    print()