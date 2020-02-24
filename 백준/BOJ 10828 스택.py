#10828 스택
stack =[]
T=int(input())
for _ in range(T):
    tmp = input()
    if tmp[:4]=='push':
        p,n = tmp.split()
        stack +=[n]
        # print(stack)
    elif tmp =='pop':
        if len(stack):
            print(stack[-1])
            del stack[-1]
        else:
            print(-1)
    elif tmp == 'size':
        print(len(stack))
    elif tmp =='empty':
        if len(stack):
            print(0)
        else:
            print(1)
    elif tmp =='top':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)