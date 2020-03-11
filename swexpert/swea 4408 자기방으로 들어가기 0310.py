T=int(input())
for z in range(T):
    n=int(input())
    before_list=[]
    after_list=[]
    for _ in range(n):
        a,b=list(map(int,input().split()))
        #짝수면 1을 빼서 숫자 맞춰주기
        if a%2==0:
            a-=1
        if b%2==0:
            b-=1
        before_list.append(min(a,b)//2) # //2를 통해서 홀짝 하나임을 나타냄 복도 번호
        after_list.append(max(a,b)//2)  #무조건 작은 번호에서 큰 번호로 가게 만들어 놨음...

    #복도 겹치는 횟수가 얼마인지 표시를 해볼거임..
    corridor = [0 for _ in range(max(max(before_list),max(after_list)+1))]  #방수가 400이니 idx가 0부터 199인 복도가 있다. #끝값은 그냥 최대값으로 해도 될듯
    for i in range(n):
        for j in range(before_list[i],after_list[i]+1):
            corridor[j]+=1

    print("#{} {}".format(z+1,max(corridor)))  #가장 많이 겹치는 경우의 복도 수만큼 시간이 걸리네