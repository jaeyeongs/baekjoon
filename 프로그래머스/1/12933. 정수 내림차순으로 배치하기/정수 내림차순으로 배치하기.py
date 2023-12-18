def solution(n):
    num = list(str(n))
    num = sorted(num, reverse=True)
    answer = int(''.join(num))
    return answer