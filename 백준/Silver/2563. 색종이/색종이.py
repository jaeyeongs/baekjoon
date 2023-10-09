N = int(input())
lst = []

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            lst.append((i, j))
            
s = set(lst)
print(len(s))