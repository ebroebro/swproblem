#1204. 최빈수 구하기

'''
생각 정리
주어진 리스트에서 다 카운트해서 최대값을 구한다.?
만약 max 값보다 그 cnt 값이 더 크다면?
그때의 data[i] 값을 max_num에 넣는다
만약 같다면 ? max_num과 data[i]를 비교한다.
그러고 큰거를 max_num에다가 넣기
'''
T=int(input())
for i in range(T):
    num=int(input())
    data=list(map(int, input().split()))
    max_cnt=0
    max_num=0
    for i in range(len(data)):
        if max_cnt < data.count(data[i]):
            max_cnt= data.count(data[i])
            max_num=data[i]
        elif max_cnt == data.count(data[i]):
            if max_num < data[i]:
                max_num =data[i]
    print("#{} {}".format(num, max_num))