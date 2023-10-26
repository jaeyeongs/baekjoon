N = int(input())
num = []

for _ in range(N):
    a = [i for i in input().split()]
    num.append(a)

num.sort(key=lambda x: int(x[0]))

for i, j in num:
    print(i, j, sep=" ")