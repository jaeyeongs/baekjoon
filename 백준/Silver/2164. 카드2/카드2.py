from collections import deque

N = int(input())
d = deque()

for i in range(1, N+1):
    d.append(i)

while len(d) != 1:
    d.popleft()
    if len(d) == 1:
        break
    d.append(d.popleft())

print(d[0])