from collections import deque

dq=deque('123')
dq.extendleft('123')
print(dq[::-1])