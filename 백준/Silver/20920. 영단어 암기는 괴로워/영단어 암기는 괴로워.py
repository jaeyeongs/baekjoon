import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())
dic = defaultdict(int)

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) < M:
        continue
    else:
        dic[word] += 1

print(*[i for i, j in sorted(dic.items(), key= lambda x: (-x[1],-len(x[0]),x[0]))], sep='\n')