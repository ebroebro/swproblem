#4008 숫자만들기


def backtracking(position): #position은 숫자 0번째말고 idx=1 부터 시작해야할듯
    global min, max,ans
    if sum(oper)==0:
        if ans >max:
            max=ans
        if ans < min:
            min = ans
        return

    for i in range(4):
        if oper[i]>0:
            tmp = ans #계산 전후 차이 두기위해서
            oper[i]-=1
            # ans = cal(ans, numbers[position], operators[i])  # 계산
            if i == 0:
                ans= int(ans + numbers[position])
            elif i==1:
                ans = int(ans - numbers[position])
            elif i==2:
                ans = int(ans * numbers[position])
            elif i==3:
                if numbers[position]:
                    ans = int(ans / numbers[position])
            position+=1 #위치옮기기
            backtracking(position)
            position-=1
            oper[i]+=1
            ans = tmp

T=int(input())
for z in range(T):
    n= int(input())
    oper= list(map(int,input().split()))  #'+','-','*','/'
    numbers=list(map(int,input().split()))
    # print(operators)
    #여기까지 input

    min=987654321
    max=-987654321
    ans=numbers[0]

    backtracking(1)
    # print(min)
    # print(max)
    print("#{} {}".format(z+1,max-min))


    ##처음에는 operator를 하나하나 나열해서 표시하고자 했는데 그러다 보니 중복순열이 발생함
    #  4 0 0 0 의 경우 ++++하나의 경우가 나와야하는데  ++++나눠서 하다보면  4!의 경우를 다 체크해버림