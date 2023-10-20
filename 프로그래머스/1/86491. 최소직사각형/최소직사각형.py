def solution(sizes):
    max_len = []
    min_len = []

    for w, h in sizes:
        if max(w, h):
            max_len.append(max(w, h))
        if min(w, h):
            min_len.append(min(w, h))

    result = max(max_len) * max(min_len)

    return result