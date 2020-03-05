#3752 시험 가능한 점수
def f(idx, score):
    global cnt
    if idx == n+1:
        if score not in score_list:
            cnt+=1
            score_list.append(score)
        return
    else:
        f(idx+1,score+data_list[idx])
        f(idx+1,score)

T=int(input())
for z in range(T):
    n=int(input())
    data_list = [0]+list(map(int,input().split())) # 맨앞에 0 추가해서 판단하기
    cnt=0
    score_list=[]
    f(0,0)
    print("#{} {}".format(z+1,cnt))
