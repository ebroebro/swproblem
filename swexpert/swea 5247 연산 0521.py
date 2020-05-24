#5247 연산
from collections import deque


t = int(input())
for z in range(1,t+1):
    n, m = map(int, input().split())
    Q = deque()
    Q.append((n, 0))
    num_lst = [0] * 1000001
    num_lst[n] = 1
    min_cnt = 0
    while Q:
        num, cnt = Q.popleft()
        if num == m:
            min_cnt = cnt
            break

        for i in range(4):
            tmp_num = 0
            if i == 0:
                tmp_num = num + 1
                if 0 < tmp_num <= 1000000 and num_lst[tmp_num] != 1:
                    Q.append((tmp_num, cnt + 1))
                    num_lst[tmp_num] = 1

            elif i == 1:
                tmp_num = num - 1
                if 0 < tmp_num <= 1000000 and num_lst[tmp_num] != 1:
                    Q.append((tmp_num, cnt + 1))
                    num_lst[tmp_num] = 1

            elif i == 2:
                tmp_num = num * 2
                if 0 < tmp_num <= 1000000 and num_lst[tmp_num] != 1:
                    Q.append((tmp_num, cnt + 1))
                    num_lst[tmp_num] = 1

            elif i == 3:
                tmp_num = num - 10
                if 0 < tmp_num <= 1000000 and num_lst[tmp_num] != 1:
                    Q.append((tmp_num, cnt + 1))
                    num_lst[tmp_num] = 1
    print("#{} {}".format(z,min_cnt))