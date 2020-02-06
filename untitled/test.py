#1493 수의 새로운 연산

x_1 =[1]
for i in range(1,300):
    x_1.append(x_1[-1]+i)
x_1.insert(0,0)  # 좌표축 맞추려고 0 집어넣음
a,b =list(map(int,input().split()))  #숫자 두개 a,b

# a숫자 먼저 x,y좌표 찾기
y1=0
for i in range(300):
    if a < x_1[i]:
        y1=i-1
        break
diff=a-x_1[y1]
y1-=diff
x1=diff+1

# b숫자 먼저 x,y좌표 찾기
y2=0
for i in range(300):
    if b < x_1[i]:
        y2=i-1
        break
diff=b-x_1[y2]
y2-=diff
x2=diff+1

#새로운 것의 좌표
newx=x1+x2
newy=y1+y2

#새로운 숫자
print("{}".format(x_1[newx+newy-1]+newx-1))
