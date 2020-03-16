#4874 forth
def cal(n1,n2,oper):
    global flag
    if oper=="+":
        return int(n1)+int(n2)
    elif oper =="-":
        return int(n1)-int(n2)
    elif oper =="*":
        return int(n1)*int(n2)
    elif oper =="/":
        if n2==0:
            flag=1
        else:
            return int(n1)//int(n2)

T=int(input())
for z in range(T):
    data_list=list(input().split())
    operation =["+","-","*","/"]
    stack=[]
    flag=0 #error아님
    for i in range(len(data_list)):
        if flag==1:
            break
        if data_list[i]==".":
            if len(stack)>1:
                flag=1 #error인경우
            break
        elif data_list[i] in operation:
            if len(stack)<2:
                flag=1
                break
            else:
                tmp2=int(stack.pop())
                tmp1=int(stack.pop())
                stack.append(cal(tmp1,tmp2,data_list[i]))
        else:
            stack.append(data_list[i])
    print("#{}".format(z+1),end=' ')
    if flag ==0:
        rslt=stack.pop()
        print(rslt)
    else:
        print('error')