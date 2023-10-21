from collections import deque, Counter

def solution(progresses, speeds):
    answer = deque()
    for p, s in zip(progresses, speeds):
        rest_progress = 100-p

        if rest_progress % s == 0:
            answer.append(rest_progress // s)
        else:
            answer.append((rest_progress // s)+1)

    for i in range(len(answer)-1):
        if answer[i] > answer[i+1]:
            answer[i+1] = answer[i]

    co = Counter(answer)
    c = []
    for i, j in co.items():
        c.append(j)
    # print(c)

    return c