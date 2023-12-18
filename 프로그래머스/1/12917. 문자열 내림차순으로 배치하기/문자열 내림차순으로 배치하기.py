def solution(s):
    s_list = list(str(s))
    s_list = sorted(s_list, reverse=True)
    answer = ''.join(s_list)
    return answer