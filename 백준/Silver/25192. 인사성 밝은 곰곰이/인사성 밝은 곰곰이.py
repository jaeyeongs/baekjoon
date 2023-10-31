N = int(input())
dic = {}
cnt = 0

for _ in range(N):
    chat = input()
    if chat == 'ENTER':
        dic = {}
        continue
    if chat not in dic:
        dic[chat] = 0
        cnt += 1

print(cnt)