import sys

N = int(sys.stdin.readline())
card_list = sorted(list(map(int, input().split())))

M = int(sys.stdin.readline())
select_list = list(map(int, input().split()))

count_dic = {}
# 시간 초과
# for i in select_list:
#     count_dic[i] = 0
# 
# for i in card_list:
#     if i in select_list:
#         count_dic[i] += 1
# 
# for i in count_dic:
#     print(count_dic[i], end=' ')

# 다른 풀이
for i in card_list:
    if i in count_dic:
        count_dic[i] += 1
    else:
        count_dic[i] = 1

for i in select_list:
    if i in count_dic:
        print(count_dic[i], end=' ')
    else:
        print(0, end=' ')