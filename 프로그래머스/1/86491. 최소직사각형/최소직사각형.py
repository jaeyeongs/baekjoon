def solution(sizes):
    max_len = [] # 최대 길이 # [60, 70, 60, 80] -> 80
    min_len = [] # 최소 길이 # [50, 30, 30, 40] -> 50

    for w, h in sizes:
        if max(w, h): # 가로, 세로 중 최대값
            max_len.append(max(w, h))
        if min(w, h): # 가로, 세로 중 최솟값
            min_len.append(min(w, h))

    # 명함의 가로, 세로 길이 중 최대값과 가로, 세로 중 작은 값 중의 최대값
    result = max(max_len) * max(min_len)

    return result

