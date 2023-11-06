def solution(clothes):
    answer = 1
    dic = {i[1] : [] for i in clothes}

    for i in clothes:
        dic[i[1]].append(i[0])

    for i in dic.keys():
        n = len(dic[i])
        answer *= n+1

    return answer-1