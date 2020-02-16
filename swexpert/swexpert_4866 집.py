#4866 괄호검사
T=int(input())
for z in range(T):
    words=list(input())
    stack=[0]
    check = ['(','{',')','}']
    isOkay=1
    no_name=[]
    for i in range(len(words)):
        if words[i] in check:
            if ((stack[-1]==check[0]) and (words[i]==check[2])) or ((stack[-1]==check[1]) and (words[i]==check[3])) :
                stack.pop()
            elif ((stack[-1]==check[0]) and (words[i]==check[3])) or ((stack[-1]==check[1]) and (words[i]==check[2])) :
                isOkay=0
            else:
                stack.append(words[i])
            # no_name.append(words[i])
    if stack !=[0]:
        isOkay=0
    # print(stack)
    print("#{} {}".format(z+1,isOkay))
    # print(no_name)