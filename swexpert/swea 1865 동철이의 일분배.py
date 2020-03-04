#1865 동철이의 일분배


def f(people, percent):
    global maxP
    if percent <= maxP:    #계속 갈수록 숫자가 결과값이 작아지기 때문에 이미 그 결과값이 작으면 더이상 볼 필요가 없음
        return    #이 두줄 없으면 시간 초과 오류남...
    if people ==n:
        if maxP < percent:
            maxP=percent
        return
    else:
        for j in range(n):
            if j not in visited and map_list[people][j]>0:
                visited.append(j)
                f(people+1,percent*(map_list[people][j]/100))
                visited.pop()

T=int(input())
for z in range(T):
    n=int(input())
    map_list=[list(map(int,input().split())) for _ in range(n)]
    maxP=0
    visited=[]
    f(0,1)
    print("#{} {}".format(z+1,format(round(maxP*100,6),".6f")))