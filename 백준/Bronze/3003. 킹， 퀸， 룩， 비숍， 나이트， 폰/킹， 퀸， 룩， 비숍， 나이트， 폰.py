lst = list(map(int, input().split()))
cnt_lst = []

for i in range(len(lst)):
    if i == 0 or i == 1:
        cnt1 = 1 - lst[i]
        cnt_lst.append(cnt1)
    elif i >= 2 and i <= 4:
        cnt2 = 2 - lst[i]
        cnt_lst.append(cnt2)
    else:
        cnt3 = 8 - lst[i]
        cnt_lst.append(cnt3)

result = " ".join(map(str, cnt_lst))
print(result)