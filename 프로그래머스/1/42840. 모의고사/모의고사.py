def solution(answers):
    result = []

    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]

    for i, answer in enumerate(answers):
        if student1[i%5] == answer:
            score[0] += 1
        if student2[i%8] == answer:
            score[1] += 1
        if student3[i%10] == answer:
            score[2] += 1

    for i in range(len(score)):
        if max(score) == score[i]:
            result.append(i+1)

    return result