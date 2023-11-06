def solution(clothes):
    answer = 1
    dic = {i[1] : [] for i in clothes}

    for i in clothes:
        dic[i[1]].append(i[0])

    for i in dic.keys():
        n = len(dic[i])
        answer *= n+1

    return answer-1

# def solution(clothes):
#     clothes_type = {}

#     for c, t in clothes:
#         if t not in clothes_type:
#             clothes_type[t] = 2
#         else:
#             clothes_type[t] += 1

#     cnt = 1
#     for num in clothes_type.values():
#         cnt *= num

#     return cnt - 1