#4008 숫자만들기

# def cal(n1,n2,op):
#     if op == '+':
#         return int(n1+n2)
#     elif op =='-':
#         return int(n1-n2)
#     elif op =='*':
#         return int(n1*n2)
#     elif op == '/':
#         return int(n1/n2)

def backtracking(position): #position은 숫자 0번째말고 idx=1 부터 시작해야할듯
    global min, max,ans
    if 0 not in visited:
        if ans >max:
            max=ans
        if ans < min:
            min = ans
        return

    for i in range(len(operators)):
        if visited[i]==0:
            tmp = ans #계산 전후 차이 두기위해서
            visited[i]=1 #방문
            # ans = cal(ans, numbers[position], operators[i])  # 계산
            if operators[i] == '+':
                ans= int(ans + numbers[position])
            elif operators[i] == '-':
                ans = int(ans - numbers[position])
            elif operators[i] == '*':
                ans = int(ans * numbers[position])
            elif operators[i] == '/':
                if numbers[position]:
                    ans = int(ans / numbers[position])
            position+=1 #위치옮기기
            backtracking(position)
            position-=1
            visited[i]=0
            ans = tmp

T=int(input())
for z in range(T):
    n= int(input())
    oper= list(map(int,input().split()))  #'+','-','*','/'
    numbers=list(map(int,input().split()))
    operators=[]
    for _ in range(oper[0]):
        operators.append('+')
    for _ in range(oper[1]):
        operators.append('-')
    for _ in range(oper[2]):
        operators.append('*')
    for _ in range(oper[3]):
        operators.append('/')
    # print(operators)
    #여기까지 input

    min=987654321
    max=-987654321
    visited=[0]*len(operators)
    ans=numbers[0]

    backtracking(1)
    # print(min)
    # print(max)
    print("#{} {}".format(z+1,max-min))