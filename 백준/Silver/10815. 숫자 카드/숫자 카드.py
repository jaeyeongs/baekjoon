import sys

N = int(sys.stdin.readline())
card_list = set(list(map(int, input().split())))

M = int(sys.stdin.readline())
select_list = list(map(int, input().split()))

for i in select_list:
    if i in card_list:
        print(1, end=' ')
    else:
        print(0, end=' ')