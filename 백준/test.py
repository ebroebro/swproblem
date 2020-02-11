top = -1
stack =[0]*10
Info = [0]*128   #특수부호는 128개정도네
Info[ord(')')]='('  #닫은 것의 index 에 열린거를 mapping
Info[ord(']')]='['
Info[ord('>')]='<'
Info[ord('}')]='{'
#오 이렇게 미리 mapping 해놓는거 좋네

isOkay=True

Data =input()
howmany = len(Data)

for now in range(howmany):
    if Data[now]=='(' or Data[now] =='<' or Data[now] =='[' or Data[now] =='{' :
        top+=1
        stack[top] =Data[now]
    elif Info[ord(Data[now])] ==stack[top] :
        top-=1
    elif Info[ord(Data[now])] !=stack[top]:
        isOkay=False
        break

if stack[top]:
    isOkay=False

print(isOkay)