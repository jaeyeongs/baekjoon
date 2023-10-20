# def solution(s):
#     min_max_num = []
#     lst = [int(i) for i in s.split()]
#     # lst = list(map(int, s.split()))
#     for i in lst:
#         if i == max(lst):
#             min_max_num.append(i)
#         elif i == min(lst):
#             min_max_num.append(i)

#     result = ' '.join(map(str, sorted(min_max_num)))
#     return result

def solution(s):
    lst = list(map(int, s.split()))
    result = f'{min(lst)} {max(lst)}'
    return result