# 버블 정렬
N = int(input())
lst = []
for i in range(N):
    lst.append(int(input()))

for i in range(N-1):
    for j in range(N-1, i, -1):
        if lst[j-1] > lst[j]:
            lst[j-1], lst[j] = lst[j], lst[j-1]

for i in lst:
    print(i)