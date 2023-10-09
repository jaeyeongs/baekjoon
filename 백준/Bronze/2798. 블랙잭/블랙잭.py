N, M = map(int, input().split())
card_list = list(map(int, input().split()))
card_sum = 0

for i in range(N):
    for j in range(i+1, N, 1):
        for k in range(j+1, N, 1):
            if card_list[i] + card_list[j] + card_list[k] > M:
                continue
            else:
                card_sum = max(card_sum, card_list[i] + card_list[j] + card_list[k])

print(card_sum)