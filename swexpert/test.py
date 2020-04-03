from collections import deque
import itertools

q=deque()
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
q.append(6)
q.append(7)
print(q)
print(q.popleft())
q2=list(itertools.islice(q,1,3))
print(q2)