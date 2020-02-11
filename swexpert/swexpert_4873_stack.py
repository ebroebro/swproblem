#4873 반복문자 지우기
T=int(input())
for z in range(T):
    words=list(input())
    length=len(words)
    stack=[words[0]]
    for i in range(1,len(words)):
        if len(stack):
            if words[i] == stack[len(stack)-1]:
                stack.pop()
            else:
                stack.append(words[i])
        else:
            stack.append(words[i])
    # print(stack)
    print("#{} {}".format(z+1,len(stack)))
