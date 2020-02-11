#4866 괄호검사
T=int(input())
for z in range(T):
    data=list(input())
    top=-1
    howmany=len(data)
    stack=[]
    Info=[0]*128 #특수부호는 128
    Info[ord(')')]='('
    Info[ord('}')]='{'
    data_list=['(',')','[',']']

    isOkay=1

    for now in range(howmany):
        if data[now] in data_list:
            if data[now]=='('or data[now]=='{':
                stack.append(data[now])
            elif Info[ord(data[now])] == stack[len(stack)-1]:
                stack.pop()
            elif Info[ord(data[now])] != stack[len(stack)-1]:
                isOkay=0
                break
    if stack:
        isOkay=0

    print("#{} {}".format(z+1,isOkay))