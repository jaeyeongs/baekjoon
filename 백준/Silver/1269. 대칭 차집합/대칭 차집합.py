A, B = map(int, input().split())

A_list = set(list(map(int, input().split())))
B_list = set(list(map(int, input().split())))

print(len(A_list-B_list) + len(B_list-A_list))