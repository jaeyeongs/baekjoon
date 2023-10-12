N, M = map(int, input().split())
word_list = []
check_list = []

for _ in range(N):
    word1 = input()
    word_list.append(word1)

for _ in range(M):
    word2 = input()
    check_list.append(word2)

count = 0

for i in check_list:
    if i in word_list:
        count += 1
    else:
        continue

print(count)