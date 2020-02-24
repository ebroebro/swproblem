#2164 카드2
n=int(input())
stack = list(range(n,0,-1))
while len(stack)>2:
    stack.pop()
    tmp=stack.pop()
    stack.insert(0,tmp)
print(stack[0])