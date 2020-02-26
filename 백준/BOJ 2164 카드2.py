#2164 카드2
n=int(input())
stack = list(range(1,n+1))
while len(stack)>2:
    del stack[0]
    stack.append(stack[0])
    del stack[0]
print(stack[1])

print()