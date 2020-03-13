#4613 러시아 국기 같은 깃발
from pprint import pprint

n,m = list(map(int,input().split()))
map_list = [list(input()) for _ in range(n)]

color = ['W','B','R'] #이 순서대로 해보자..
color_flag=['W','R']
flag=0 #blue가 0이면 w 가능 1이면 r이 가능
cnt=0

#맨 위줄은 w로 아래줄은 R로
for j in range(m):
    if map_list[0][j]!='W':
        map_list[0][j]='W'
        cnt+=1
    if map_list[n-1][j]!='R':
        map_list[n-1][j]='R'
        cnt+=1

# print(cnt)
# pprint(map_list)

def color_change(data_list,col):
    global cnt3,flag
    cnt3=0
    if col=='B':
        flag=1
    if col=='R':
        flag=2
    for i in range(len(data_list)):
        if data_list[i]!=col:
            data_list[i]=col
            cnt3+=1

min_cnt=987654321
def f(post,cnt2):
    global min_cnt
    if post == n-1:
        if flag==0:
            return
        elif cnt2 <min_cnt:
            min_cnt=cnt2
        return
    else:
        if flag ==0:
            #흰색 칠하기
            tmp_list = map_list[post]
            color_change(tmp_list,'W') #흰색으로 하면 몇개나 바뀌니
            f(post+1,cnt2+cnt3)
            #파란색 칠하기
            tmp_list = map_list[post]
            color_change(tmp_list,'B')
            f(post+1,cnt2+cnt3)
        elif flag==1:
            #파란색 칠하기
            tmp_list = map_list[post]
            color_change(tmp_list, 'B')
            f(post + 1, cnt2 + cnt3)
            #빨간색 칠하기
            tmp_list = map_list[post]
            color_change(tmp_list, 'R')
            f(post + 1, cnt2 + cnt3)
        elif flag==2:
            # 빨간색 칠하기
            tmp_list = map_list[post]
            color_change(tmp_list, 'R')
            f(post + 1, cnt2 + cnt3)

f(1,0)
cnt+=min_cnt
print(cnt)



