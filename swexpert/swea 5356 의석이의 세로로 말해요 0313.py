#5356 의석이의 세ㅗㄹ로 말해요
from pprint import pprint

T=int(input())
for z in range(T):
    map_list=[list(input()) for _ in range(5)]
    max_len=0
    for i in range(5):
        if max_len < len(map_list[i]):
            max_len = len(map_list[i])

    new_list=[[987654321 for i in range(max_len)] for _ in range(5)]

    for i in range(5):
        for j in range(max_len):
            if j < len(map_list[i]):
                new_list[i][j]=map_list[i][j]
    # pprint(new_list)
    print("#{}".format(z+1), end=' ')
    for i in range(max_len):
        for j in range(5):
            if new_list[j][i] !=987654321:
                print(new_list[j][i],end='')
    print('')
