from collections import deque

N, K = map(int, input().split())
q = deque(range(1, N+1))
result = []

while len(q) != 0:
    for _ in range(K-1):
        q.append(q.popleft())
    result.append(q.popleft())

print("<", end="")
print(", ".join(map(str, result)), end="")
print(">")