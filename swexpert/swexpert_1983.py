#1983 조교의 성적 매기기
#띄어쓰기 있는 input 받아들이기
#map(f,L)은 L에 있는 원소에 각각 f를 적용.
#map(int, ["12","34","56"])을 하면 int("12"), int("34"),int("56")이 나온다...
# N,K= list(map(int,input().split())) 이렇게 하면 하나씩 들어간다..
# A,B,C ="CAR"  "CAR" 배열이 있으면 A, B, C 변수에 각각 하나씩 들어가는거야..
T=int(input())
for m in range(T):
    N,k= list(map(int,input().split()))
    score=[] #이걸 갯수를 맞춰서 초기화 해주지 않으면 나중에는 append로 해줘야행
    for studentNum in range(N):
        a,b,c = map(int,input().split())
        #score.append(round((0.35*a+0.45*b+0.2*c),2)) #이렇게 하면 소수점두자리까지 반올림된 숫자를 갖게됨.
        #score.append("{0:0.2f}".format(0.35*a+0.45*b+0.2*c),2))) 이거는 값이 str형태로 들어가게 됨...
        score.append(0.35*a+0.45*b+0.2*c) #어차피 값 안보여주는 거라.. 이거 써도 될듯. .
    score_k_stud=score[k-1]  # k번째 학생의 점수는?!
    print(score)
    print(score_k_stud)

    #k번째 학생이 몇등인지 보자
    new_score=sorted(score,reverse=True) # sorted(리스트) 하면 리스트 정렬
    print(new_score)
    rank = new_score.index(score_k_stud)  #리스트.index(값)  값의 index번호 찾기
    print(rank)


    score_type=['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']  ##등급 얼마나 주는지
    new_score_type=[]
    for i in range(10):
        for j in range(N//10):
            new_score_type.append(score_type[i])

    print("#{} {}".format(m,new_score_type[rank]))
