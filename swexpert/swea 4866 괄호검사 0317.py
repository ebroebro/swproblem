#1979 단어가 어디에 들어갈 수 있을까
T=int(input())
for z in range(T):
    data_list = list(input())
    stack=[0]  #이렇게 한 이유... 처음부터 } ) 나오는 경우까지 고려해 주려고 미리 하나를 넣어둔다.
    check=['(','{',')','}']
    flag=1
    for char in data_list:
        if char in check:
            if char == '(' or char=='{':
                stack.append(char)
            else:
                if stack[-1]!=check[check.index(char)-2]:
                    flag=0
                    break
                else:
                    stack.pop()
    if stack!=[0]:
        flag=0
    print("#{} {}".format(z+1,flag))
