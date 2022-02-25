from collections import deque

dq = deque()

dq.append('a')

dq.appendleft('b')

print(dq)

dq.clear()

print(dq)

dq.append('a')

dq.extend('bcd')

print(dq)

dq.extendleft('xyz')

print(dq)

print(dq.index('x'))

dq.insert(3,'A')

print(dq)

dq.remove('A')

print(dq)

dq.reverse()

print(dq)