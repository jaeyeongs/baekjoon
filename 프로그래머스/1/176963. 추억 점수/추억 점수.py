def solution(name, yearning, photo):
    answer = []
    dic = dict(zip(name, yearning))
    
    for i in photo:
        result = 0
        for j in i:
            if j in dic:
                result += dic[j]
        answer.append(result)
        
    return answer