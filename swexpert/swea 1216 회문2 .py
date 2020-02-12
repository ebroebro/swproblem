#1216 회문2
import sys
# from pprint import pprint

sys.stdin = open('input.txt','r')

for _ in range(10):
    z= int(input())
    m=100
    map_list=[]
    for _ in range(m):
        map_list.append(list(input()))
    # pprint(map_list)
    max_num =0
    for i in range(m):
        for j in range(0,m):
            for k in range(j,m):
                tmp = map_list[i][j:k+1]
                if tmp == tmp[::-1]:
                    if max_num < len(tmp):
                        max_num=len(tmp)
    # print(max_num)

    hmap=[[0 for _ in range(m)] for _ in range(m)]
    for i in range(m):
        for j in range(m):
            hmap[i][j]=map_list[j][i]

    # print(hmap)
    for i in range(m):
        for j in range(0,m):
            for k in range(j,m):
                tmp = hmap[i][j:k+1]
                if tmp == tmp[::-1]:
                    if max_num < len(tmp):
                        max_num=len(tmp)

    print("#{} {}".format(z,max_num))