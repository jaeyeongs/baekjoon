N = int(input())
num = []

for _ in range(N):
    a = [int(i) for i in input().split()]
    num.append(a)

num.sort()

for i, j in num:
    print(i, j, sep=" ")