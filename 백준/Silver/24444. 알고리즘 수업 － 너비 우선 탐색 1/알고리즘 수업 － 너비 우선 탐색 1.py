from collections import deque
import sys

input = sys.stdin.readline
N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
start = 1

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    global start
    q = deque([R])
    visited[R] = 1

    while q:
        v = q.popleft()
        graph[v].sort()

        for i in graph[v]:
            if visited[i] == 0:
                q.append(i)
                start += 1
                visited[i] = start

bfs(R)

for i in range(1, N+1):
    print(visited[i])