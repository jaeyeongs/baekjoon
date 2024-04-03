import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
num = []

for _ in range(N):
    num.append(int(input()))

num.sort()

print(round(sum(num)/N)) # 산술평균
print(num[N//2]) # 중앙값

# 최빈값
counter = Counter(num)
common = counter.most_common()

if len(common) > 1 and common[0][1] == common[1][1]:
    print(common[1][0])
else:
    print(common[0][0])

print(num[-1] - num[0]) # 범위