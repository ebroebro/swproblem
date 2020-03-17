#5432 쇠막대기 자르기
T=int(input())
for z in range(T):
    data_list = list(input())
    stack=[]
    cnt=0
    i=0
    while True:
        if i >= len(data_list)-1:
            break
        if data_list[i] == '(':
            if data_list[i+1] == ')':
                cnt+=len(stack)
                i+=2
            else:
                stack.append(i)
                i+=1
                cnt+=1
        else:
            stack.pop()
            i+=1
    print("#{} {}".format(z+1,cnt))