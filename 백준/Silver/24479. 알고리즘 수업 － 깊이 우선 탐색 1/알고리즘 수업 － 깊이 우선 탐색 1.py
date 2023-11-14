import sys
sys.setrecursionlimit(10**6)

def dfs(idx):
    global start
    visited[idx] = start
    graph[idx].sort()

    for i in graph[idx]:
        if visited[i] == 0:
            start += 1
            dfs(i)

input = sys.stdin.readline
N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
start = 1

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(R)

for i in range(1, N+1):
    print(visited[i])